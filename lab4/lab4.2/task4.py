import numpy as np
from scipy import integrate

# Одномерная функция: 7x^2 + 23x + 16
def f(x):
    return 7*x**2 + 23*x + 16

print("Одномерный интеграл: ∫ (7x² + 23x + 16) dx")
a = float(input("Введите нижний предел (a): "))
b = float(input("Введите верхний предел (b): "))

single_integral, _ = integrate.quad(f, a, b)

# Двумерная функция: добавим y^2 для зависимости от двух переменных
def integrand(y, x):
    return 7*x**2 + 23*x + 16 + y**2

print("\nДвойной интеграл: ∫∫ (7x² + 23x + 16 + y²) dy dx")
x_a = float(input("Введите нижний предел по x: "))
x_b = float(input("Введите верхний предел по x: "))
y_a = float(input("Введите нижний предел по y: "))
y_b = float(input("Введите верхний предел по y: "))

double_integral, _ = integrate.dblquad(
    integrand,
    x_a, x_b,
    lambda x: y_a,
    lambda x: y_b
)

print(f"\nОдномерный интеграл = {single_integral:.6f}")
print(f"Двойной интеграл = {double_integral:.6f}")