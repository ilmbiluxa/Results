import numpy as np
import matplotlib.pyplot as plt
import os

def func(x):
    return (
        -20 * np.exp(-0.2 * np.sqrt(0.5 * x**2))
        - np.exp(0.5 * (np.cos(2 * np.pi * x) + 1))
        + np.e
        + 20
    )

# Создаём массив значений x с шагом 0.1 от -5 до 5 включительно
x = np.arange(-5, 5.1, 0.1)

# Вычисляем значения функции
y = func(x)

# Создаём папку "results", если её нет, чтобы сохранить результаты
os.makedirs("results", exist_ok=True)

# Путь к файлу с результатами (внутри папки results)
filename = "results/func1.txt"

# Записываем пары (x, y) в файл с форматированием
with open(filename, "w", encoding="utf-8") as f_out:
    for x_val, y_val in zip(x, y):
        f_out.write(f"{x_val:.5f}    {y_val:.5f}\n")

print(f"Результаты сохранены в файл: {filename}")

# Строим график функции
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("График функции")
plt.grid(True)
plt.savefig("function_2_plot.png", dpi=200)  # Сохраняем график в файл
plt.show()  # Показываем график на экране
