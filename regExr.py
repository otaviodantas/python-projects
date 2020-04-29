import re

padrao = "e[0-9]{1,2} [s,t][0-9]{1,2}"
conversa1 = "Estou no e 1 t 3 de Naruto"
conversa2 = "O e02 t2 é o melhor de Rick and Morty"
conversa3 = "Eu parei GOT no e2 s3"
conversa4 = "Não gostei do ep4 t5 de Vikings"
conversa5 = "O melhor episódio de Boku no Hero é o e011 s02"

retorno = re.findall(padrao,conversa3)
print(retorno)