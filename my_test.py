from my_code import inc


def test_inc():
    assert 5 == inc(4)
    assert 1 == inc(0)
    assert 0 == inc(-1)
