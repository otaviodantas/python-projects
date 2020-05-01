lista = [1,2,3,4,5]

#Quando é colocado lista = None isso faz com que uma lista nova vazia não seja atribuida a ela nada antes de colocarem os valores reais

def testeLista(lista = None):
    if lista == None: 
        lista = list()
    
    print(len(lista))
    lista.append(13)


testeLista(lista)
print(lista)