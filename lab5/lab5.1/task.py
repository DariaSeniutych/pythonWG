import os
import sys
import time
import csv
import re
import requests
from bs4 import BeautifulSoup
import argparse

# папочка для кэширования html-страниц
CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)


def get_cached_page(url):
    """возвращает содержимое страницы из кэша или загружает и кэширует"""
    safe_filename = url.replace("/", "_").replace(":", "_").replace("?", "_").replace("&", "_")
    filename = os.path.join(CACHE_DIR, safe_filename + ".html")
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        return response.text
    except requests.RequestException as e:
        print(f"ошибка при загрузке {url}: {e}", file=sys.stderr)
        return None


def clean_number(s):
    """удаляет запятые, пробелы и приводит к int или возвращает None"""
    if not s:
        return None
    s = re.sub(r"[^\d]", "", s)  # Оставляем только цифры
    return int(s) if s.isdigit() else None


def extract_country_info(country_name, html_content):
    """извлекает столицу, площадь и население из англоязычной википедии"""
    soup = BeautifulSoup(html_content, "html.parser")
    infobox = soup.find("table", class_="infobox")

    capital = "N/A"
    if infobox:
        capital_row = infobox.find("th", string=lambda x: x and "Capital" in x)
        if capital_row:
            td = capital_row.find_next("td")
            if td:
                a_tag = td.find("a")
                capital = a_tag.get_text(strip=True) if a_tag else td.get_text(strip=True)
                # Убираем уточнения в скобках
                if " (" in capital:
                    capital = capital.split(" (")[0]

    area = "N/A"
    if infobox:
        area_row = infobox.find("th", string=lambda x: x and ("Area" in x or "area" in x))
        if area_row:
            td = area_row.find_next("td")
            if td:
                text = td.get_text()
                match = re.search(r"([\d,]+)\s*km²", text)
                if match:
                    area = clean_number(match.group(1))
                else:
                    lines = text.splitlines()
                    for line in lines:
                        if "total" in line.lower() or "km" in line:
                            num_match = re.search(r"[\d,]+", line)
                            if num_match:
                                area = clean_number(num_match.group())
                                break

    population = "N/A"
    if infobox:
        pop_row = infobox.find("th", string=lambda x: x and ("Population" in x or "population" in x))
        if pop_row:
            td = pop_row.find_next("td")
            if td:
                text = td.get_text()
                numbers = re.findall(r"[\d,]+", text)
                if numbers:
                    population = clean_number(numbers[0])

    return {
        "country": country_name,
        "city": capital,
        "area": area,
        "population": population
    }


def main():
    parser = argparse.ArgumentParser(description="парсер данных о странах с англоязычной википедии")
    parser.add_argument("input", help="путь к файлу со списком стран (например, countries.txt)")
    parser.add_argument("output", help="путь к выходному CSV-файлу (например, countries_data.csv)")
    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            countries = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"ошибка: файл {args.input} не найден.", file=sys.stderr)
        sys.exit(1)

    results = []

    for country in countries:
        print(f"обработка: {country}...")
        url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
        html = get_cached_page(url)
        if html is None:
            results.append({
                "country": country,
                "city": "N/A",
                "area": "N/A",
                "population": "N/A"
            })
        else:
            info = extract_country_info(country, html)
            results.append(info)
        time.sleep(1)

    try:
        with open(args.output, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["country", "city", "area", "population"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"данные успешно сохранены в {args.output}")
    except Exception as e:
        print(f"ошибка при записи CSV: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()