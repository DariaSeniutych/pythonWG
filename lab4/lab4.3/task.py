import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random

np.random.seed(42)
random.seed(42)
fake = Faker('ru_RU')

YEARS = list(range(2021, 2026))
SPECIALTY = "программная инженерия"
FORMS = ["дневная (бюджет)", "дневная (платная)", "заочная (платная)"]

# аля распределение форм обучения (учитывая, что бюджет ограничен)
form_probs = {
    2021: [0.3, 0.5, 0.2],
    2022: [0.28, 0.52, 0.2],
    2023: [0.25, 0.55, 0.2],
    2024: [0.24, 0.56, 0.2],
    2025: [0.22, 0.58, 0.2],
}

# данные генерируем
data = []

for year in YEARS:
    n_students = np.random.randint(120, 181)  # 120–180 студентов в год
    forms = np.random.choice(FORMS, size=n_students, p=form_probs[year])

    for form in forms:
        ct_rus = np.random.randint(20, 101)
        ct_math = np.random.randint(20, 101)
        ct_phys = np.random.randint(15, 101)

        school_avg = round(np.random.uniform(8.5, 10.0), 1)
        total_score = ct_rus + ct_math + ct_phys + school_avg * 10

        full_name = fake.name()
        address = f"г. {fake.city()}, {fake.street_address()}"
        phone = "+375" + random.choice(["29", "33", "44", "25"]) + str(np.random.randint(10000000, 99999999))

        data.append({
            "ФИО": full_name,
            "Год поступления": year,
            "Форма обучения": form,
            "Балл ЦТ русский": ct_rus,
            "Балл ЦТ математика": ct_math,
            "Балл ЦТ физика": ct_phys,
            "Средний балл аттестата": school_avg,
            "Общий балл при поступлении": round(total_score, 1),
            "Специальность": SPECIALTY,
            "Адрес регистрации": address,
            "Номер мобильного телефона": phone
        })

df = pd.DataFrame(data)
# динамика среднего балла ЦТ по предметам
ct_means = df.groupby('Год поступления')[['Балл ЦТ русский', 'Балл ЦТ математика', 'Балл ЦТ физика']].mean()

plt.figure(figsize=(10, 5))
plt.plot(ct_means.index, ct_means['Балл ЦТ русский'], label='Русский язык', marker='o')
plt.plot(ct_means.index, ct_means['Балл ЦТ математика'], label='Математика', marker='o')
plt.plot(ct_means.index, ct_means['Балл ЦТ физика'], label='Физика', marker='o')
plt.title('Динамика среднего балла ЦТ по предметам (2021–2025)')
plt.xlabel('Год')
plt.ylabel('Средний балл')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# динамика среднего балла аттестата
school_means = df.groupby('Год поступления')['Средний балл аттестата'].mean()

plt.figure(figsize=(8, 4))
plt.plot(school_means.index, school_means.values, marker='s', color='green')
plt.title('Динамика среднего балла аттестата (2021–2025)')
plt.xlabel('Год')
plt.ylabel('Средний балл аттестата')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# динамика проходного балла (минимум на бюджете)
budget_df = df[df['Форма обучения'] == 'дневная (бюджет)']
passing_score = budget_df.groupby('Год поступления')['Общий балл при поступлении'].min()

plt.figure(figsize=(8, 4))
plt.plot(passing_score.index, passing_score.values, marker='D', color='red')
plt.title('Динамика проходного балла на бюджет (Программная инженерия)')
plt.xlabel('Год')
plt.ylabel('Проходной балл')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# количество поступивших по формам обучения
form_counts = df.groupby(['Год поступления', 'Форма обучения']).size().unstack(fill_value=0)

form_counts.plot(kind='bar', figsize=(10, 5), stacked=False)
plt.title('Количество поступивших по формам обучения (2021–2025)')
plt.xlabel('Год')
plt.ylabel('Число студентов')
plt.xticks(rotation=0)
plt.legend(title='Форма обучения')
plt.tight_layout()
plt.show()

# статистика по формам обучения (всего за 5 лет)
total_by_form = df['Форма обучения'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(total_by_form.values, labels=total_by_form.index, autopct='%1.1f%%', startangle=90)
plt.title('Распределение студентов по формам обучения (2021–2025)')
plt.tight_layout()
plt.show()
