from challenges.merge_sort.merge_sort import Merge, Mergesort

def test_merge_sort():
    expected = [4, 8, 15, 16, 23, 42]
    actual = Mergesort([8,4,23,42,16,15])
    assert actual == expected

def test_merge_sort_reverse_sorted():
    reversed_array = [20,18,12,8,5,-2]
    Mergesort(reversed_array)
    assert reversed_array == [-2, 5, 8, 12, 18, 20]

def test_merge_sort_unique():
    expected = [5, 5, 5, 7, 7, 12]
    actual = Mergesort([5,12,7,5,5,7])
    assert actual == expected

def test_merge_sort_nearly_sorted():
    expected = [2, 3, 5, 7, 11, 13]
    actual = Mergesort([2,3,5,7,13,11])
    assert actual == expected
