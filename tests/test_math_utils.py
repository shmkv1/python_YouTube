from src.math_utils import multiply

def test_basic_math():
    assert 2 + 2 == 4

def test_multyply():
    assert multiply(3, 5) == 15, "функция отработала не правильно"