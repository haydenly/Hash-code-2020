import Library
import in_out
import preproccess

def maxLibrary(libraries):
    maxLib = None
    maxBook = 0
    for i in libraries:
        if(i.numberOfbooks >= maxBook):
            maxLib = i
            
            maxBook = i.numberOfbooks
    return maxLib

def sortBooks(books):
    return sorted(books, key = lambda book: book[1], reverse=True)


def chooseBooks(library,time,timeLim,booksused):   
    newTime = time + library.signUpTime
    remainingTime = timeLim - newTime
    booksToChoose = library.booksPerDay * remainingTime
    allbooks = zip(library.bookIndexes,library.bookScores)
    filteredBooks = list(filter(lambda book: booksused.get(book[0],-1)==-1,allbooks))
    #print("old books: {}, new books: {}".format(len(library.booksInLib),len(filteredBooks)))
    sortedBooks = [book[0] for book in sortBooks(filteredBooks)]
    finalChoice = sortedBooks[:booksToChoose]
    return finalChoice

def alg(timeLim, libraries):
    usedbooks = dict()
    output = []
    outputLibs = -1
    currentTime = 0
    while(currentTime <= timeLim):
        maxLib = maxLibrary(libraries)
        if(maxLib == None):
            break
        if(currentTime + maxLib.signUpTime >= timeLim):
            break
        libraries.remove(maxLib)
        bookChoice = chooseBooks(maxLib,currentTime,timeLim, usedbooks)
        for book in bookChoice:
            usedbooks[book]=1
        currentTime = currentTime + maxLib.signUpTime
        output.append([maxLib.ID])
        outputLibs += 1
        output[outputLibs] = output[outputLibs] + bookChoice
    return output
        


libraries = preproccess.getLibraries("d_tough_choices.txt")
outputMatrix = alg(libraries[0].timeLim,libraries)
print(outputMatrix)
in_out.out_data("d_answer_v2.txt", outputMatrix)







    


            


