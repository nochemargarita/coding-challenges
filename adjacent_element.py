def adjacentElementsProduct(inputArray):
    
    product = None
    for i in range(len(inputArray) - 1):
        answer = inputArray[i] * inputArray[i + 1]
        if answer > product:
            product = answer
            
    return product
        

inputArray = [3, 6, -2, -5, 7, 3]
inputArray: [-23, 4, -3, 8, -12]
adjacentElementsProduct(inputArray)