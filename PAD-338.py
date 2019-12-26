from classes.frutas_class import Fruta
acertos = []
f = Fruta()
fruta_sorteio = f.sortear_fruta()
print(fruta_sorteio)
menu = int(input('Digite 1 para continuar ou 2 para sair!'))
while menu != 2:
    if f.tentativa_de_acerto(acertos,fruta_sorteio):
        break
    letra = f.letra_digitada()
    letras_na_fruta = f.qtd_letras_frutas(fruta_sorteio,letra)
    verificacao = f.verificar_se_existe_letra_em_fruta(letra,fruta_sorteio,letras_na_fruta,acertos)
    print(verificacao)
    posicoes = f.posicao_da_letra(letra,fruta_sorteio)






