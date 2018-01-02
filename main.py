from sorteador import *

janSel = JanelaSel()
janSel.mainloop()

janEqp = JanelaEquipe()
janEqp.setContador(janSel.nEquipe)
janEqp.mainloop()

janComp = JanelaComp(janEqp.equipes)
janComp.setContador(janSel.nComp)
janComp.mainloop()

janDet = JanelaDetalhes()
janDet.mainloop()

chave = sortear_chaves(janSel.nComp, janComp.competidores)
chave = ver_equipes(janEqp.equipes, chave)

criar_xlsx(janDet.torneioGet, janDet.categoriaGet, janDet.pesoGet, janDet.faixaGet, janDet.sexoGet, janSel.nComp, chave)
