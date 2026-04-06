def missing_number(lo,hi,numbers):
    if lo == hi:
        return lo
    mid = (lo + hi) // 2
    left  = [x for x in numbers if x <= mid]
    right = [x for x in numbers if x > mid]
    expected_left_count = mid - lo + 1
    if len(left) == expected_left_count:
        return missing_number(mid + 1, hi, right)
    else:
        return missing_number(lo, mid, left)   
    
if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    result = missing_number(1,n, numbers)
    print(result)
    
    