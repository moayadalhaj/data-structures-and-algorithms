from .hashtable import HashTable

def left_join(left_hash, right_hash):
    """
    A function that takes to two ashtables as arguments
    LEFT JOIN means all the values in the first hashmap are returned,
    and if values exist in the “right” hashmap, they are appended to the result row
    """
    output = []
    for item in left_hash._buckets:
        if item:
            if right_hash.contains(item.head.value[0]):
                right_item = right_hash.get(item.head.value[0])
                output.append([item.head.value[0], item.head.value[1],right_item])
            else:
                output.append([item.head.value[0], item.head.value[1],'Null'])
    return output

if __name__ == '__main__':
    left_hash = HashTable()
    left_hash.add('fond','enamored')
    left_hash.add('wrath','anger')
    left_hash.add('diligent','employed')

    right_hash = HashTable()
    right_hash.add('fond','averse')
    right_hash.add('wrath','delight')
    right_hash.add('guide','follow')

    print(left_join(left_hash,right_hash))
