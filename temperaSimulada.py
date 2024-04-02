import numpy as np
import random
import math
import matplotlib.pyplot as plt
from distanceMatrix import distancias  
import time

# Função para calcular o custo total de um caminho específico
def calcular_custo(caminho):
    # A soma das distâncias entre pontos consecutivos no caminho, mais a distância do último ponto de volta ao primeiro
    return sum(distancias[caminho[i-1]][caminho[i]] for i in range(1, len(caminho))) + distancias[caminho[-1]][caminho[0]]


def tempera_simulada(T, T_min, resfriamento):
    # Começa com um caminho inicial e um custo inicial
    caminho_atual = list(range(len(distancias)))
    custo_atual = calcular_custo(caminho_atual)

    # Loop principal do algoritmo de resfriamento simulado
    while T > T_min:
        # Gera um novo caminho por inversão de uma subseção do caminho atual
        i, j = sorted(random.sample(range(1, len(distancias)), 2))
        novo_caminho = caminho_atual[:i] + caminho_atual[j:i-1:-1] + caminho_atual[j+1:]
        novo_custo = calcular_custo(novo_caminho)

        # Se o novo caminho tem um custo menor, ele é aceito
        # Se o novo caminho tem um custo maior, ele pode ainda ser aceito com uma probabilidade que diminui com a diferença de custo e a "temperatura" atual
        if novo_custo < custo_atual or random.random() < math.exp((custo_atual - novo_custo) / T):
            caminho_atual, custo_atual = novo_caminho, novo_custo

        # A temperatura é gradualmente resfriada
        T *= resfriamento

    # Retorna o melhor caminho encontrado e seu custo
    return caminho_atual, custo_atual

# Inicializa o melhor caminho e o menor custo como nulos e infinito, respectivamente

def main():
    inicio = time.time()
    melhor_caminho, menor_custo = None, float('inf')
    custos = []
    T = 12
    T_min = 0.01
    resfriamento = 0.9

    repeticoes = 10000
    for i in range(repeticoes):
    # Cada vez que um caminho com um custo menor é encontrado, ele é salvo como o melhor caminho até agora
        caminho, custo = tempera_simulada(T, T_min, resfriamento)
        if custo < menor_custo:
            melhor_caminho, menor_custo = caminho, custo
    # O custo do melhor caminho é registrado após cada execução
        custos.append(menor_custo)

# Imprime o melhor caminho encontrado e seu custo
    melhor_caminho.append(melhor_caminho[0])
    fim = time.time()
    tempo_total = fim - inicio
    tempo_ap = "{:.2f}".format(tempo_total)
    print(f'O melhor caminho encontrado é {melhor_caminho} com um custo total de {menor_custo}')

# Plota o menor custo encontrado após cada execução do algoritmo de Tempera Simulada
    plt.plot(custos)
    plt.suptitle(f'Melhor Distância por Geração do TS com resfriamento={resfriamento}')
    plt.title(f'Melhor Distância encontrada = {menor_custo}, tempo de execução = {tempo_ap} seg', fontsize = 10)
    plt.xlabel('Número de repetições')
    plt.ylabel('Menor Distância (Km)')
    plt.show()
    

if __name__ == "__main__":
        main()