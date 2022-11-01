import csv
import matplotlib.pyplot as plt

def leObras(filename):
    file = open(filename, encoding="UTF8")
    file.readline()
    csv_line = csv.reader(file, delimiter = ";")
    
    lista=[]
    for obra in csv_line:
        lista.append(tuple(obra))
    return lista
    
def tamanhoObras(obras):
    return len(obras)

def imprime(obras):
    print(f"| {'nome':20} | {'descrição':25} | {'ano':8} | {'compositor':15} | ")
    for nome, desc, ano, _, comp, *_ in obras:
        print(f"| {nome[:20]:20} | {desc[:25]:25} | {ano:8} | {comp[:15]:15} |")

def ordem(tuplo):
    return tuplo[0] #queremos ordenar pelo primeiro elemento do tuplo, ou seja, pelo titulo

def ordem2(tuplo):
    return tuplo[2] #ordenando por ano

def titAno(obras):
    lista = []
    for nome, _, ano, *_ in obras:
        lista.append((nome, ano))
    lista.sort(key = ordem)
    return lista

def titAno2(obras): #outra forma de fazer podemos cagar nisto é só para ordenar de outra forma
    lista = []
    for nome, _, ano, *_ in obras:
        lista.append((nome, ano))

    lista.sort(key = lambda tuplo: tuplo[1])
    return lista

def titAno3(obras):
    dici = {}
    for nome, _, ano, *_ in obras:
        if ano in dici.keys():
            dici[ano].append(nome)
        else: 
            dici[ano] = [nome]
    return dici

def distPeriodo(obras):
    dici = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in dici.keys():
            dici[periodo] = dici[periodo] + 1
        else: 
            dici[periodo] = 1

    x = list(dici)
    y = list(dici.values())
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("distribuições por periodo")
    plt.show()
    print(x)
    print(y)



def distAno(obras):
    dici = {}
    for _, _, ano,*_ in obras:
        if ano in dici.keys():
            dici[ano] = dici[ano] + 1
        else: 
            dici[ano] = 1

    x = list(dici)
    y = list(dici.values())
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("distribuições por ano")
    plt.show()
    print(x)
    print(y)

def distComp(obras):
    dici = {}
    for _, _, _, _, compositor,*_ in obras:
        if compositor in dici.keys():
            dici[compositor] = dici[compositor] + 1
        else: 
            dici[compositor] = 1
    
        x = list(dici)
    y = list(dici.values())
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("distribuições por periodo")
    plt.show()
    print(x)
    print(y)

def listaObrasporComp(obras):
    dici = {}
    for nome, _, _, _, compositor,*_ in obras:
        if compositor in dici.keys():
            dici[compositor].append(nome)
        else:
            dici[compositor] = [nome]
        
    for compositor in dici:
        print({f"{compositor} -:::::- {dici[compositor]}"})


