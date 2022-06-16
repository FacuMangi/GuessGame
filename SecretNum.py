import random
def getSecretNum(NUMDIGITS):
    #Devuelve un string de numeros de NUMDIGITS de largo todos random.
    numbers = list(range(NUMDIGITS))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUMDIGITS):
        secretNum += str(numbers[i])
    return secretNum

