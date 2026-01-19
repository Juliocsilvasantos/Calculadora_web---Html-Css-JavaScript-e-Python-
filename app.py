from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def multiplicacao(x, y):
    """Multiplica dois números."""
    return x * y

def divisao(x, y):
    """Divide dois números."""
    if y == 0:
        return "Erro: Divisão por zero não é permitida!"
    return x / y

def subtracao(x, y):
    """Subtrai dois números."""
    return x - y

def adicao(x, y):
    """Soma dois números."""
    return x + y

def obter_numero(mensagem):
    """Solicita e valida a entrada de um número."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido!")

def obter_operacao():
    """Solicita e valida a escolha da operação."""
    while True:
        try:
            print("\n=== CALCULADORA ===")
            print("1 - Adição")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("0 - Sair")
            
            operacao = int(input("\nEscolha a operação desejada: "))
            
            if operacao in [0, 1, 2, 3, 4]:
                return operacao
            else:
                print("Erro: Escolha uma opção válida (0-4)!")
        except ValueError:
            print("Erro: Digite apenas números!")

def calculadora():
    """Função principal da calculadora."""
    print("Olá! Bem-vindo à Calculadora Profissional!\n")
    
    while True:
        operacao = obter_operacao()
        
        if operacao == 0:
            print("\nObrigado por usar a calculadora. Até logo!")
            break
        
        n1 = obter_numero("Digite o PRIMEIRO valor: ")
        n2 = obter_numero("Digite o SEGUNDO valor: ")
        
        operacoes = {
            1: (adicao, "Adição"),
            2: (subtracao, "Subtração"),
            3: (multiplicacao, "Multiplicação"),
            4: (divisao, "Divisão")
        }
        
        funcao, nome = operacoes[operacao]
        resultado = funcao(n1, n2)
        
        print(f"\n{'='*40}")
        print(f"{nome} de {n1} e {n2}: {resultado}")
        print(f"{'='*40}\n")

# Executa apenas se for o arquivo principal
if __name__ == "__main__":
    calculadora()