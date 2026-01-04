def test_one_two():
    x = 1
    y = 2
    assert x + y == 3

def test_diff_contains():
    x = {'a': 1, 'b': 2}
    expected = {'a': 1}
    assert expected.items() <= x.items()
