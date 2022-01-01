from .models import Station
from .models import Track

def dijkstra(source, destination):

    listOfTracks = Track.objects.all()
    graph = {}

    for track in listOfTracks:
        src = str(track.source)
        dst = str(track.destination)

        if src not in graph:
            graph[src] = []
        
        if dst not in graph:
            graph[dst] = []

        graph[src].append((dst, track.track_line))
        graph[dst].append((src, track.track_line))

    trackList = []
    lineChange = []

    stationQueue = [(source, -1)]
    isStationVisited = set()
    parentStation = {}

    while stationQueue:
        currentStation = stationQueue[0][0]
        curLine = stationQueue[0][1]
        stationQueue.pop(0)

        if currentStation in isStationVisited:
            continue

        isStationVisited.add(currentStation)

        if currentStation == destination:
            break

        for track in graph[currentStation]:
            nextStation = track[0]
            nextLine = track[1]
            if nextStation in isStationVisited:
                continue

            parentStation[nextStation] = (currentStation, nextLine)
            stationQueue.append((nextStation, nextLine))

    currentStation = destination

    while currentStation != source:
        trackList.append([parentStation[currentStation][0], currentStation, parentStation[currentStation][1], False])
        currentStation = parentStation[currentStation][0]

    trackList.reverse()

    lineChange.append(False)
    trackList[0][3] = False
    for i in range(1, len(trackList)):
        lineChange.append(True if trackList[i][2] != trackList[i - 1][2] else False)
        trackList[i][3] = lineChange[-1]

    return trackList