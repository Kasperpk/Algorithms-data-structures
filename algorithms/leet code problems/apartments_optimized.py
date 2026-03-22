def apartments(allowed_difference, desired_sizes, apartment_sizes):
    sorted_apartments = sorted(apartment_sizes)
    sorted_applications = sorted(desired_sizes)

    count = 0
    i = j = 0

    while i < len(sorted_applications) and j < len(sorted_apartments):
        diff = sorted_apartments[j] - sorted_applications[i]
        if abs(diff) <= allowed_difference:
            count += 1
            i += 1
            j += 1
        elif diff < 0:
            j += 1
        else:
            i += 1

    return count


if __name__ == '__main__':
    n,m, allowed_difference = map(int, input().split())
    desired_sizes = list(map(int, input().split()))
    apartment_sizes = list(map(int, input().split()))


    result = apartments(allowed_difference=allowed_difference, desired_sizes=desired_sizes, apartment_sizes=apartment_sizes)
    print(result)