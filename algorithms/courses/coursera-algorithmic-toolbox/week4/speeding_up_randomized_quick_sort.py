def speeding_up_randomized_quick_sort(array, low=0, high=None):
    def partition(array, low, high):
        pivot = array[high]  # setting the current pivot to the last element in the input array
        current_index_in_low_array = low - 1  # defining the pointer for the current index in the
        # low part of the array
        for index in range(low, high):  # looping through elements from low to high
            if array[index] <= pivot:  # if element at index is less than pivot, increment and put at
                # start of the array
                current_index_in_low_array += 1
                array[current_index_in_low_array], array[index] = array[index], array[current_index_in_low_array]
        array[current_index_in_low_array + 1], array[high] = array[high], array[current_index_in_low_array + 1]
        return current_index_in_low_array + 1
    if high is None:
        high = len(array) - 1
    if low < high:
        pivot_index = partition(array, low, high)
        speeding_up_randomized_quick_sort(array, low, pivot_index - 1)
        speeding_up_randomized_quick_sort(array, pivot_index + 1, high)
    return array


if __name__ == '__main__':

    n = int(input())
    integers = list(map(int, input().split()))
    result = speeding_up_randomized_quick_sort(integers)
    print(' '.join(str(num) for num in result))