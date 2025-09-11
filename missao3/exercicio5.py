
import time
import numpy as np

print("\n--- Exercício 5: O Robô com Bateria ---")
posicao_agente = 0
objetivo = 9
recompensa_total = 0
bateria = 100 # Novo estado!

for passo in range(20):
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Bateria={bateria}%")
    bateria -= 10
    
    acao = np.random.choice(['esquerda', 'direita'])
    if acao == 'direita': posicao_agente += 1
    else: posicao_agente -= 1
    posicao_agente = np.clip(posicao_agente, 0, 9)
    
    if posicao_agente == objetivo:
        recompensa_total += 100
        print("Objetivo alcançado!")
        break
        
    if bateria <= 0:
        recompensa_total -= 30
        print("Acabou a bateria")
        break
    else:
        recompensa_total += 0
    
    time.sleep(0.5)
    
print(f"Simulação finalizada! Posição: {posicao_agente}, Bateria: {bateria}%, Recompensa: {recompensa_total}")
