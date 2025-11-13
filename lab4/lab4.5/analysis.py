import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# настройки
plt.rcParams['figure.figsize'] = (12, 7)
sns.set(style="whitegrid")

# загружаем данные
df = pd.read_excel("lab_4_part_5.xlsx", header=1)
df = df.drop(df.columns[0], axis=1)
df.columns = ["Дата", "Год", "Год_мес", "Точка", "Бренд", "Товар", "Количество", "Продажи", "Себестоимость"]
df['Дата'] = pd.to_datetime(df['Дата'])

# доп штуки
df['Средняя_цена'] = df['Продажи'] / df['Количество']
df['Прибыль'] = df['Продажи'] - df['Себестоимость']

print("данные обработаны, анализируем: \n")


# 1 динамика продаж по каждому товару (топ-5 товаров по выручке)

print("1 динамика по товарам (топ-5)")

top_products = df.groupby('Товар')['Продажи'].sum().nlargest(5).index
df_top = df[df['Товар'].isin(top_products)]

# агрегация по месяцу
df_top['Год_мес'] = df_top['Год_мес'].astype(str)
monthly_product = df_top.groupby(['Год_мес', 'Товар'])['Продажи'].sum().reset_index()

plt.figure()
sns.lineplot(data=monthly_product, x='Год_мес', y='Продажи', hue='Товар', marker='o')
plt.title(" динамика продаж по топ-5 товарам")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("1_sales_by_product.png")
print(" сохранён график: 1_sales_by_product.png")

# 2 динамикв по точкам продаж

print("\n2 динамика по точкам продаж")

top_points = df.groupby('Точка')['Продажи'].sum().nlargest(5).index
df_points = df[df['Точка'].isin(top_points)]
monthly_points = df_points.groupby(['Год_мес', 'Точка'])['Продажи'].sum().reset_index()

plt.figure()
sns.lineplot(data=monthly_points, x='Год_мес', y='Продажи', hue='Точка', marker='o')
plt.title(" динамика продаж по топ-5 точкам")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("2_sales_by_point.png")
print("сохранён график: 2_sales_by_point.png")


# 3 общий товарооборот

print("\n3 общий товарооборот")

total_monthly = df.groupby('Год_мес')['Продажи'].sum().reset_index()
total_monthly['Год_мес'] = total_monthly['Год_мес'].astype(str)

plt.figure()
plt.plot(total_monthly['Год_мес'], total_monthly['Продажи'], marker='o', linewidth=2)
plt.title("общий товарооборот по месяцам")
plt.xlabel("месяц")
plt.ylabel("продажи (руб.)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("3_total_turnover.png")
print(" сохранён график: 3_total_turnover.png")


# 4 средние продажи на точку и рост/спад

print("\n4 средние продажи и рост/спад")

# Средние продажи на точку (за весь период)
avg_per_point = df.groupby('Точка')['Продажи'].mean().sort_values(ascending=False)
print(" топ точек по средним продажам:")
print(avg_per_point.head())

# рост/спад, сравнение посл и предпосл месяцев
df['Год_мес'] = df['Год_мес'].astype(str)
monthly_total = df.groupby('Год_мес')['Продажи'].sum().sort_index()
if len(monthly_total) >= 2:
    last = monthly_total.iloc[-1]
    prev = monthly_total.iloc[-2]
    change = (last - prev) / prev * 100
    print(f"\n рост/спад: {change:+.2f}% (последний месяц к предыдущему)")


# 5 прогноз продаж по каждому товару

print("\n5 прогноз продаж на 3 месяца вперёд")

# преобразование год_мес в числовой признак
df_forecast = df.copy()
df_forecast['Год_мес'] = df_forecast['Год_мес'].astype(int)
df_forecast = df_forecast.sort_values('Год_мес')

forecasts = {}

for product in top_products:
    prod_data = df_forecast[df_forecast['Товар'] == product]
    monthly = prod_data.groupby('Год_мес')['Продажи'].sum().reset_index()

    if len(monthly) < 3:
        continue

    X = monthly['Год_мес'].values.reshape(-1, 1)
    y = monthly['Продажи'].values

    model = LinearRegression().fit(X, y)

    # аля прогноз на 3 некст месяца
    last_month = monthly['Год_мес'].max()
    future_months = np.array([last_month + 1, last_month + 2, last_month + 3]).reshape(-1, 1)
    pred = model.predict(future_months)

    forecasts[product] = pred

print("\n прогноз продаж по товарам (руб):")
for prod, pred in forecasts.items():
    print(f"{prod}: {[int(p) for p in pred]}")

print("\n анализ завершён, все графики сохранены")