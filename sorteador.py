from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

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
        self.iconbitmap(bitmap="@source/icon.xbm")#Ícone do programa
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
        self.iconbitmap(bitmap="@source/icon.xbm")
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
        self.iconbitmap(bitmap="@source/icon.xbm")
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
        self.iconbitmap(bitmap="@source/icon.xbm")
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