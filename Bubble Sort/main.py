def bubble_sort(item_list):
    n = len(item_list)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if item_list[j] > item_list[j + 1]:
                item_list[j], item_list[j + 1] = item_list[j + 1], item_list[j]
                swapped = True

        if not swapped:
            break


arr = [5, 3, 6, 1, 7, 2, 10, 4]

bubble_sort(arr)

print(arr)
