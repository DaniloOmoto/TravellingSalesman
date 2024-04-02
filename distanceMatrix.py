import pandas as pd
import requests
import random
from random import sample
from key import apiKey

def get_distance(origem,destino):
    route = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + origem + "&wp.1=" + destino + "/&key=" + apiKey
    r = requests.get(url = route)
    result = r.json()
    distance = result["resourceSets"][0]["resources"][0]["travelDistance"]
    print(distance)
    return distance

def generate_matrix(endereco):
    distancias = []
    for origem in endereco:
        dist = []
        for destino in endereco:
            dist.append(get_distance(origem, destino))
        distancias.append(dist)
    print(distancias)


def main():
    pontos_turiscos = {
        "Slaviero Curitiba Batel":"Avenida Visconde de Guarapuava, 4069, Batel",
        "Jardim Botânico": "Avenida Prof. Lothario Meissner, 632 - Jardim Botânico",
        "Ópera de Arame": "Rua João Gava, 920 - Abranches",
        "Parque Tanguá": "Rua Oswaldo Maciel, 97 - Taboão",
        "Museu Oscar Niemeyer": "Rua Mal. Hermes, 999 - Centro Cívico",
        "Bosque Alemão": "Rua Nicolo Paganini, s/n - Pilarzinho",
        "Rua das Flores": "R. XV de Novembro, 36 - Centro",
        "Parque Barigui": "Avenida Cândido Hartmann, S/N - Bigorrilho",
        "Teatro Guaíra": "Rua XV de Novembro, 971 - Centro",
        "Mercado Municipal": "Avenida Sete de Setembro, 1865 - Centro",
        "Largo da Ordem": "Rua José Bonifácio, 33 - Centro",
        "Museu Ferroviario" : "Av. Sete de Setembro, 2775 - Rebouças",
        "Torre Panorâmica" : "Rua Professor Lycio Grein Castro Vellozo, 191 - Mercês"
    }

    endereco = list(pontos_turiscos.values())
    generate_matrix(endereco)
   

    
    
distancias = [[0, 5.48, 8.457, 9.367, 7.311, 5.824, 2.752, 8.297, 4.143, 3.485, 2.734, 2.483, 3.054], 
              [5.51, 0, 9.898, 11.565, 6.144, 9.04, 5.294, 13.808, 4.229, 3.341, 5.511, 4.383, 7.792], 
              [7.401, 9.662, 0, 1.875, 4.041, 3.187, 5.679, 8.309, 5.929, 7.72, 5.543, 6.805, 6.294], 
              [8.695, 10.786, 1.505, 0, 5.335, 3.66, 6.973, 9.827, 7.223, 8.844, 6.837, 8.099, 7.588], 
              [5.85, 5.65, 4.167, 5.834, 0, 3.309, 3.303, 6.391, 2.464, 3.708, 2.238, 4.969, 4.376], 
              [5.154, 8.682, 3.145, 3.727, 3.677, 0, 4.263, 6.287, 5.119, 6.74, 4.733, 5.389, 3.012], 
              [1.722, 4.592, 6.434, 8.101, 4.274, 4.924, 0, 5.803, 1.634, 2.18, 1.073, 1.126, 3.803], 
              [4.568, 8.83, 7.306, 7.888, 6.423, 4.281, 4.803, 0, 5.24, 6.485, 4.667, 6.044, 2.348], 
              [2.672, 4.073, 5.937, 7.604, 3.592, 4.825, 1.284, 5.853, 0, 1.789, 1.501, 1.791, 3.648], 
              [2.737, 2.349, 7.049, 8.716, 3.927, 6.191, 2.531, 11.035, 1.466, 0, 2.748, 1.856, 4.925], 
              [2.269, 4.921, 5.594, 7.261, 3.608, 4.333, 0.547, 5.142, 1.331, 2.576, 0, 1.673, 3.142], 
              [2.97, 3.332, 7.578, 9.245, 5.163, 6.72, 2.77, 11.268, 1.995, 1.048, 2.987, 0, 5.469], 
              [3.129, 7.494, 5.729, 6.311, 4.846, 2.704, 3.019, 2.359, 3.904, 5.149, 3.331, 4.145, 0]]


if __name__ == "__main__":
        main()
