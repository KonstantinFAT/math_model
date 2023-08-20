import numpy as np

# Создание сетки (изначально концентрация вещества везде равна нулю)
field = np.zeros_like(np.linspace(np.linspace(0,10,11), 10, 11))

# Помещение в поле источник вещества, обозначим через концентрацию C
C = 50
X = 5
Y = 5
field[X][Y] = C
print(field)

