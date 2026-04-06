def increasing_array(n,numbers):
    num_moves = 0
    for num in range(0,n):
        if num+1 < len(numbers) and numbers[num] > numbers[num+1]:
            num_moves += numbers[num] - numbers[num+1]
            #while numbers[num+1] < numbers[num]:
            #    numbers[num+1] += 1
            #    num_moves += 1
    
    return num_moves

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    result = increasing_array(n=n, numbers=numbers)
    print(result)
