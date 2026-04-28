"""
Zumbi Normal: Nenhum atributo especial

Zumbi Cabeça-de-Cone: 4 a mais de vida

Zumbi do Jornal: Fica mais rápido depois de perder o jornal (com metade da vida, de 2 para 3 de velocidade)

Zumbi Saltador: Capaz de atravessar a Noz-Obstáculo
"""
##função para compra das plantas e uma para a batalha

#função para compra das plantas
def compra_fun(nome_planta, s):

    if nome_planta == "Disparervilha" and s >= 50:
        s -= 50
        list_combate.append(nome_planta)

    elif nome_planta == "Gelervilha" and s >= 100:
        s -= 100
        list_combate.append(nome_planta)

    elif nome_planta == "Noz_Obstáculo" and s >= 75:
        s -= 75
        list_combate.append(nome_planta)

    else:
        print("Você não tem sóis suficientes para isso!")

    return s


print("O quintal está sendo invadido! Prepare a melhor linha de defesa possível!")
list_combate = []

#total de sóis disponíveis para o jogador
qtd_sois = int(input())

nome_planta = ""

while nome_planta != "FIM":
    nome_planta = input()

    if nome_planta != "FIM":
        qtd_sois = compra_fun(nome_planta, qtd_sois)

    
