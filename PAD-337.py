import random
score = 0
while score < 21:
    cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']
    print('Quer uma carta?(s/n)')
    pergunta = input('')
    if pergunta.lower().strip() == 's':
        carta_retirada = random.choice(cartas)
        print(f'Carta retirada: {carta_retirada}')

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
        print(f'Score: {score}')

    elif pergunta.lower().strip() == 'n':
        print('Você saiu do jogo!')
        break


if score == 21:
    print('Você ganhou!')
elif score > 21:
    print('Você perdeu!')







walloliveira








