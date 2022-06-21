def getClues(guess, secretNum):
    #Devuelve las pistas Tito, Teto, Tato al usuario
    if guess == secretNum:
        return f'Felicidades! {secretNum} es el numero correcto!'
    
    clue = []

    for i in range(len(guess)):
        #i viene a representar un lugar "i" de los elementos pertenecientes al string guess (guess siendo un string compuesto por puros numeros, 3 en este caso).
        if guess[i] == secretNum[i]:
            clue.append('Teto')
        elif guess[i] in secretNum:
            clue.append('Tato')
    if len(clue) == 0:
        return 'Tito'
    
    clue.sort()
    return' '.join(clue)
        