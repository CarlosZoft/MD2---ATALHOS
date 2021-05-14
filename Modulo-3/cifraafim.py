#padrao
alfabeto  = 26
#conversao = {"A":"0", "B":"1", "C":"2", "D":"3", "E":"4","F":"5", "G":"6", "H":"7", "I":"8", "J":"9", "K":"10", "L":"11", "M":"12", "N":"13", "O":"14", "P":"15", "Q":"16", "R":"17", "S":"18", "T":"19", "U":"20", "V":"21", "W":"22", "X":"23", "Y":"24", "Z":"25"}
#numeroletra = {"0":"A", "1":"B", "2":"C", "3":"D", "4":"E","5":"F", "6":"G", "7":"H", "8":"I", "9":"J", "10":"K", "11":"L", "12":"M", "13":"N", "14":"O", "15":"P", "16":"Q", "17":"R", "18":"S", "19":"T", "20":"U", "21":"V", "22":"W", "23":"X", "24":"Y", "25":"Z"}

conversao = {"H":"0", "A":"1", "P":"2", "Q":"3", "D":"4","E":"5", "G":"6", "R":"7", "F":"8", "O":"9", "S":"10", "T":"11", "U":"12", "I":"13", "V":"14", "W":"15", "B":"16", "C":"17", "X":"18", "J":"19", "Z":"20", "K":"21", "L":"22", "M":"23", "N":"24", "Y":"25"}
numeroletra = {"0":"H", "1":"A", "2":"P", "3":"Q", "4":"D","5":"E", "6":"G", "7":"R", "8":"F", "9":"O", "10":"S", "11":"T", "12":"U", "13":"I", "14":"V", "15":"W", "16":"B", "17":"C", "18":"X", "19":"J", "20":"Z", "21":"K", "22":"L", "23":"M", "24":"N", "25":"Y"}

def cifra(num, x, y):
    cifrado = x * num + y % alfabeto
    return str(cifrado % 26)



def letraemnumero(letra):
    return conversao[letra]

def nummeroemletra(numero):
    return numeroletra[numero]

def menormpositivo(a, b, mod):
    m = 0
    while(True):
        if (a * m % mod) == (b % mod):
            return m
        else:
            m = m + 1
        

def main():
    escolha = input("Cifrar - 1\nDecifrar - 2\n")

    if escolha == '1':
        mensagem = input("Entre com a mensagem:\n")
        mensagem = mensagem.upper()
        
        X = int(input("X = "))
        Y = int(input("Y = "))

        letra = {}

        index = 0
        for i in mensagem:
            num = cifra(int(letraemnumero(i)), X, Y)
            letra[index] = nummeroemletra(num)
            print(letra[index], end='')
            index = index + 1

    if escolha == '2':
        mensagem = input("Entre com a mensagem:\n")
        mensagem = mensagem.upper()

        X = int(input("X = "))
        Y = int(input("Y = "))

        for i in mensagem:
            num = str(menormpositivo(X, int(letraemnumero(i)) - Y, alfabeto))
            letra = nummeroemletra(num)
            print(letra, end='')


main()