from challenges.insertion_sort.insertion_sort import insertionSort


def test_insertion_Sort():
    expected = [4, 8, 15, 16, 23, 42]
    actual = insertionSort([8,4,23,42,16,15])
    assert actual == expected

def test_reverse_sorted():
    expected = [-2, 5, 8, 12, 18, 20]
    actual = insertionSort([20,18,12,8,5,-2])
    assert actual == expected

def test_few_uniques():
    expected = [5, 5, 5, 7, 7, 12]
    actual = insertionSort([5,12,7,5,5,7])
    assert actual == expected

def test_nearly_sorted():
    expected = [2,3,5,7,11,13]
    actual = insertionSort ([2,3,5,7,13,11])
    assert actual == expected
