import pandas as pd

# загрузка с пропуском первой строки, там где заголовки
df = pd.read_excel("lab_4_part_5.xlsx", header=1)

# удаляем первый столбик, тк он пустой, все NaN
df = df.drop(df.columns[0], axis=1)

df.columns = [
    "Дата", "Год", "Год_мес", "Точка", "Бренд",
    "Товар", "Количество", "Продажи", "Себестоимость"
]

# преобразвание даты
df['Дата'] = pd.to_datetime(df['Дата'])

print("данные загружены")
print(df.head())
print("\nСтолбцы:", df.columns.tolist())