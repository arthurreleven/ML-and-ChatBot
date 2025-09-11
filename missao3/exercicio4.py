import time
import numpy as np

# Exercício 4: O Chão de Lava


print("\n--- Exercício 4: O Chão de Lava ---")
posicao_agente = 0
objetivo = 9
chao_de_lava = [3, 4, 5]
recompensa_total = 0

for passo in range(20):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Ação='{acao}'")

    if acao == 'direita': posicao_agente += 1
    else: posicao_agente -= 1
    posicao_agente = np.clip(posicao_agente, 0, 9)
    
    if posicao_agente == objetivo:
        print("Objetivo alcançado!")
        recompensa_total += 50
        break
    
    if posicao_agente in (chao_de_lava):
        recompensa_passo = 5
        recompensa_total -= recompensa_passo
    else:
        recompensa_passo = 1 
        recompensa_total -= recompensa_passo
    
    time.sleep(0.5)
    

print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")
