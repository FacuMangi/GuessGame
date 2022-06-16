import random
from . import getSecretNum
from . import getClues






NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f'''Juego de deduccion en base a la logica.


Estoy pensando en un numero de {NUM_DIGITS} digitos.
Trata de adivinar cual es. Aqui hay algunas pistas:
Cuando diga:    Significa:
    Tito        Un digito es correcto pero esta en la posicion equivocada.
    Teto        Un digito es correcto y esta en la posicion correcta.
    Tato        Ningun digito es correcto.''')




    while True:
        # Esto guarda el numero secreto que el jugador debe adivinar en una variable.
        secretNum = getSecretNum()
        print('Acabo de pensar un numero.')
        print(f'Tenes {MAX_GUESSES} intento para adivinar.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Sigue en el loop hasta que entran un dato valido.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Intento #{numGuesses}')
            guess = input('> ')
