from mean import compute_mean

def test_empty():
    l0 = []
    res = compute_mean(l0)
    assert res == 0

def test_one_elem():
    assert compute_mean([6]) == 6
