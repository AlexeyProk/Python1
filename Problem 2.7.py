


#implement the Bubble Sort algorithm in Python to sort a list of numbers in ascending order?
def bubble_sort(array):
    if len(array) <= 1:
        return array

    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array [j + 1], array[j]
    return array
#Test
numbers = [51, 654, 65, 1, 15, 7]
sorted_numbers = bubble_sort(numbers)
print("List", sorted_numbers)