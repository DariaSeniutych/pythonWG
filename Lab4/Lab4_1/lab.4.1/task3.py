import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Цвета
body = "#5cc6e8"
outline = "#0077a4"

# Создаём холст
fig, ax = plt.subplots(figsize=(7, 9))
ax.set_aspect('equal')
ax.axis('off')

# --- УШИ ---
ax.add_patch(patches.Ellipse((-1.0, 3.1), 1.0, 4.2, angle=12, facecolor=body, edgecolor=outline, linewidth=8))
ax.add_patch(patches.Ellipse((1.0, 3.1), 1.0, 4.2, angle=-12, facecolor=body, edgecolor=outline, linewidth=8))

# --- ГОЛОВА ---
ax.add_patch(patches.Circle((0, 0), 2.25, facecolor=body, edgecolor=outline, linewidth=8))

# --- ГЛАЗА (обратная асимметрия) ---
ax.add_patch(patches.Ellipse((-0.6, 0.8), 1.0, 1.0, facecolor='white', edgecolor=outline, linewidth=6))
ax.add_patch(patches.Ellipse((0.6, 0.8), 1.0, 1.25, facecolor='white', edgecolor=outline, linewidth=6))
ax.add_patch(patches.Circle((-0.6, 0.8), 0.25, color='black'))
ax.add_patch(patches.Circle((0.6, 0.8), 0.25, color='black'))

# --- НОС ---
nose_color = "#f36d6d"  # розовый, как у Кроша
nose_outline = "#d63031"
ax.add_patch(patches.Circle((0, 0.1), 0.22, facecolor=nose_color, edgecolor=nose_outline, linewidth=4))

# --- УЛЫБКА (тоньше и с круглыми краями) ---
ax.add_patch(patches.Arc((0, -0.25), 1.7, 1.2, angle=0, theta1=215, theta2=325, color='black', linewidth=4))

''' 
# --- ЗУБЫ (торчат из-под улыбки, ближе к центру) ---
tooth_width = 0.22
tooth_height = 0.4
tooth_y = -0.85  # подняли ближе к улыбке

# Левый зуб
ax.add_patch(patches.Rectangle((-tooth_width - 0.05, tooth_y), tooth_width, tooth_height,
                               facecolor='white', edgecolor='white', linewidth=3))

# Правый зуб
ax.add_patch(patches.Rectangle((0.05, tooth_y), tooth_width, tooth_height,
                               facecolor='white', edgecolor='white', linewidth=3))
'''

# --- РУКИ и НОГИ — ОДИНАКОВЫЕ, СКРУГЛЁННЫЕ
# Форма: плоский овал = "скруглённый прямоугольник"
arm_leg_width = 1.4
arm_leg_height = 0.8

# Левая рука / левая нога
ax.add_patch(patches.Ellipse((-2.0, -0.3), arm_leg_width, arm_leg_height, angle=20, facecolor=body, edgecolor=outline, linewidth=8))
ax.add_patch(patches.Ellipse((-0.8, -2.2), arm_leg_width, arm_leg_height, angle=10, facecolor=body, edgecolor=outline, linewidth=8))

# Правая рука / правая нога
ax.add_patch(patches.Ellipse((2.0, -0.3), arm_leg_width, arm_leg_height, angle=-20, facecolor=body, edgecolor=outline, linewidth=8))
ax.add_patch(patches.Ellipse((0.8, -2.2), arm_leg_width, arm_leg_height, angle=-10, facecolor=body, edgecolor=outline, linewidth=8))

# Настройка области
plt.xlim(-4, 4)
plt.ylim(-3, 7)
plt.show()