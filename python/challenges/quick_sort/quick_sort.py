def QuickSort(list,left,right):

    if left < right:

        position = Partition(list,left,right)
        QuickSort(list,left,position-1)
        QuickSort(list,position+1,right)

    return list

def Partition(list,left,right):

    pivot = list[right]
    low = left - 1

    for i in range(left,right):
        if list[i] <= pivot:
            low+=1
            Swap(list,i,low)

    Swap(list,right,low+1)

    return low+1

def Swap(list,i,low):

    temp = list[i]
    list[i] = list[low]
    list[low] = temp

if __name__ == '__main__':
    QuickSort([8,4,23,42,16,15],0,5)
