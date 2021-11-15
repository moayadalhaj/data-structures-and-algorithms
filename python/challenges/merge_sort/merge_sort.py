def Mergesort(list):
    """
    A function so split the list to sub-lists until each sub-list consists of a single element
    """
    n = len(list)

    if n > 1:
      mid = int(n/2)
      left = list[0:mid]
      right = list[mid:]
      Mergesort(left)
      Mergesort(right)
      Merge(left, right, list)
    return list

def Merge(left, right, list):
    """
    A function that merging those sub-lists in a manner that results into a sorted list.
    """
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            list[k] = left[i]
            i = i + 1
        else:
            list[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
    while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

if __name__ == "__main__":
    print(Mergesort([8,4,23,42,16,15]))
