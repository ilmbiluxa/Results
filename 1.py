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

x = np.arange(-5, 5.1, 0.1)
y = func(x)

# Создаем папку results, если её нет
os.makedirs("results", exist_ok=True)
with open("results/func1.txt", "w", encoding="utf-8") as f_out:
    for x_val, y_val in zip(x, y):
        f_out.write(f"{x_val:.5f}    {y_val:.5f}\n")

print("Результаты сохранены в файл:", filename)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("График функции")
plt.grid(True)


plot_filename = "results/function_2_plot.png"
plt.savefig(plot_filename, dpi=200)
plt.show()
