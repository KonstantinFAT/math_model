import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y, t, C):
        '''Определение координат точки, времени и концентрации'''
        self.x = x
        self.y = y
        self.t = t
        self.C = float(C)


# Граничные условия
X = int(input("Введите граничное значние по X: "))  
Y = int(input("Введите граничное значние по Y: ")) 

# Создание сетки (изначально концентрация вещества везде равна нулю)
field = np.array([Point(i, j, 0, 0) for i in range(X) for j in range(Y)]).reshape(X,Y) #Создал матрицу точек, динамически задал координаты

# Помещение в поле источник вещества
X_source = int(input("Введите координаты источника выброса по X: "))
Y_source = int(input("Введите координаты источника выброса по Y: "))
C_source = float(input("Концентрация в точке: "))
field[X_source][Y_source] = Point(X_source, Y_source, 0, C_source)
c = np.array([j.C for i in field for j in i]).reshape(X, Y) # Поле концентраций

# Непроницаемый объект
impenetrable_object = np.array()



# Уравнение диффузии (явный метод)
D = 0.1 # Коэффициент диффузии
dx = 0.1  # Шаг по оси x
dy = 0.1  # Шаг по оси y
dt = 0.01  # Шаг по времени
T = 0.2  # Общее время интегрирования
Nt = int(T / dt)  # Количество временных слоев

# Влияение ветра
Vx = 5  # Горизонтальная компонента скорости ветра
Vy = 5  # Вертикальная компонента скорости ветра

# Параметры осаждения
S = 10  # Коэффициент осаждения

# Цикл по временным слоям
for t in range(Nt+1):
    
    # Визуализация (тепловая карта)
    heatmap = plt.imshow(c, cmap='viridis', vmin=0, vmax=1000) #cmap - стиль отображения карты, vmin/vmax - фиксированные значения шкалы
    plt.title(f"Уравнение диффузии, шаг по времени - {t}")
    plt.colorbar(heatmap)
    plt.show()
    
    # Цикл по узлам сетки
    for i in range(1, X - 1):
        for j in range(1, Y - 1):
            # Аппроксимация производных второго порядка
            d2u_dx2 = (c[i+1, j] - 2*c[i, j] + c[i-1, j]) / dx**2
            d2u_dy2 = (c[i, j+1] - 2*c[i, j] + c[i, j-1]) / dy**2
            du_dx = (c[i+1, j] - c[i-1, j]) / (2*dx)  # Новая аппроксимация по оси x
            du_dy = (c[i, j+1] - c[i, j-1]) / (2*dy)  # Новая аппроксимация по оси x

            # Явная схема
            c[i, j] = c[i, j] + dt * D * (d2u_dx2 + d2u_dy2) + dt * Vx * du_dx + + dt * Vy * du_dy + dt * S

