import time
import numpy as np

print("\n--- Exercício 2: O Agente Indeciso ---")
posicao_agente = 5
objetivo = 9
recompensa_total = 0

for passo in range(15):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Ação='{acao}'")
    
    # TODO 1: Crie uma estrutura if/elif para atualizar a 'posicao_agente'.
    # Se a ação for 'direita', some 1. Se for 'esquerda', subtraia 1.
    if(acao == "direita"):
        posicao_agente += 1
    elif(acao == "esquerda"):
        posicao_agente -= 1

    # TODO 2: Garanta que o agente não saia dos limites (0 e 9).
    # Use as funções max() e min() para isso. Ex: posicao = max(0, posicao)
    posicao_agente = max(0, posicao_agente)
    posicao_agente = min(9, posicao_agente)

    
    # TODO 3: Se o agente chegar no 'objetivo', dê +20 de recompensa e pare (break).
    # Senão, ele perde 1 ponto de recompensa.
    if(posicao_agente == objetivo):
        recompensa_total += 20
        break
    else:
        recompensa_total -= 1
    
    time.sleep(0.1)

print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")