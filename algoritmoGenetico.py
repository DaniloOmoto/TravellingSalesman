import random
import matplotlib.pyplot as plt
from distanceMatrix import distancias  
import time

# Função para criar uma rota aleatória
def criar_rota(matriz):
    rota = list(range(1, len(matriz)))  # Cria uma lista de todos os pontos, exceto o ponto inicial
    random.shuffle(rota)  # Embaralha a lista para criar uma rota aleatória
    rota = [0] + rota + [0]  # Adiciona o ponto inicial e final na rota
    return rota

# Função para calcular a distância total de uma rota
def calcular_distancia(matriz, rota):
    distancia_total = 0
    for i in range(len(rota) - 1):  # Para cada par de pontos consecutivos na rota
        distancia_total += matriz[rota[i]][rota[i + 1]]  # Adiciona a distância entre os pontos à distância total
    return distancia_total

# Função para cruzar duas rotas e criar uma nova
def cruzar_rotas(rota1, rota2):
    meio = len(rota1) // 2  # Encontra o ponto do meio
    filho = rota1[1:meio]  # Pega a sub-rota da primeira rota até o meio
    # Completa a rota com a segunda rota, evitando pontos já presentes na sub-rota e o ponto inicial
    filho += [ponto for ponto in rota2 if ponto not in filho and ponto != 0]
    filho = [0] + filho + [0]  # Adiciona o ponto inicial e final na rota
    return filho

# Função para mutar uma rota, trocando dois pontos de lugar
def mutar_rota(rota):
    i, j = random.sample(range(1, len(rota) - 1), 2)  # Escolhe dois pontos aleatórios, evitando o ponto inicial e final
    rota[i], rota[j] = rota[j], rota[i]  # Troca os pontos de lugar

# Implementação do algoritmo genético
def algoritmo_genetico(matriz, num_geracoes, tamanho_populacao, taxa_mutacao, taxa_elitismo):
    # Cria uma população inicial de rotas aleatórias
    populacao = [criar_rota(matriz) for _ in range(tamanho_populacao)]
    melhores_distancias = []  # Lista para armazenar a melhor distância de cada geração
    for geracao in range(num_geracoes):  # Para cada geração
        # Calcula a distância de cada rota na população
        pontuacoes = [(calcular_distancia(matriz, rota), rota) for rota in populacao]
        pontuacoes.sort()  # Ordena as rotas pela distância
        melhores_distancias.append(pontuacoes[0][0])  # Armazena a melhor distância desta geração
        # Seleciona a elite da população
        elite = pontuacoes[:max(2, int(taxa_elitismo * tamanho_populacao))]  # Garante pelo menos 2 indivíduos
        populacao = [rota for (_, rota) in elite]  # Cria uma nova população com a elite
        while len(populacao) < tamanho_populacao:  # Enquanto a população não estiver completa
            if random.random() < taxa_mutacao:  # Com uma probabilidade igual à taxa de mutação
                mutar_rota(populacao[-1])  # Muta a última rota adicionada à população
            pai1, pai2 = random.sample(populacao, 2)  # Escolhe dois pais aleatoriamente
            filho = cruzar_rotas(pai1, pai2)  # Cria um filho a partir dos pais
            populacao.append(filho)  # Adiciona o filho à população
    # Encontra a melhor rota na população final
    melhor_rota = min((calcular_distancia(matriz, rota), rota) for rota in populacao)
    return melhor_rota, melhores_distancias

def main():
    inicio = time.time()
    repeticoes = 10000
    n_populacao = 5
    mutacao = 0.01
    elitismo = 0.1
    melhor_rota, melhores_distancias = algoritmo_genetico(distancias, repeticoes, n_populacao, mutacao, elitismo)

# Imprime a melhor rota encontrada e seu custo
    print(f'O melhor caminho encontrado é {melhor_rota[1]} com um custo total de {melhor_rota[0]}')
    fim = time.time()
    tempo_total = fim - inicio
    tempo_ap = "{:.2f}".format(tempo_total)

# Plota a melhor distância de cada geração
    plt.plot(melhores_distancias)
    plt.suptitle(f'Melhor Distância por Geração do AG com População={n_populacao}')
    plt.title(f'Melhor Distância encontrada = {melhor_rota[0]}, tempo de execução = {tempo_ap} seg', fontsize = 10)
    plt.xlabel('Geração')
    plt.ylabel('Melhor Distância (Km)')
    plt.show()

if __name__ == "__main__":
        main()


