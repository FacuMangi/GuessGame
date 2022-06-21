import random
from SecretNum import getSecretNum
import Clues
from itsOnlyDigits import isOnlyDigits
import Dificulty





MAX_GUESSES = 10


def main():
    print ('Nivel de dificultad? (1, 2 o 3)')
    selection = input('>')
    NUM_DIGITS = Dificulty.setDificulty(selection)

    print(f'''Juego de deduccion en base a la logica.


Estoy pensando en un numero de {NUM_DIGITS} digitos.
Trata de adivinar cual es. Aqui hay algunas pistas:
Cuando diga:    Significa:
    Tato        Un digito es correcto pero esta en la posicion equivocada.
    Teto        Un digito es correcto y esta en la posicion correcta.
    Tito        Ningun digito es correcto.''')




    while True:
        # Esto guarda el numero secreto que el jugador debe adivinar en una variable.
        secretNum = getSecretNum(NUM_DIGITS)
        print('Acabo de pensar un numero.')
        print(f'Tenes {MAX_GUESSES} intentos para adivinar.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Sigue en el loop hasta que entran un dato valido.
            while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
                print(f'Intento #{numGuesses}')
                guess = input('> ')

            clues = Clues.getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break #Adivinaron asi que el loop se rompe.
            if numGuesses > MAX_GUESSES:
                print('Se te acabaron los intentos :(')
                print(f'Tu numero secreto era {secretNum}')

            #Pregunta si queres jugar otra vez.
        print('Queres jugar otra vez? (si/no)')
        if not input('> ').lower().startswith('s'):
            break
        print('GRACIAS POR JUGAR')

if __name__ == '__main__':
    main()