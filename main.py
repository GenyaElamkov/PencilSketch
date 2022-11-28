import os
import cv2
import numpy


def convert_drawing(image: str) -> numpy.ndarray:
    """Конвертирует изображение в карандашный рисунок."""
    # Считаем изображение.
    img = cv2.imread(image)

    # Преобразуем исходное изображение в оттенки серого.
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Инвертируем новое изображение в оттенки серого.
    inverted_img = 255 - gray_img

    # Размываем изображение по Гауссу. GaussianBlur -  меняя аргументы, меняться четкость.
    blured = cv2.GaussianBlur(inverted_img, (21, 21), 0)

    # Инвертируем изображение. Преобразуем в карандашный рисунок.
    inverted_blured = 255 - blured
    pencil_sketch = cv2.divide(gray_img, inverted_blured, scale=256.0)
    return pencil_sketch


def save_drawing(folder: str, image: str, sketch: numpy.ndarray) -> None:
    cv2.imwrite(f'{folder}\\new_{image}', sketch)


def get_files(folder: str) -> list:
    """Возвращает путь к файлу изображения."""
    return [f"{folder}\\\\{p}" for p in os.listdir(folder)]


def main(folder: str) -> None:
    if not os.path.exists(folder):
        os.makedirs(folder)

    for path in get_files(folder):
        sketch = convert_drawing(path)
        name = path.replace(path[:path.rfind('\\') + 1], '')
        save_drawing(folder, name, sketch)


if __name__ == '__main__':
    folder = 'image'  # Имя директории, где сохранять.
    input(f'[!] Положите фотографии в папку [{folder}], нажмите "Enter"')
    main(folder)
    print(f'Ваши конвертированные фотографии сохранены в папке [{folder}]')
    input('Для выхода нажмите "Enter"')
