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


x = np.arange(-5, 6, 0.1)
y = func(x)
os.makedirs("results1", exist_ok=True)
out_file = os.path.join("results1", "function_2_results1.txt")
with open(out_file, "w") as f_out:
    for x_val, y_val in zip(x, y):
        f_out.write(f"{x_val:.5f}    {y_val:.5f}\n")
print(f"Файл с результатами сохранён: {out_file}")

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("График функции №2")
plt.grid(True)
plt.savefig("function_2_plot.png", dpi=200)
plt.show()
