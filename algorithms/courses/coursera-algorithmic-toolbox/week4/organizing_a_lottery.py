def organizating_a_lottery(segments, points):
    output = [0]*len(points) # setting up the output array

    for point in range(0, len(points)):
        for segment in segments:
            if points[point] >= segment[0] and points[point] <= segment[1]:
                output[point] += 1
    return output


if __name__ == '__main__':
    n,m = map(int, input().split())
    segments = []
    for segment in range(0, n):
        seg = tuple(map(int, input().split()))
        segments.append(seg)
    points = list(map(int, input().split()))
    result = organizating_a_lottery(segments=segments, points=points)
    print(' '.join(str(num) for num in result))


