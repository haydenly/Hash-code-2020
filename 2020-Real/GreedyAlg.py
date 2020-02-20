import Library

def maxLibrary(libraries):
    maxLib = None
    maxBook = 0
    for i in libraries:
        if(i.numberOfbooks > maxBook):
            maxLib = i
            maxBook = i.numberOfbooks
    return maxLib

def sortBooks(books,bookScore):
    books.sort(key = lambda x: bookScore[x], reversed = True)
    return books

def chooseBooks(library,time,timeLim):   
    newTime = time + library.signUpTime
    remainingTime = timeLim - newTime
    booksToChoose = library.booksPerDay * remainingTime
    sortedBooks = sortBooks(library.bookIndexes,library.bookScores)
    finalChoice = sortedBooks[:booksToChoose]
    return finalChoice

def alg(timeLim, libraries):
    output = []
    outputLibs = -1
    currentTime = 0
    while(currentTime <= timeLim):
        maxLib = maxLibrary(libraries)
        if(currentTime + maxLib.signUpTime >= timeLim):
            break
        libraries.remove(maxLib)
        bookChoice = chooseBooks(maxLib,currentTime,timeLim)
        currentTime = currentTime + maxLib.signUpTime
        output.append([maxLib.ID])
        outputLibs += 1
        output[outputLibs] = output[outputLibs] + bookChoice
        








    


            


