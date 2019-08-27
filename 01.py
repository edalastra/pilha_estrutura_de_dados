t = -1
b = -1
tam = 4
pilha = ['','','','','']

def mostra():
    print('\n_________________')
    for i in range(4,-1,-1):
        print(pilha[i])
        print('_________________')
        

def inclusao(valor):
    global t
    if(t == tam):
        print("Overflow ocorrido")
    else:
        t+=1
        pilha[t] = valor
        print('{} foi incluso'.format(valor))
        mostra()
    
def retirada():
    valor = ""
    global t
    if(t == b):
        print('Underflow ocorrido')
    else:
        pilha[t] = ""
        valor = pilha[t]
        t-=1
        print('{} retirado da pilha'.format(valor))
        mostra()



while(True):
    opc = input('Deseja inserir ou retirar um valor (i ou r): ').upper()
    if(opc == 'I'):
        valor = input('Digite o valor: ')
        inclusao(valor)
    elif(opc == 'R'):
        retirada()
    else:
        print('Opção inválida')