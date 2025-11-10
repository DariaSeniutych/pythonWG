import numpy as np

# 1. Ввод данных
lengths_str = input("Введите длины участков через пробел: ").strip()
speeds_str = input("Введите средние скорости через пробел: ").strip()
k = int(input("Номер участка, на котором въехал (начиная с 1): "))
p = int(input("Номер участка, после которого выехал (начиная с 1): "))

# 2. Преобразование строк в массивы NumPy
lengths = np.array(list(map(float, lengths_str.split())))
speeds = np.array(list(map(float, speeds_str.split())))

# 3. Проверка: k и p должны быть в пределах количества участков
if k < 1 or p > len(lengths) or k > p:
    print("❌ Ошибка: неверные номера участков!")
else:
    # Индексы в Python начинаются с 0 → k-1 до p-1 (включительно)
    start_idx = k - 1
    end_idx = p - 1  # включительно!

    # 4. Выбираем нужные участки
    selected_lengths = lengths[start_idx:end_idx+1]
    selected_speeds = speeds[start_idx:end_idx+1]

    # 5. Расчёт
    total_distance = np.sum(selected_lengths)  # S
    total_time = np.sum(selected_lengths / selected_speeds)  # T = Σ(Si / Vi)
    avg_speed = total_distance / total_time  # V = S / T

    # 6. Вывод результата
    print("\n✅ Результаты:")
    print(f"🔹 Длина пути (S): {total_distance:.2f} км")
    print(f"🔹 Время в пути (T): {total_time:.2f} часа")
    print(f"🔹 Средняя скорость (V): {avg_speed:.2f} км/ч")

    # 7. Для проверки — вывод выбранных участков
    print(f"\n📌 Участки с {k} по {p}:")
    for i in range(len(selected_lengths)):
        print(f"   Участок {start_idx + i + 1}: длина={selected_lengths[i]} км, скорость={selected_speeds[i]} км/ч")