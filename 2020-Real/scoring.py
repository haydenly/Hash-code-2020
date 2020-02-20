from in_out import *
from Library import library

(params, bookscores, libs) = load_data("a_example.txt")


print(params, bookscores, libs)

def score(lib, timeRemaining):
    daysOfProccessing = timeRemaining - lib.signUpTime
    booksCanProccess = min(daysOfProccessing * lib.booksPerDay, lib.numberOfbooks)

    ##ASSUMES LIST OF BOOKS IN ORDER OF SCORE
    totalThroughput = sum(lib.bookScoresInLib[:booksCanProccess])
    return totalThroughput


    