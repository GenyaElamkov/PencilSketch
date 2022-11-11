import pytest

from main import get_files


def test_get_files_type():
    assert type(get_files('tests')) is list


def test_get_files_list():
    assert get_files('tests') == ['tests\\\\.pytest_cache',
                                  'tests\\\\image.jpg',
                                  'tests\\\\image.png',
                                  'tests\\\\new_image.jpg',
                                  'tests\\\\test_convert_drawing.py',
                                  'tests\\\\test_get_files.py',
                                  'tests\\\\test_save_drawing.py',
                                  'tests\\\\__pycache__']


def test_get_files_type_error():
    with pytest.raises(TypeError):
        get_files()
