import Library
import in_out
import preproccess

def maxLibrary(libraries):
    maxLib = None
    maxBook = 0

    for i in libraries:
        factor = int((i.booksPerDay*2 + i.numberOfbooks)/(1.5*i.signUpTime))
        if(factor >= maxBook):
            maxLib = i
            
            maxBook = factor
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
    sortedBooks = library.bookIndexes
    finalChoice = sortedBooks[:booksToChoose]
    return finalChoice

#sorted library
def alg(timeLim, libraries):
    output = []
    outputLibs = 0
    currentTime = 0
    #usedBooks = set()
    while(currentTime <= timeLim):
        maxLib = maxLibrary(libraries)
        if(maxLib == None):
            break
        if(currentTime + maxLib.signUpTime >= timeLim):
            break
        libraries.remove(maxLib)
        bookChoice = chooseBooks(maxLib,currentTime,timeLim)

        #usedBooks.update(bookChoice)

        currentTime = currentTime + maxLib.signUpTime
        output.append([maxLib.ID])
        output[outputLibs] = output[outputLibs] + bookChoice
        outputLibs += 1

    return output

def alg2(timeLim, libraries):
    output = []
    outputLibs = 0
    currentTime = 0
    #usedBooks = set()
    sortFactor = int(len(libraries)*0.1)
    while(currentTime <= timeLim):
        maxLib = libraries[0]
        if(maxLib == None):
            break
        if(currentTime + maxLib.signUpTime >= timeLim):
            break
        bookChoice = chooseBooks(maxLib,currentTime,timeLim)
        libraries.pop(0)

        #usedBooks.update(bookChoice)

        currentTime = currentTime + maxLib.signUpTime
        output.append([maxLib.ID])
        output[outputLibs] = output[outputLibs] + bookChoice
        outputLibs += 1
        if(outputLibs % 1 == 0):
            for i in libraries:
                i.setScore(timeLim - currentTime)
            libraries.sort(key = lambda x: x.score, reverse= True)
        

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
        in_out.out_data(i + "alganswer.txt", outputMatrix)
        print("done: " + i)

solve(anslist)



