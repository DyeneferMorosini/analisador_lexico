import json
data = [[
'Palavras reservadas: while, do'],['Operadores: i, j'],['constantes: sequencia de numeros (um ou mais numeros)'],
['numeros: 0,1,2,3,4,5,6,7,8,9'],['identificadores: i, j'],['terminador: ;']]
with open('no.txt', 'w') as txtfile:
    json.dump(data, txtfile)

'*******'

class AnalisadorLexico():
    
    def ehPalavraReservada (self, lista):
        palavra = ['while', 'do']
        list = []
        posicao=[]
        for i in range(len(lista)):
            if lista[i] in palavra:
                list.append(lista[i])
                list.append(len(lista[i]))
                t = (' '.join(lista))

                if not t.index(lista[i]) in posicao:
                    posicao.append(t.index(lista[i]))
                    list.append(t.index(lista[i]))
                    lista[i]=len(lista[i])*'#'

                else:
                    print('Simbolo nao pertencente ao conjunto de simbolos da linguagem')
        return ('Palavras reservadas', list)
    
    def ehOperador(self, entrada):
        list=[]
        posicao=[]
        operadores = ['<', '=', '+']
        for i in range(len(entrada)):
            if entrada[i] in operadores:
                list.append(entrada[i])
                list.append(len(entrada[i]))
                t = (' '.join(entrada))

                if not t.index(entrada[i]) in posicao:
                    posicao.append(t.index(entrada[i]))
                    list.append(t.index(entrada[i]))
                    entrada[i]=len(entrada[i])*'#'
            
        return ('Operadores',list)

    def ehTerminador(self, entrada):
        terminador = [";"]
        lista=[]
        posicao=[]
        stringNormal = (' '.join(entrada))
        t = list(stringNormal)
        if t[-1] == ';':
            lista.append(t[-1])
            lista.append(len(t[-1]))
            #lista.append(t[-1].index)  #falta trazer o indíce na impressao
        
        return ('Terminador',lista)
    
    def ehIdentificador(self, entrada):
        identificadores = ['i', 'j']
        posicao=[]
        list=[]
        for i in range(len(entrada)):
            if entrada[i] in identificadores:
                list.append(entrada[i])
                list.append(len(entrada[i]))
                t = (' '.join(entrada))

                if not t.index(entrada[i]) in posicao:
                    posicao.append(t.index(entrada[i]))
                    list.append(t.index(entrada[i]))
                    entrada[i]=len(entrada[i])*'#'

        return ('identificadores',list)

    # Metodo que verifica se a entrada eh um numero
    def ehNumero(self, entrada):
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        list=[]
        posicao=[]
        for i in range(len(entrada)):
            
            if entrada[i] in numeros:
                list.append(entrada[i])
                list.append(len(entrada[i]))
                t = (' '.join(entrada))

                if not t.index(entrada[i]) in posicao:
                    posicao.append(t.index(entrada[i]))
                    list.append(t.index(entrada[i]))
                    entrada[i]=len(entrada[i])*'#'
        return ('Numero',list)
    
    def ehSequencia(self, entrada):
        list=[]
        posicao=[]
        for i in range(len(entrada)):
            if entrada[i].isnumeric():
                list.append(entrada[i])
                list.append(len(entrada[i]))
                t = (' '.join(entrada))

                if not t.index(entrada[i]) in posicao:
                    posicao.append(t.index(entrada[i]))
                    list.append(t.index(entrada[i]))
                    entrada[i]=len(entrada[i])*'#'

        return ('Sequência numérica',list)

    def executar(self, entrada):

        listaGeral=[]
        lista = entrada.split(' ')
        listaGeral.append(self.ehPalavraReservada(lista))
        listaGeral.append(self.ehNumero(lista))
        listaGeral.append(self.ehOperador(lista))
        listaGeral.append(self.ehIdentificador(lista))
        listaGeral.append(self.ehTerminador(lista))
        listaGeral.append(self.ehSequencia(lista))

        for i in range(len(listaGeral)):
            print(listaGeral[i])

