def car_fueling(distance, miles, stops):
    num_stops = 0
    stops = stops + [distance] # adding the final distance to last stop

    while distance > 0:
        if stops[-1] <= m:  # if last stop within reach return
            return num_stops
        if stops[1] > miles:
            return -1
        best_stop = 0
        for stop in stops:
            if stop <= miles:
                best_stop = stop
        num_stops += 1
        best_stop_index = stops.index(best_stop)
        stops = stops[best_stop_index:]
        stops = [stop-best_stop for stop in stops]
        distance = distance - best_stop
    return num_stops

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    result = car_fueling(d,m,stops)
    print(result)









