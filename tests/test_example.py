import pytest
from models_functions import predict_lr



def multiply(a, b):
    return a * b


@pytest.mark.parametrize("input_a, input_b, expected", [(2, 3, 6), (0, 5, 0), (-2, 4, -8), (3, 3, 9)])
def test_multiplication(input_a, input_b, expected):
    result = multiply(input_a, input_b)
    assert result == expected





