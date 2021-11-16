from challenges.quick_sort.quick_sort import QuickSort

def test_merge_sort():
    expected = [4, 8, 15, 16, 23, 42]
    sample_list = [8,4,23,42,16,15]
    actual = QuickSort(sample_list,0,len(sample_list)-1)
    assert actual == expected

def test_merge_sort_reverse_sorted():
    expected = [-2, 5, 8, 12, 18, 20]
    reverse_sorted = [20,18,12,8,5,-2]
    actual = QuickSort(reverse_sorted,0,len(reverse_sorted)-1)
    assert actual == expected

def test_merge_sort_unique():
    expected = [5, 5, 5, 7, 7, 12]
    unique = [5,12,7,5,5,7]
    actual = QuickSort(unique,0,len(unique)-1)
    assert actual == expected

def test_merge_sort_nearly_sorted():
    expected = [2, 3, 5, 7, 11, 13]
    nearly_sorted = [2,3,5,7,13,11]
    actual = QuickSort(nearly_sorted,0,len(nearly_sorted)-1)
    assert actual == expected
