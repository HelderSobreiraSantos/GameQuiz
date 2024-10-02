import json

def recebePergunta(): 
    enunciado = input("Digite o texto do enunciato: ")
    altA = input("Digite a alternativa A: ")
    altB = input("Digite a alternativa B: ")
    altC = input("Digite a alternativa C: ")
    altD = input("Digite a alternativa D: ")
    altE = input("Digite a alternativa E: ")
    altCorreta = input("Digite a alternativa correta: ")
    return montaPergunta(enunciado, altA, altB, altC, altD, altE, altCorreta)

def montaPergunta(enunciado, altA, altB, altC, altD, altE, altCorreta):
    dic = {'Enunciato' : enunciado, 'A' : altA, 'B' : altB, 'C' : altC, 'D' : altD, 'E' : altE, 'altCorreta' : altCorreta}
    return dic  

def montaQuestionario():
    dic = {'nome' : '', 'perguntas' : []}
    dic['nome'] = input("Digite o nome do questionário: ")
    while (True):
        resposta = input("Deseja cadastrar uma nova pergunta?")
        if resposta == "sim" or resposta == "SIM" or resposta == "Sim" or resposta == "s":
            dic['perguntas'].append(recebePergunta())
        else:
            break
    print(dic)
    CriaJson(dic)
    return "FIM"

def CriaJson(dic):
    # Tente ler o arquivo existente
    try:
        with open('questionarios.json', 'r') as file:
            newData = json.load(file)
    # Se o arquivo não existir, inicie uma nova lista
    except FileNotFoundError:
        newData = []  
    # Adicione o novo questionário
    newData.append(dic)  
    # Escreva de volta no arquivo
    with open('questionarios.json', 'w') as file:
        json.dump(newData, file, indent=4)

# def CriaJson(dic):
#     json_object = json.dumps(dic, indent = 4)
#     with open('questionarios.json', 'w') as file:
#         newData = json.load(file)
#         newData.append(dic)
#         file.seek(0)
#         json.dump(newData, file, indent = 4) 

def lerJson():
    with open('questionarios.json', 'r') as file:
        data = json.load(file)
    return data

montaQuestionario()

#def GeraPergunta():
#    return "pergunta"


#def GeraQuestionario():
#    return "questionario"

#CriaJson(dic)
#niceDic = lerJson()
#print(niceDic)


#lerJson()
#print(data)
