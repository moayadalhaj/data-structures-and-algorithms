def QuickSort(list,left,right):
    """
    A function that takes list, left=0, right=len(list), as arguments
    then pass these arguments to Partition function that each loop take a pivot

    input: list, int, int
    output: sorted list
    """
    if left < right:

        position = Partition(list,left,right)
        QuickSort(list,left,position-1)
        QuickSort(list,position+1,right)

    return list

def Partition(list,left,right):
    """
    Partition function that each loop take a list[right] equal to pivot
    then check the values that less than this pivot if the condition meet this
    condition it will pass the index of value that is grater than pivot to Swap function

    input: list, left, right
    output: index of the value that is grater than pivot
    """

    pivot = list[right]
    low = left - 1

    for i in range(left,right):
        if list[i] <= pivot:
            low+=1
            Swap(list,i,low)

    Swap(list,right,low+1)

    return low+1

def Swap(list,i,low):
    """
    A function to swap between pivot and the first great value in the list

    input: list, i: int, low: int
    output: list
    """
    temp = list[i]
    list[i] = list[low]
    list[low] = temp

if __name__ == '__main__':
    QuickSort([8,4,23,42,16,15],0,5)
