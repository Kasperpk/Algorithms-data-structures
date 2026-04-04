def wierd_algorithm(number, sequence=''):
    sequence = sequence + ' ' + str(number)
    if number == 1:
        return sequence.strip()
    if number%2 == 0:
        number = int(number / 2)
    else:
        number = int(number*3+1)
    return wierd_algorithm(number, sequence)

if __name__ == '__main__':
    number = int(input())
    result = wierd_algorithm(number)
    print(result)