# lista_original = [2, 3, 4, 5, 6, 7]
# pares = [elemento for elemento in lista_original if elemento % 2 == 0]
# print(pares)


def gerar_dicionario_quadrados(n):
    dicionario_quadrados = {x : x**2 for x in range(1, n + 1)}
    
    return dicionario_quadrados

def imprimir_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(f'({chave}, {valor})')

n = int(input("Digite um valor para n: "))