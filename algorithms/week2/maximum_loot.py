def sort_items(items):
    for i in range(0, len(items)):
        key = items[i]
        j = i-1
        unit_value = items[i][1] / items[i][0]
        while j >= 0 and unit_value > items[j][1]/items[j][0]:
            items[j+1] = items[j]
            j-=1
        items[j+1] = key

    return items

def knapsack(w, items):
    sort_items(items)
    print(items)
    amounts = [0] * len(items)
    total_value = 0
    for i in range(0, len(items)):
        if w == 0:
            return (total_value, amounts)

        a = min(items[i][0], w)

        # calculate the new total value of knapsack
        total_value = total_value+a*(items[i][1]/items[i][0])

        # decrease the amount of item i with unit a
        items[i][0] = items[i][0]-a

        # reflect that we took a units of weight of the item at position i
        amounts[i] = amounts[i] + a
        w = w - a
    return total_value, amounts

if __name__ == '__main__':
    n, w = map(int, input().split())
    items = []
    for i in range(0, n):
        print(items)
        items.append(tuple(map(int, input().split())))
    result = knapsack(w, items)
    print(result)