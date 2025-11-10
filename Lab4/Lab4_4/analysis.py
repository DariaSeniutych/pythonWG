import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# настройки
plt.rcParams['figure.figsize'] = (12, 7)
sns.set(style="whitegrid")

# загрузка данных
df = pd.read_excel("s7.xlsx")

# преобразование даты
df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
df['FLIGHT_DATE_LOC'] = pd.to_datetime(df['FLIGHT_DATE_LOC'])

# для удобства понимания сезонности добавим месяц вылета
df['FLIGHT_MONTH'] = df['FLIGHT_DATE_LOC'].dt.month
df['FLIGHT_YEAR'] = df['FLIGHT_DATE_LOC'].dt.year

print("данные загружены и обработаны\n")

# 1 общие описательные статистики

print("1 описательные статистики")
print(df['REVENUE_AMOUNT'].describe())
print(f"\nОбщая выручка: {df['REVENUE_AMOUNT'].sum():,} руб.")
print(f"Всего билетов: {len(df):,}")

# гистограмма сумм
plt.figure()
sns.histplot(df['REVENUE_AMOUNT'], bins=50, kde=True)
plt.title("Распределение сумм продаж")
plt.xlabel("Сумма (руб.)")
plt.ylabel("Частота")
plt.tight_layout()
plt.savefig("1_revenue_hist.png")
print(" сохранён график: 1_revenue_hist.png")

# 2 анализ аэропортов

print("2 топ-10 аэропортов вылета")
top_airports = df['ORIG_CITY_CODE'].value_counts().head(10)
print(top_airports)

plt.figure()
sns.barplot(x=top_airports.values, y=top_airports.index, palette="viridis")
plt.title("Топ-10 аэропортов вылета по количеству продаж")
plt.xlabel("Количество билетов")
plt.tight_layout()
plt.savefig("2_top_airports.png")
print(" сохранён график: 2_top_airports.png")

# 3 сезонность

print("3 сезонность продаж")
monthly = df.groupby('FLIGHT_MONTH').agg(
    total_revenue=('REVENUE_AMOUNT', 'sum'),
    ticket_count=('REVENUE_AMOUNT', 'size')
).reset_index()

print(monthly)

# график сезонности
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('Месяц')
ax1.set_ylabel('Выручка (млн руб.)', color=color)
ax1.bar(monthly['FLIGHT_MONTH'], monthly['total_revenue']/1e6, color=color, alpha=0.7)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Количество билетов (тыс.)', color=color)
ax2.plot(monthly['FLIGHT_MONTH'], monthly['ticket_count']/1e3, color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

plt.title("Сезонность: выручка и количество билетов по месяцам")
plt.tight_layout()
plt.savefig("3_seasonality.png")
print(" сохранён график: 3_seasonality.png")


# 4 типы пассажиров и статус


print("4 анализ по типу пассажиров и FFP")
# PAX_TYPE
pax_stats = df.groupby('PAX_TYPE')['REVENUE_AMOUNT'].agg(['count', 'mean', 'sum'])
print("\nПо типу пассажира:")
print(pax_stats)

# FFP_FLAG
df['FFP'] = df['FFP_FLAG'].notna()
ffp_stats = df.groupby('FFP')['REVENUE_AMOUNT'].agg(['count', 'mean'])
ffp_stats.index = ['Не в FFP', 'В FFP']
print("\n по программе лояльности (FFP):")
print(ffp_stats)

# 5 способ оплаты

print("5 способ оплаты (FOP_TYPE_CODE)")

fop_stats = df.groupby('FOP_TYPE_CODE').agg(
    count=('REVENUE_AMOUNT', 'size'),
    avg_revenue=('REVENUE_AMOUNT', 'mean')
).sort_values('count', ascending=False)

print(fop_stats)

plt.figure()
sns.barplot(data=fop_stats.reset_index(), x='avg_revenue', y='FOP_TYPE_CODE', palette="rocket")
plt.title("Средняя сумма продажи по способу оплаты")
plt.xlabel("Средняя сумма (руб.)")
plt.tight_layout()
plt.savefig("5_fop_analysis.png")
print(" сохранён график: 5_fop_analysis.png")

# 6 прогноз

print("6 упрощённый прогноз (линейный тренд по месяцам)")

# агрегация по месяцам год+месяц
df['YEAR_MONTH'] = df['FLIGHT_DATE_LOC'].dt.to_period('M')
monthly_trend = df.groupby('YEAR_MONTH').size().reset_index(name='tickets')
monthly_trend['YEAR_MONTH'] = monthly_trend['YEAR_MONTH'].dt.start_time

from sklearn.linear_model import LinearRegression
monthly_trend['days'] = (monthly_trend['YEAR_MONTH'] - monthly_trend['YEAR_MONTH'].min()).dt.days

X = monthly_trend[['days']]
y = monthly_trend['tickets']
model = LinearRegression().fit(X, y)

# прогноз на 3 месяца вперёд
last_date = monthly_trend['YEAR_MONTH'].max()
future_dates = pd.date_range(last_date + pd.offsets.MonthBegin(), periods=3, freq='MS')
future_days = (future_dates - monthly_trend['YEAR_MONTH'].min()).days

forecast = model.predict(future_days.values.reshape(-1, 1))

print("Прогноз количества билетов на ближайшие 3 месяца:")
for i, date in enumerate(future_dates):
    print(f"  {date.strftime('%Y-%m')}: {int(forecast[i])} билетов")

print("\n анализ завершён, все графики сохранены в папку")