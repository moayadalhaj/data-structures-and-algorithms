def insertionSort(list):
    for i in range(1,len(list)):
        j = i-1
        temp = list[i]

        while j>=0 and temp < list[j]:
            j=j-1
        list.pop(i)
        list.insert(j+1,temp)

    return list

if __name__ == "__main__":
    list = [8,4,23,42,16,15]
    print(insertionSort(list))
