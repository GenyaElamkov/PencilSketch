from main import save_drawing, convert_drawing

import os


def test_save_drawing():
    sketch = convert_drawing("tests\\image.jpg")
    save_drawing('tests', 'image.jpg', sketch)

    assert 'new_image.jpg' in os.listdir('tests')
