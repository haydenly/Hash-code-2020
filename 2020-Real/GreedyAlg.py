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

def scoreSort(currentTime,libraries):
    maxLib = None
    maxBook = 0
    for i in libraries:
        if(i.numberOfbooks >= maxBook):
            maxLib = i
            
            maxBook = i.numberOfbooks
    return maxLib

def sortBooks(books,bookScore):
    books.sort(key = lambda x: bookScore[x], reverse = True)
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
        if(maxLib == None):
            break
        if(currentTime + maxLib.signUpTime >= timeLim):
            break
        libraries.remove(maxLib)
        bookChoice = chooseBooks(maxLib,currentTime,timeLim)
        currentTime = currentTime + maxLib.signUpTime
        output.append([maxLib.ID])
        outputLibs += 1
        output[outputLibs] = output[outputLibs] + bookChoice
    return output
        




b = "b_read_on"
c = "c_incunabula"
d = "d_tough_choices"
e = "e_so_many_books"
f = "f_libraries_of_the_world"
anslist = [b,c,d,e,f]

def solve(anslist):
    for i in anslist:
        libraries = preproccess.getLibraries(i + ".txt")
        outputMatrix = alg(libraries[0].timeLim,libraries)
        in_out.out_data(i + "answer.txt", outputMatrix)

solve(anslist)








    


            


