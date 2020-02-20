from in_out import *

class book:
    score = 0
    def __init__(self,score, id):
        self.score = score
        self.id = id

class library:
    bookScores  = []
    bookIndexes = []
    ID = 0
    numberOfbooks = 0
    signUpTime  = 0
    booksPerDay  = 0
    timeLim = 0


    def __init__(self, bookScores , bookIndexes , signUpTime , booksPerDay,ID,timeLim):
        self.bookIndexes=bookIndexes
        self.signUpTime=signUpTime
        self.booksPerDay=booksPerDay
        self.numberOfbooks = len(bookIndexes)
        self.ID = ID
        self.timeLim = timeLim
        self.score = 0
        self.booksInLib = sorted([book(bookScores[index], index) for index in bookIndexes], reverse = True, key = lambda x : x.score)
    
    def setScore(timeRemaining): 
        daysOfProccessing = timeRemaining - lib.signUpTime
        booksCanProccess = min(daysOfProccessing * lib.booksPerDay, lib.numberOfbooks)

        ##ASSUMES LIST OF BOOKS IN ORDER OF SCORE
        totalThroughput = sum(lib.bookScoresInLib[:booksCanProccess])
        score = totalThroughput


    