# tests/test_app.py
from app.main import sumar

def test_sumar():
    assert sumar(2, 3) == 5
