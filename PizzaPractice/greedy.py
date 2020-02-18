from practice import load_data, out_data

params, sliceSizes = load_data("e_also_big.in")

print(params, sliceSizes)

maxVal = params[0]
typeNum = params[1]

total = 0
chosenSizes = []
chosenPizzas = []

for i in range(typeNum - 1, 0, -1):
    currentSliceCount = sliceSizes[i]
    potentialTotal = total + currentSliceCount
    if potentialTotal == maxVal:
        break
    elif potentialTotal < maxVal:
        total = potentialTotal
        chosenSizes.append(currentSliceCount)
        chosenPizzas.append(i)

#chosenSizes.reverse()
#print(chosenSizes)
#print(sum(chosenSizes))

out_data(chosenPizzas, "chosenpizzas.txt")
