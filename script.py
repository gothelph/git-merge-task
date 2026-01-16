def sort(array):
    arr = array.copy()      # чтобы не менять исходный массив
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    data = [5, 2, 9, 1, 3]
    sorted_data = sort(data)
    print(sorted_data)


main()
