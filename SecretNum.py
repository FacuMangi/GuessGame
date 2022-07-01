import random
def getSecretNum(NUM_DIGITS):
    #Devuelve un string compuesto por los digitos random unicos de NUMDIGITS.
    numbers = list(range(10))
    random.shuffle(numbers)
    
    #Agarra los primeros 3 numeros de la lista numbers y los agrega a secretNum como string.
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


