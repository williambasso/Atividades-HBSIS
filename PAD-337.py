import random
score = 0
while score < 21:
    cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']
    print('\033[1;32mQuer uma carta?\033[1;33m(s/n)\033[m')
    pergunta = input('')
    if pergunta.lower().strip() == 's':
        carta_retirada = random.choice(cartas)
        print(f'\033[1;36mCarta retirada: {carta_retirada}\033[m')

        try:
            valor_carta = int(carta_retirada)
        except:
            if carta_retirada == 'A' and score == 0:
                valor_carta = 11
            elif carta_retirada == 'A' and score != 0:
                valor_carta = 1
            else:
                valor_carta = 10

        score += valor_carta
        print(f'\033[1;34mScore: {score}\033[m')

    elif pergunta.lower().strip() == 'n':
        print('\033[4;31mVocê saiu do jogo!\033[m')
        break


if score == 21:
    print('\033[1;35mVocê ganhou!\033[m')
elif score > 21:
    print('\033[1;31mVocê perdeu!\033[m')
















