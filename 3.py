import numpy
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource

def func1(x1, x2):
    r = numpy.sqrt(x1**2 + x2**2)
    val = numpy.sin(x1) * numpy.cos(x2) * numpy.exp(numpy.abs(1 - r / numpy.pi))
    return -numpy.abs(val)

def makeData():
    # Создаем сетку значений по x1 и x2 в диапазоне [-10, 10]
    x1 = numpy.linspace(-10, 10, 100)
    x2 = numpy.linspace(-10, 10, 100)
    xgrid, ygrid = numpy.meshgrid(x1, x2)
    Z = func1(xgrid, ygrid)
    return xgrid, ygrid, Z

if __name__ == '__main__':
    # Тестовая точка
    x10, x20 = 8.05502, 9.66459
    y0 = func1(x10, x20)

    xgrid, ygrid, Z = makeData()

    fig = plt.figure(figsize=(14, 12))
    
    # 1. Трехмерная поверхность (изометрический вид с освещением)
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    ls = LightSource(azdeg=315, altdeg=45)
    rgb = ls.shade(Z, cmap=plt.cm.viridis)
    surf1 = ax1.plot_surface(xgrid, ygrid, Z, facecolors=rgb, rcount=40, ccount=40, linewidth=0, shade=False)
    ax1.set_xlabel('x1')
    ax1.set_ylabel('x2')
    ax1.set_zlabel('y = f(x1, x2)')
    ax1.set_title('3D Surface (Изометрический вид)')
    ax1.view_init(elev=30, azim=45)

    # 2. Трехмерная поверхность (вид сверху - перпендикулярно XOY)
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    surf2 = ax2.plot_surface(xgrid, ygrid, Z, cmap='viridis', rcount=40, ccount=40, linewidth=0, antialiased=True)
    ax2.set_xlabel('x1')
    ax2.set_ylabel('x2')
    ax2.set_zlabel('y = f(x1, x2)')
    ax2.set_title('3D Surface (Вид сверху)')
    ax2.view_init(elev=90, azim=-90)

    # 3. График y = f(x1) при фиксированном x2 = x20
    ax3 = fig.add_subplot(2, 2, 3)
    x1_line = numpy.linspace(-10, 10, 300)
    y_slice1 = func1(x1_line, x20)
    ax3.plot(x1_line, y_slice1, color='blue', label='f(x1, x2 fixed)')
    ax3.scatter(x10, y0, color='red', label='Тестовая точка')
    ax3.set_xlabel('x1')
    ax3.set_ylabel(f'y = f(x1, x2={x20:.5f})')
    ax3.set_title('Срез функции по x1')
    ax3.legend()
    ax3.grid(True)

    # 4. График y = f(x2) при фиксированном x1 = x10
    ax4 = fig.add_subplot(2, 2, 4)
    x2_line = numpy.linspace(-10, 10, 300)
    y_slice2 = func1(x10, x2_line)
    ax4.plot(x2_line, y_slice2, color='green', label='f(x2, x1 fixed)')
    ax4.scatter(x20, y0, color='red', label='Тестовая точка')
    ax4.set_xlabel('x2')
    ax4.set_ylabel(f'y = f(x1={x10:.5f}, x2)')
    ax4.set_title('Срез функции по x2')
    ax4.legend()
    ax4.grid(True)

    fig.suptitle(f'Тестовая точка: (x1, x2) = ({x10:.5f}, {x20:.5f}), f = {y0:.5f}', fontsize=16)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

