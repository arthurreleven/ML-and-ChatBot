# Exercício 1: O Corredor Simples
import numpy as np
import time

print("\n--- Exercício 1: O Corredor Simples ---")
posicao_agente = 0
objetivo = 6
recompensa_total = 0

for passo in range(10):
    print(f"Passo {passo + 1}: Posição atual = {posicao_agente}")
    
    # Neste cenário simples, a única ação possível é 'avançar'.
    # TODO 1: Atualize a 'posicao_agente' para que ele avance 1 passo.
    posicao_agente += 1

    # posicao_agente + 1
    
    # TODO 2: Verifique se o agente alcançou o 'objetivo'.
    # Se sim, adicione 10 pontos à 'recompensa_total' e use 'break' para parar.
    if(posicao_agente == objetivo):
        print(">> Objetivo Alcançado!")
        recompensa_total += 10
        break
    else:
        recompensa_total -= 1

    # if(posicao_agente >= 10):
    #     print("Conseguiu")
    #     recompensa_total + 10
    #     break
    # else:
    #     print("Nao foi dessa vez")
    #     recompensa_total - 1 
    
    # Se não chegou, ele perde 1 ponto de 'recompensa_total' pelo esforço.
    
    time.sleep(0.1)

print(f"Simulação finalizada! Recompensa total: {recompensa_total}")