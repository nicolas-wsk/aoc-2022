import os
import pydash
import re
import math
from scipy.spatial import distance as distanceScipy


path = f'{os.path.dirname(__file__)}/inputs/15.txt'


sensors = []
beacons = []
link = {}

with open(path) as f:
    lines = f.readlines()

    for line in lines:
        [xSensor, ySensor, xBeacon, yBeacon] = re.findall(r'-?\d+', line)
        sensors.append((int(xSensor), int(ySensor)))
        beacons.append((int(xBeacon), int(yBeacon)))
        link[(int(xSensor), int(ySensor))] = (int(xBeacon), int(yBeacon))

maxXSensors = max(sensors, key=lambda x: x[0])[0]
minYSensors = min(sensors, key=lambda x: x[1])[1]
maxYSensors = max(sensors, key=lambda x: x[1])[1]
minXSensors = min(sensors, key=lambda x: x[0])[0]

maxXBeacons = max(beacons, key=lambda x: x[0])[0]
minYBeacons = min(beacons, key=lambda x: x[1])[1]
maxYBeacons = max(beacons, key=lambda x: x[1])[1]
minXBeacons = min(beacons, key=lambda x: x[0])[0]

maxX = max(maxXSensors, maxXBeacons)
minX = min(minXSensors, minXBeacons)
maxY = max(maxYSensors, maxYBeacons)
minY = min(minYSensors, minYBeacons)

print(maxX, minX, maxY, minY)
# print(sensors)
# print(beacons)


# Solution 2: ( but too slow :/ )

maxLineY = 4000000

for lineY in range(maxLineY + 1):
    start = set()
    filled = set()
    intervals = []

    for x in range(maxLineY + 1):
        start.add((x, lineY))
    # print(start)

    for (sensorX, sensorY) in sensors:
        n = link[(sensorX, sensorY)]

        distanceToBeacon = distanceScipy.cityblock((sensorX, sensorY), n)

        dx = distanceToBeacon - abs(sensorY - lineY)
        if dx <= 0:
            continue

        intervals.append((sensorX - dx, sensorX + dx))

    for (x1, x2) in intervals:
        for x in range(x1, x2 + 1):
            filled.add((x, lineY))

    diff = start.difference(filled)
    if diff:
        print(diff)


# SOLUTION 1 :
# filled = set()
# lineY = 2000000

# intervals = []

# for (sensorX, sensorY) in sensors:
#     n = link[(sensorX, sensorY)]

#     distanceToBeacon = distanceScipy.cityblock((sensorX, sensorY), n)

#     dx = distanceToBeacon - abs(sensorY - lineY)
#     if dx <= 0:
#         continue

#     intervals.append((sensorX - dx, sensorX + dx))


# for (x1, x2) in intervals:
#     for x in range(x1, x2):
#         filled.add((x, lineY))


# print(len(filled))
