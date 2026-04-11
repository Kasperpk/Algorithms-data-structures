def collection_signatures(segments):
    num_stops = 0
    stops = []
    stop = segments[0][1]
    while segments:
        for segment in segments:
            # finding the first segment stop
            if segment[1] < stop:
                stop = segment[1]

        num_stops = num_stops + 1
        stops.append(stop)
        segments = [segment for segment in segments if segment[0] > stop]

    return num_stops, stops