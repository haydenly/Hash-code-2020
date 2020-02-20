from Library import library
from in_out import *


def getLibraries(fname):
    params, bookscores, libs = load_data(fname)
    timeLim = params[2]
    libraryList = [library(bookscores,lib[1],lib[0][1],lib[0][2],i,timeLim)
                    for (i,lib) in enumerate(libs)]
    return libraryList

