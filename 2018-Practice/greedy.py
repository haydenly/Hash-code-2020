from in_out import *
from taxi import *

params, rawRides = load_data("d_metropolis.in")

vehicleCount = params[2]
bonus = params[4]

rides = [Ride(r[0],r[1],r[2],r[3],r[4],r[5]) for r in rawRides]

def distance(x1, y1, x2, y2):
    return abs(y2 - y1) + abs(x2 - x1)

points = 0

for i in range(1, vehicleCount + 1):
    currentX = 0
    currentY = 0
    step = 0
    for ride in rides:
        if ride.taxi == None:
            potentialStart = step + distance(currentX, currentY, ride.startX, ride.startY)
            if potentialStart <= ride.latestStart:
                points += ride.distance
                ride.taxi = i
                #wait until after early time
                distanceToStart = distance(currentX, currentY, ride.startX, ride.startY)
                startTime = max(step + distanceToStart, ride.early)
                
                if startTime == ride.early:
                    points += bonus

                step = startTime + ride.distance
                currentX = ride.finishX
                currentY = ride.finishY

for (i, ride) in enumerate(rides):
    print(i, ride.taxi)

print(points)