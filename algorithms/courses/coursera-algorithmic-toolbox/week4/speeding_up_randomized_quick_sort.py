import random

def speeding_up_randomized_quick_sort(array, low=0, high=None):
    def partition3(array, low, high):
        # Randomly select pivot and swap it to the front
        rand_index = random.randint(low, high)
        array[low], array[rand_index] = array[rand_index], array[low]
        pivot = array[low]

        # Dutch National Flag: lt is the boundary of <pivot region,
        # gt is the boundary of >pivot region, i is the current element
        lt = low      # array[low..lt-1] < pivot
        gt = high     # array[gt+1..high] > pivot
        i = low + 1   # array[lt..i-1] == pivot

        while i <= gt:
            if array[i] < pivot:
                array[lt], array[i] = array[i], array[lt]
                lt += 1
                i += 1
            elif array[i] > pivot:
                array[gt], array[i] = array[i], array[gt]
                gt -= 1
            else:
                i += 1

        return lt, gt  # array[lt..gt] are all equal to pivot

    if high is None:
        high = len(array) - 1
    if low < high:
        lt, gt = partition3(array, low, high)
        speeding_up_randomized_quick_sort(array, low, lt - 1)
        speeding_up_randomized_quick_sort(array, gt + 1, high)
    return array


if __name__ == '__main__':

    n = int(input())
    integers = list(map(int, input().split()))
    result = speeding_up_randomized_quick_sort(integers)
    print(' '.join(str(num) for num in result))