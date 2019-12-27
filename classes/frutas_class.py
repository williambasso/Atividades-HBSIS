import random


class Fruta:
    frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']

    def __int__(self):
        pass

    def sortear_fruta(self):
        print('O jogo sorteou uma fruta! Tente adivinhar qual é:')
        fruta_sorteada = random.choice(self.frutas)
        return fruta_sorteada

    def letra_digitada(self):
        while True:
            letra_digitada = input('Digite uma letra:').lower()
            is_numeric = letra_digitada.isnumeric()
            if is_numeric:
                print('Valor inválido')
            elif len(letra_digitada) == 1 and letra_digitada.isalpha():
                return letra_digitada


    def qtd_letras_frutas(self, fruta_sorteada, letra_digitada):
        qtd_letra_fruta = fruta_sorteada.count(letra_digitada)
        return qtd_letra_fruta

    def len_da_fruta(self, fruta_sorteada):
        tamanho_fruta = len(fruta_sorteada)
        return tamanho_fruta

    def verificar_se_existe_letra_em_fruta(self, letra_digitada, fruta_sorteada, qtd_letras_digitada_dentro_fruta, qtd_acertos: list):
        if not letra_digitada in qtd_acertos:
            if letra_digitada in fruta_sorteada:
                qtd_acertos.append(letra_digitada)
                return f'Existe \033[1;32m{qtd_letras_digitada_dentro_fruta}\033[m letra(s) \033[1;32m{letra_digitada}\033[m na fruta sorteada! '
            elif letra_digitada not in fruta_sorteada:
                return f'A letra \033[1;32m{letra_digitada}\033[m não existe nesta fruta!\n'



        return f'Está letra já foi digitada!'

    def tentativa_de_acerto(self, qtd_acertos: list, fruta_sorteada):
        if len(qtd_acertos) >= 3:
            tentativa = input('Digite a resposta! ')
            if tentativa == fruta_sorteada:
                print("Parabéns ")
                return True
            elif tentativa != fruta_sorteada:
                print("Tente novamente! ")
                return False

    def posicao_da_letra(self,letra_digitada,fruta_sorteada):
        if letra_digitada in fruta_sorteada:
            posicoes = {letra_digitada:[]}
            for i in range(0,len(fruta_sorteada)):
                if letra_digitada == fruta_sorteada[i]:
                    posicoes[letra_digitada].append(i+1)
            print(f'A letra \033[1;32m{letra_digitada}\033[m se encontra na posição: ')
            for a in posicoes[letra_digitada]:
                print(a, end='° posição ')
            print()











