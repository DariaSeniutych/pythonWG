import matplotlib.pyplot as plt
import math

x_deg = range(-360, 361, 10)
f_values = []
h_values = []

for deg in x_deg:
    rad = math.radians(deg)

    # f(x)
    f_val = (math.exp(math.cos(rad)) +
             math.log((math.cos(0.6 * rad) ** 2) + 1) * math.sin(rad))
    f_values.append(f_val)

    # h(x)
    h_val = -math.log((math.cos(rad) + math.sin(rad)) ** 2 + 2.5) + 10
    h_values.append(h_val)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(x_deg, f_values, 'b-')
plt.title('f(x)')
plt.xlabel('Градусы')

plt.subplot(1, 2, 2)
plt.plot(x_deg, h_values, 'r-')
plt.title('h(x)')
plt.xlabel('Градусы')

plt.show()