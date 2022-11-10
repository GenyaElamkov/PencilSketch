import os
import cv2


def convert_drawing(image: str) -> list:
    """Конвертирует изображение в карандашный рисунок"""
    # Считаем изображение
    img = cv2.imread(image)

    # Преобразуем исходное изображение в оттенки серого
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Инвертируем новое изображение в оттенки серого.
    inverted_img = 255 - gray_img

    # Размываем изображение по Гауссу
    blured = cv2.GaussianBlur(inverted_img, (21, 21), 0)

    # Инвертируем изображение. Преобразуем в карандашный рисунок
    inverted_blured = 255 - blured
    pencil_sketch = cv2.divide(gray_img, inverted_blured, scale=256.0)
    return pencil_sketch


def save_drawing(path: str, image: str, sketch: list) -> None:
    cv2.imwrite(f'{path}\\new_{image}', sketch)


def get_files(path: str) -> list:
    return [f"{path}\\\\{p}" for p in os.listdir(path)]


def main(path: str) -> None:
    for img in get_files(path):
        sketch = convert_drawing(img)
        res = img.replace(img[:img.rfind('\\') + 1], '')
        save_drawing(path, res, sketch)


if __name__ == '__main__':
    path = 'image'
    if not os.path.exists(path):
        os.makedirs(path)

    input(f'[!] Положите фотографии в папку [{path}], нажмите "Enter"')
    main(path)
    print(f'Ваши конвертированные фотографии сохранены в папке [{path}]')
    input('Для выхода нажмите "Enter"')
    # Показываем изображение в оригинале и карандаш.
    # cv2.imshow('Original', img)
    # cv2.imshow('Sketch', pencil_sketch)
    # cv2.waitKey(0)
