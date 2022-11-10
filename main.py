import os
import cv2


def convert_drawing(image: str) -> list:
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
    # Показываем изображение в оригинале и карандаш.
    # cv2.imshow('Original', img)
    # cv2.imshow('Sketch', pencil_sketch)
    # cv2.waitKey(0)


def save_drawing(image: str, sketch: list) -> None:
    cv2.imwrite(f'image\\new_{image}', sketch)


def get_files(path: str) -> list:
    return [f"{path}\\{p}" for p in os.listdir(path)]


def main(arr_img: list):
    print(arr_img)
    for img in arr_img:
        print(img)
        # convert_drawing(img)


if __name__ == '__main__':
    path = 'image'
    main(get_files(path))
    # main(res)
    # print(res)
    # print(get_files(path))
    # img = convert_drawing('image\\WhatsApp Image 2022-02-14 at 21.19.21.jpeg')
    # save_drawing('WhatsApp Image 2022-02-14 at 21.19.21.jpeg', img)
