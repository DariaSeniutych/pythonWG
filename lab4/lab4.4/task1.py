import pandas as pd

df = pd.read_excel("s7.xlsx")

print("файл загружен")
print("\n первые 5 строк:")
print(df.head())

print("\n столбцы:")
print(df.columns.tolist())

print("\n типы данных:")
print(df.dtypes)

print("\n пропуски:")
print(df.isnull().sum())