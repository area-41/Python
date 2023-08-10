""" The Minion Game
Regras do jogo
    Ambos os jogadores recebem a mesma string, string.
    Ambos os jogadores devem fazer substrings usando as letras da string.
    Stuart tem que formar palavras começando com consoantes.
    Kevin tem que formar palavras começando com vogais.
    O jogo termina quando ambos os jogadores tiverem feito todas as substrings possíveis.
Pontuação
    Um jogador recebe +1 ponto para cada ocorrência da substring na string.
Por exemplo:
    Corda = BANANA
    Palavra inicial de vogal de Kevin = ANA
    Aqui, ANA ocorre duas vezes em BANANA. Portanto, Kevin receberá 2 pontos.
"""


def minion_game(string):
    s = len(string)  # definir o tamanho da string
    vowel, consonant = 0, 0

    for i in range(s):  # realiza o número de vezes da string
        print(i)
            # correr cada letra da string
        print(f'Letra: {string[i]}'.format(string[i]))
        if string[i].upper() in 'AEIOU': # se vogal, ganha kevin o tamanho (s) - posição (i)
            vowel += (s - i)
            print('Vowel: ', vowel, ' pontos.')
        else:
            consonant += (s - i)
            print('Consonant: ', consonant, ' pontos.')

    print('\n\tVencedor:')
    if vowel < consonant:
        print("Consonants " + str(consonant))
    elif vowel > consonant:
        print("Vowels " + str(vowel))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
