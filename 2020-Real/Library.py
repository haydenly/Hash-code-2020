class book:
    score = 0
    def __init__(self,score):
        self.score = score

class library:
    bookScores  = []
    bookIndexes = []
    ID = 0
    numberOfbooks = 0
    signUpTime  = 0
    booksPerDay  = 0


    def __init__(self, bookScores , bookIndexes , signUpTime , booksPerDay,ID):
        self.bookScores=bookScores
        self.bookIndexes=bookIndexes
        self.signUpTime=signUpTime
        self.booksPerDay=booksPerDay
        self.numberOfbooks = len(bookIndexes)
        self.ID = ID
    


