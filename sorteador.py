from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from random import choice, randint
from openpyxl import load_workbook
from platform import system

os = system()

class Competidor():
    nome = ""
    equipe = ""
    mudouEqp = False

    def __str__(self):
        return ("----------------\ncompetidor %s\nequipe %s\n----------------\n" % (self.nome, self.equipe))
    def __repr__(self):
        return ("\ncompetidor %s\nequipe %s\n" % (self.nome, self.equipe))

class JanelaSel(Tk):#Utilizei a biblioteca tkinter
    def __init__(self):
        super().__init__()
        os = system()
        if os == 'Linux':
            self.iconbitmap(bitmap="@source/icon.xbm")#Ícone do programa
        else:
            self.iconbitmap(bitmap="source/icon.ico")
        self.geometry("250x150")
        self.title("Sorteador de Chaves")

        self.framePrincipal = Frame(self)

        self.frameEquipe = Frame(self.framePrincipal)
        Label(self.frameEquipe, text="Número de Equipes:").pack(anchor=W)
        self.entNEquipe = Entry(self.frameEquipe)
        self.entNEquipe.pack(anchor=E)
        self.frameEquipe.pack()

        self.frameComp = Frame(self.framePrincipal)
        Label(self.frameComp, text="Número de Competidores:").pack(anchor=W)
        self.entNComp = Entry(self.frameComp)
        self.entNComp.pack(anchor=E)
        self.frameComp.pack()

        self.btEnv = Button(self.framePrincipal, text="Continuar", command=self.enviarDados).pack()

        self.framePrincipal.pack()

        self.nComp = 0
        self.nEquipe = 0

    def enviarDados(self):
        try:
            int(self.entNComp.get())
            int(self.entNEquipe.get())
        except ValueError:
            showwarning("Aviso", "Digite um valor válido!")
            return
        self.nEquipe = int(self.entNEquipe.get())
        self.nComp = int(self.entNComp.get())
        self.destroy()

class JanelaEquipe (Tk):
    def __init__(self):
        super().__init__()
        if os == 'Linux':
            self.iconbitmap(bitmap="@source/icon.xbm")#Ícone do programa
        else:
            self.iconbitmap(bitmap="source/icon.ico")
        self.geometry("250x150")
        self.title("Sorteador de Chaves")

        self.framePrincipal = Frame(self)

        Label(self.framePrincipal, text="Nome da Equipe:").pack(anchor=W)
        self.nomeEquipe = Entry(self.framePrincipal)
        self.nomeEquipe.pack()

        self.btEnv = Button(self.framePrincipal, text="Próxima", command=self.enviarDados).pack()

        self.framePrincipal.pack()

        self.equipes = []

        self.loop = False
        self.loopCount = 0
        self.loopMax = 0


    def enviarDados(self):
        if self.nomeEquipe.get() in self.equipes:
            showwarning("Aviso", "Equipe já registrada!")
            return
        elif self.nomeEquipe.get() == "":
            showerror("Erro", "Digite o nome da equipe!")
        else:
            self.equipes.append(self.nomeEquipe.get())
            self.nomeEquipe.delete(0, 1000)
            if self.loop:
                self.loopCount += 1
                if self.loopCount == self.loopMax:
                    self.destroy()
            return

    def setContador(self, n):
        self.loop = True
        self.loopMax = n
        return


class JanelaComp (Tk):

    def __init__(self, equipes):
        super().__init__()
        if os == 'Linux':
            self.iconbitmap(bitmap="@source/icon.xbm")#Ícone do programa
        else:
            self.iconbitmap(bitmap="source/icon.ico")
        self.geometry("250x150")
        self.title("Sorteador de Chaves")

        self.framePrincipal = Frame(self)

        Label(self.framePrincipal, text="Nome do Competidor:").pack(anchor=W)
        self.nomeComp = Entry(self.framePrincipal)
        self.nomeComp.pack()

        Label(self.framePrincipal, text="Selecione a equipe do competidor:").pack()
        self.selEquipe = Combobox(self.framePrincipal)
        self.selEquipe.bind("<<ComboboxSelected>>")
        self.selEquipe['values'] = equipes
        self.selEquipe.current(0)
        self.selEquipe.pack()

        self.btEnv = Button(self.framePrincipal, text="Próximo", command=self.enviarDados).pack()

        self.framePrincipal.pack()

        self.competidores = []

        self.loop = False
        self.loopCount = 0
        self.loopMax = 0

    def enviarDados(self):
        novo = Competidor()
        novo.nome = self.nomeComp.get()
        novo.equipe = self.selEquipe.get()
        if novo in self.competidores:
            showwarning("Aviso", "Competidor já registrado!")
            return False
        elif novo.nome == "":
            showwarning("Aviso", "Digite um nome válido!")
            return False
        else:
            self.competidores.append(novo)
            self.nomeComp.delete(0, 1000)
            self.selEquipe.current(0)
            if self.loop:
                self.loopCount += 1
                if self.loopCount == self.loopMax:
                    self.destroy()
                    return True
            return True

    def setContador(self, n):
        self.loop = True
        self.loopMax = n
        return


class JanelaDetalhes (Tk):
    def __init__(self):
        super().__init__()
        if os == 'Linux':
            self.iconbitmap(bitmap="@source/icon.xbm")#Ícone do programa
        else:
            self.iconbitmap(bitmap="source/icon.ico")
        self.geometry("250x250")
        self.title("Sorteador de Chaves")

        self.framePrincipal = Frame(self)

        Label(self.framePrincipal, text="Torneio:").pack(anchor=W)
        self.torneio = Entry(self.framePrincipal)
        self.torneio.pack()
        self.torneioGet = ""

        Label(self.framePrincipal, text="Categoria:").pack(anchor=W)
        self.categoria = Entry(self.framePrincipal)
        self.categoria.pack()
        self.categoriaGet = ""

        Label(self.framePrincipal, text="Peso:").pack(anchor=W)
        self.peso = Entry(self.framePrincipal)
        self.peso.pack()
        self.pesoGet = ""

        Label(self.framePrincipal, text="Faixa:").pack(anchor=W)
        self.faixa = Entry(self.framePrincipal)
        self.faixa.pack()
        self.faixaGet = ""

        Label(self.framePrincipal, text="Sexo:").pack(anchor=W)
        self.sexo = Entry(self.framePrincipal)
        self.sexo.pack()
        self.sexoGet = ""

        self.btEnv = Button(self.framePrincipal, text="Gerar Planilha", command=self.enviarDados).pack()

        self.framePrincipal.pack()


    def enviarDados(self):
        if self.torneio.get() == "":
            showwarning("Aviso", "Digite o nome do torneio!")
            return False
        elif self.categoria.get() == "":
            showwarning("Aviso", "Digite a categoria!")
            return False
        elif self.peso.get() == "":
            showwarning("Aviso", "Digite o peso!")
            return False
        elif self.faixa.get() == "":
            showwarning("Aviso", "Digite a faixa!")
            return False
        elif self.sexo.get() == "":
            showwarning("Aviso", "Digite o sexo!")
            return False
        else:
            self.torneioGet = self.torneio.get()
            self.categoriaGet = self.categoria.get()
            self.pesoGet = self.peso.get()
            self.faixaGet = self.faixa.get()
            self.sexoGet = self.sexo.get()
            self.destroy()
            return True

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

