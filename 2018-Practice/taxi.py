#ride class for each individual ride
class ride:
    def __init__(self,a,b,x,y,s,f):
        self.startX = a
        self.finishX = x
        self.startY = b
        self.finishY = y
        self.early = s
        self.late = f
        self.start = [a,b]
        self.finish = [x,y]

#taxi class stores all the rides and data
class Taxi:
    rides = []

    def __init__(self,params):
        self.rows, self.cols, self.vehicleCount, self.rideCount, self.bonus, self.steps, self.tempRides = params
        
        
    def rideConvert(self):
        for r in self.tempRides:
            self.rides.append(ride(r[0],r[1],r[2],r[3],r[4],r[5]))
    

