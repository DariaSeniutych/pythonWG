import matplotlib.pyplot as plt
import math

x_values = []
f_values = []

for i in range(-1000, 1001):
    x = i * 0.01

    if abs(x - (-3)) > 0.1 and abs(x - 3) > 0.1:
        denominator = x ** 2 - 9
        if abs(denominator) > 0.001:
            f_val = 5 / denominator

            if abs(f_val) < 20:
                x_values.append(x)
                f_values.append(f_val)

plt.figure(figsize=(10, 6))
plt.plot(x_values, f_values, 'purple', linewidth=2)
plt.title('График функции $f(x) = \\frac{5}{x^2 - 9}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)

plt.axvline(x=-3, color='red', linestyle='--', alpha=0.7, label=' - точки разрыва')
plt.axvline(x=3, color='red', linestyle='--', alpha=0.7)
plt.legend()

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()

print("График построен! Точки разрыва при x = -3 и x = 3")
