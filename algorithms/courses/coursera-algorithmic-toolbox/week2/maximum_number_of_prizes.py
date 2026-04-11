def maximum_number_of_prizes(n):
    '''
    :param n: Number to be split into maximum pairwise integers
    :return: The number of integers and the integers themselves
    '''

    # initializing variables
    num_integers = 0
    sum = 0
    integers = []
    num = 1

    # start while loop that continues until sum is n.
    while sum != n:

        # if num + num + 1 is not greater than n-sum then we can
        # add that next number as a pairwise object
        # example if we have the n = 8, then first 1+1+1 > 8-0 is taken
        # and we add 1 to the sum and increment num.
        # on the next iteration it is 2+2+1 (5) > 8-1 is still false
        # so we take the branch
        if not num + num + 1 > n-sum:
            sum = sum + num
            integers.append(num)
            num_integers += 1
            num += 1

        # else we have to add the remaining until we reach the sum
        else:
            integers.append(n-sum)
            num_integers += 1
            sum = sum + (n-sum)
            num += 1
    return num_integers, integers

if __name__ == '__main__':
    n = int(input())
    result = maximum_number_of_prizes(n)
    print(result)
