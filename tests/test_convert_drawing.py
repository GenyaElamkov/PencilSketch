import numpy

from main import convert_drawing


def test_convert_drawing_type():
    assert type(convert_drawing("tests\\image.png")) is numpy.ndarray
