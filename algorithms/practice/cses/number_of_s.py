matrix = [[1,2,9,10,25],
          [4,3,8,11,24],
          [5,6,7,12,23],
          [16,15,14,13,22],
          [17,18,19,20,21]]

def number_of_s(rows_cols):
    res = []

    for rc in rows_cols:
        res.append(matrix[rc[0]-1][rc[1]-1])

    return res


if __name__ == '__main__':
    n = int(input())
    rc = []
    for row_col in range(0, n):
        rc.append(tuple(map(int, input().split())))

    result = number_of_s(rc)

    print(' '.join(str(num) for num in result))