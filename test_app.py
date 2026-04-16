from app import add, divide

def test_add():
    assert add(2, 3) == 4

def test_divide():
    assert divide(10, 2) == 5