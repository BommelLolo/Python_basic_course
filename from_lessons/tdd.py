# O(len(hay))
# O(log(len(hay)))

def binary_search(needle, hay):
    if not hay:
        return None

    middle_point = len(hay) // 2
    if needle == hay[middle_point]:
        return middle_point

    if needle < hay[middle_point]:
        return binary_search(needle, hay[:middle_point])

    inner_index = binary_search(needle, hay[middle_point + 1:])
    if inner_index is None:
        return None

    return middle_point + 1 + inner_index


if __name__ == '__main__':
    arr = [1, 4, 7, 10, 15, 17, 19]
    arr.sort()
    arr1 = [1, 4, 7, 10, 15, 17, 19, 22]
    arr1 = sorted(arr1)

    assert binary_search(10, arr) == 4
    assert binary_search(15, arr1) == 4

    assert binary_search(1, arr) == 0
    assert binary_search(1, arr1) == 0
    assert binary_search(4, arr) == 1
    assert binary_search(4, arr1) == 1
    assert binary_search(0, arr) is None
    assert binary_search(0, arr1) is None
    assert binary_search(13, arr) is None
    assert binary_search(17, arr) == 5
    assert binary_search(13, arr1) is None
    assert binary_search(19, arr1) == 6
    assert binary_search(20, arr) is None
    assert binary_search(25, arr1) is None
