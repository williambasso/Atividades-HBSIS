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
        letra = input('Digite uma letra: ').lower()
        return letra

    def qtd_letras_frutas(self, fruta_sorteada, letra_digitada):
        qtd_letra_fruta = fruta_sorteada.count(letra_digitada)
        return qtd_letra_fruta

    def len_da_fruta(self, fruta_sorteada):
        tamanho_fruta = len(fruta_sorteada)
        return tamanho_fruta

    def verificar_se_existe_letra_em_fruta(self, letra, fruta, quantidade, acertos: list):
        if not letra in acertos:
            if letra in fruta:
                acertos.append(letra)
                return f'A letra \033[1;32m{letra}\033[m existe nesta fruta e o número de vezes que apareceu foi {quantidade}'
            elif letra not in fruta:
                return f'A letra \033[1;32m{letra}\033[m não existe nesta fruta!'
        return f'Está letra já foi digitada!'

    def tentativa_de_acerto(self, acertos: list, fruta):
        if len(acertos) >= 3:
            tentativa = input('Digite a resposta! ')
            if tentativa == fruta:
                print("Parabéns ")
                return True
            elif tentativa != fruta:
                print("Tente novamente! ")
                return False

    def posicao_da_letra(self,letra,fruta):
        posicoes = {letra:[]}
        for i in range(0,len(fruta)):
            if letra == fruta[i]:
                posicoes[letra].append(i+1)
        #FALTA RETORNAR AS POSIÇÕES






