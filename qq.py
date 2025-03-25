import matplotlib.pyplot as plt
import random
import numpy as np

def task_1(size=5):
    if size % 2 == 0:
        raise ValueError("Размер спрайта должен быть нечетным для центральной симметрии.")

    half_size = size // 2
    sprite = np.zeros((size, size), dtype=int)

    # Заполняем случайными значениями левую половину и центральный столбец
    for i in range(size):
        for j in range(half_size + 1):
            sprite[i, j] = random.randint(0, 1)

    # Зеркально отражаем левую половину для создания правой
    for i in range(size):
        for j in range(half_size):
            sprite[i, size - 1 - j] = sprite[i, j]

    return sprite

# Генерируем случайный симметричный спрайт 5x5
sprite = generate_symmetric_sprite()

# Отображаем спрайт с помощью imshow
plt.imshow(sprite, cmap='binary', interpolation='nearest')
plt.title('Случайный симметричный спрайт 5x5')
plt.xticks(range(5))
plt.yticks(range(5))
plt.grid(True)
plt.show()

