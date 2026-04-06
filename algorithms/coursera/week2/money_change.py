def money_change(n):
    '''

    :param n: integer coin
    :return: the minimum number of coins with denominations 1,5,10 that
    changes that money
    '''

    num_coins = 0
    coin_value = n
    while coin_value != 0:

        if coin_value >= 10:
            coin_value = coin_value - 10
            num_coins += 1

        elif coin_value >= 5:
            coin_value = coin_value - 5
            num_coins += 1

        else:
            coin_value = coin_value - 1
            num_coins += 1
    return num_coins

if __name__ == '__main__':
    n = int(input())
    result = money_change(n)
    print(result)

