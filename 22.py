import argparse
import sys
import matplotlib.pyplot as plt

def createParser():
    parser = argparse.ArgumentParser(description="""Это невероятно полезная программа,
                                                    которая строит графики по входящему 
                                                    текстовому файлу с координатами
                                                    и позволяет выбирать стиль линии              
                                     """)
    parser.add_argument("name", type=argparse.FileType(),
                        help="Входной текстовый файл с координатами (X Y)")
    parser.add_argument("--linestyle", choices=["solid", "dashed", "dotted"], default="solid",
                        help="Стиль линии: solid — сплошной (по умолчанию), dashed — штриховой, dotted — пунктирный")
    return parser

def read_xy_pairs(file_object):
    X = []
    Y = []
    for line in file_object:
        if line.strip():
            parts = line.strip().split()
            if len(parts) >= 2:
                x, y = float(parts[0]), float(parts[1])
                X.append(x)
                Y.append(y)
    return X, Y


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    print(namespace)

    X_values, Y_values = read_xy_pairs(namespace.name)
    print(f"X:", X_values)
    print(f"Y:", Y_values)

    plt.plot(X_values, Y_values, linestyle=namespace.linestyle)
    plt.title("График из файла с выбором стиля линии")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
