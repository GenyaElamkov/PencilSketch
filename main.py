import cv2


def main(image: str) -> None:
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
    pencil_scetch = cv2.divide(gray_img, inverted_blured, scale=256.0)

    # Показываем изображение в оригинале и карандаш.
    # cv2.imshow('Original', img)
    # cv2.imshow('Scetch', pencil_scetch)
    # cv2.waitKey(0)

    cv2.imwrite(f'new_{image}', pencil_scetch)


if __name__ == '__main__':
    image = 'dother.jpeg'
    main(image)
