#%%
def ferris_wheel(max_weight, child_weights):
    weights = sorted(child_weights)
    gondolas = 0
    left = 0
    right = len(weights) - 1

    while left <= right:
        if left == right:
            # Only one child left - rides alone
            gondolas += 1
            break
        if weights[left] + weights[right] <= max_weight:
            left += 1
            right -= 1
        else:
            right -= 1

        gondolas += 1

    return gondolas

if __name__ == '__main__':
    n, w = map(int, input().split())
    weights = list(map(int, input().split()))
    result = ferris_wheel(w, weights)
    print(result)