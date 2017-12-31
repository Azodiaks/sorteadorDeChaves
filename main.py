import sorteador
from random import choice, randint
from openpyxl import load_workbook

#TODO fazer o algoritmo do resto das chaves, por enquanto o programa só funciona com 3 e 4 competidores
def criar_xlsx(torneio, categoria, peso, faixa, sexo, n_competidores, chave):#Função que gera a planilha
    if n_competidores == 3 or n_competidores == 4:
        c3_4 = [["A8", "A14"], ["A18", "A24"], ["A14"]] #Posição das células dos competidores na chave de 3 ou 4
        xlsx_template = load_workbook(filename="source/3_4.xlsx")#Abre a planilha na pasta source
        active = xlsx_template.active#Active permite alterar o valor das células na planilha
        for i in range(len(chave)):#Itera sobre a lista de competidores
            for j in range(len(chave[i])):
                active[c3_4[i][j]] = chave[i][j].nome#Aqui se altera para o valor do nome do competidor
                equipe = list(c3_4[i][j])
                if len(equipe) == 2:#Esses if e else somam na posição da célula para alterar a equipe
                    equipe[1] = str(int(equipe[1]) + 1)
                else:
                    if equipe[2] == "9":
                        equipe[2] = "0"
                        equipe[1] = str(int(equipe[1]) + 1)
                    else:
                        equipe[2] = str(int(equipe[2]) + 1)
                equipe = "".join(equipe)#Retornando o valor de lista para string
                active[str(equipe)] = chave[i][j].equipe#Alterando o valor da célula com a equipe do competidor
    active["A1"] = torneio
    active["J1"] = categoria
    active["B2"] = peso
    active["G2"] = faixa
    active["L2"] = sexo
    nomeArq = "chaves/" + torneio + "-" + categoria + "-" + peso + "-" + faixa + "-" + sexo + ".xlsx"#Nome do arquivo criado
    xlsx_template.save(nomeArq)
    return True

def is_potencia2(n):
    if n in {2, 4, 8, 16, 32, 64}:
        return True
    else:
        return False

def potencia2_maior(n):
    for i in range(n, n*2):
        print(i)
        if is_potencia2(i):
            return i


def sortear_chaves(n_competidores, vet_competidores):
    lado1 = []# Esses vetores lado são para organizar os competidores o lado 3 será usado se o numero de competidor não for uma potencia de 2
    lado2 = []
    lado3 = []
    if is_potencia2(n_competidores):
        for i in range(n_competidores):
            escolhido = choice(vet_competidores)#Escolha aleatoria dos competidores
            while escolhido in lado1 or escolhido in lado2:
                escolhido = choice(vet_competidores)
            if randint(0, 1) == 0:
                if len(lado1) < n_competidores/2:
                    lado1.append(escolhido)
                else:
                    lado2.append(escolhido)
            else:
                if len(lado2) < n_competidores/2:
                    lado2.append(escolhido)
                else:
                    lado1.append(escolhido)
        return [lado1, lado2]
    else:
        tam_lado3 = 0
        if n_competidores % 2 != 0:#Esse algoritmo abaixo tirei de um material de um professor de educação fisica
            tam_lado12 = n_competidores - 1
            tam_lado3 += 1
        else:
            tam_lado12 = 0
        if(not is_potencia2(tam_lado12)):
            tam_lado3 += potencia2_maior(tam_lado12) - tam_lado12
            tam_lado12 = n_competidores - tam_lado3
        for i in range(n_competidores):
            escolhido = choice(vet_competidores)
            while escolhido in lado1 or escolhido in lado2 or escolhido in lado3:
                escolhido = choice(vet_competidores)
            intsel = randint(0, 2)
            if intsel == 0:
                if len(lado1) < tam_lado12/2:
                    lado1.append(escolhido)
                elif len(lado2) < tam_lado12/2:
                    lado2.append(escolhido)
                else:
                    lado3.append(escolhido)
            elif intsel == 1:
                if len(lado2) < tam_lado12/2:
                    lado2.append(escolhido)
                elif len(lado1) < tam_lado12/2:
                    lado1.append(escolhido)
                else:
                    lado3.append(escolhido)
            else:
                if len(lado3) < tam_lado3:
                    lado3.append(escolhido)
                elif len(lado1) < tam_lado12/2:
                    lado1.append(escolhido)
                else:
                    lado2.append(escolhido)
        return [lado1, lado2, lado3]



def ver_equipes(vet_equipes, vet_competidores):#Essa função verifica se o numero de competidores por equipe não é maior que 2, se for acrescenta uma letra
    for equipe in vet_equipes:
        contador = 0
        for lado in vet_competidores:
            for competidor in lado:
                if competidor.equipe == equipe:
                    contador += 1
        if contador > 2:
            if contador % 2 == 1:
                for i in range(contador//2):
                    if i < contador//2:
                        for j in range(2):
                            esc = choice(vet_competidores)
                            esc = choice(esc)
                            while esc.mudouEqp and esc.equipe != equipe:
                                esc = choice(vet_competidores)
                                esc = choice(esc)
                            esc.mudouEqp = True
                            esc.equipe += " " + chr(ord('B') + i)
                    else:
                        esc = choice(vet_competidores)
                        esc = choice(esc)
                        while esc.mudouEqp and esc.equipe != equipe:
                            esc = choice(vet_competidores)
                            esc = choice(esc)
                        esc.mudouEqp = True
                        esc.equipe += " " + chr(ord('B') + i)
            else:
                for i in range(contador//2 - 1):
                    for j in range(2):
                        esc = choice(vet_competidores)
                        esc = choice(esc)
                        while esc.mudouEqp and esc.equipe != equipe:
                            esc = choice(vet_competidores)
                            esc = choice(esc)
                        esc.mudouEqp = True
                        esc.equipe += " " + chr(ord('B') + i)
    return vet_competidores


janSel = sorteador.JanelaSel()
janSel.mainloop()

janEqp = sorteador.JanelaEquipe()
janEqp.setContador(janSel.nEquipe)
janEqp.mainloop()

janComp = sorteador.JanelaComp(janEqp.equipes)
janComp.setContador(janSel.nComp)
janComp.mainloop()

janDet = sorteador.JanelaDetalhes()
janDet.mainloop()

chave = sortear_chaves(janSel.nComp, janComp.competidores)
chave = ver_equipes(janEqp.equipes, chave)

criar_xlsx(janDet.torneioGet, janDet.categoriaGet, janDet.pesoGet, janDet.faixaGet, janDet.sexoGet, janSel.nComp, chave)
