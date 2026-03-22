def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers)//2
    left_half = numbers[:middle]
    right_half = numbers[middle:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []

    # pointers to keep track of where to insert numbers in array
    index = pointer = 0

    while index < len(left) and pointer < len(right):

        if left[index] < right[pointer]:
            result.append(left[index])
            index += 1
        else:
            result.append(right[pointer])
            pointer += 1

    result.extend(left[index:])
    result.extend(right[pointer:])

    return result

def apartments(allowed_difference, desired_sizes, apartment_sizes):

    sorted_apartments = merge_sort(apartment_sizes)
    sorted_applications = merge_sort(desired_sizes)
    number_of_apartments_occupied = 0
    apartment_index = 0
    application_index = 0
    while sorted_apartments and sorted_applications:
            difference = sorted_apartments[apartment_index] - sorted_applications[application_index]
            if abs(difference) <= allowed_difference:
                number_of_apartments_occupied = number_of_apartments_occupied + 1
                sorted_apartments.remove(sorted_apartments[apartment_index])
                sorted_applications.remove(sorted_applications[application_index])
                application_index = 0
            else:
                # if we have reached the final element in applications
                # then reset the application index and progress the
                # apartment
                if application_index + 1 > len(sorted_applications) - 1:
                    application_index = 0
                    sorted_apartments.remove(sorted_apartments[apartment_index])

                else:
                    application_index += 1

    return number_of_apartments_occupied


if __name__ == '__main__':
    n,m, allowed_difference = map(int, input().split())
    desired_sizes = list(map(int, input().split()))
    apartment_sizes = list(map(int, input().split()))


    result = apartments(allowed_difference=allowed_difference, desired_sizes=desired_sizes, apartment_sizes=apartment_sizes)
    print(result)