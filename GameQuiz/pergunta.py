import json

class Pergunta:
    enunciado = ""
    altA = ""
    altB = ""
    altC = ""
    altD = ""
    altE = ""
    altCorreta = "" # tá
    #tá boa.

    #recebe os atributos da classe pelo teclado, um a um
    def recebePergunta(){
        contador = 1
        while(true): 
            id = contador
            enunciado = input("Digite o texto do enunciato: ")
            altA = input("Digite a alternativa A: ")
            altB = input("Digite a alternativa B: ")
            altC = input("Digite a alternativa C: ")
            altD = input("Digite a alternativa D: ")
            altE = input("Digite a alternativa E: ")
            altCorreta = input("Digite a alternativa correta: ")
            continuar = input("Adicionar outra Pergunta? (S|N)")
            if(continuar != "S"):
                break 
    }
    
    def montaPergunta()
        dic = 'Enunciato' : enunciato, 'A' : altA, 'B' : altB, 'C' : altC, 'D' : altD, 'E' : altE, 'altCorreta' : altCorreta
        return dic 

dic = {
    "ID" : "001",
    "enuciato": "ausdh",
    "altA": "asoidjoasufhas",
    "altB": "asdsad",
    "altCorreta": "A"
}
    
def lerJson():
    with open('questionarios.json', 'r') as file:
        data = json.load(file)
    return data

def CriaJson(dic):
    json_object = json.dumps(dic, indent = 4)
    with open('questionarios.json', 'w') as file:
        newData = json.load(file)
        newData.append(dic)
        file.seek(0)
        json.dump(newData, file, indent = 4) 

def GeraPergunta():
    return "pergunta"


def GeraQuestionario():
    return "questionario"

CriaJson(dic)
niceDic = lerJson()
print(niceDic)

'''a função de criar o json tem que receber um dicionario 
    
    dic = {
        "enuciato" : "ausdh"
        "altA" : "asoidjoasufhas"
        "altB" : "asdsad"
        "altCorreta" : "A"
    }
    
    tá ligado?
'''

#lerJson()
#print(data)
