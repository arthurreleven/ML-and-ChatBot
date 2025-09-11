import time
import numpy as np

# Exercício 3: O Caminho Perigoso
print("\n--- Exercício 3: O Caminho Perigoso ---")
posicao_agente = 5
objetivo = 9
buraco = 2
recompensa_total = 0

for passo in range(15):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Ação='{acao}'")
    
    if(acao == 'direita'):
        posicao_agente += 1
    else:
        posicao_agente -= 1
        posicao_agente = np.clip(posicao_agente, 0, 9) # np.clip faz o mesmo que max/min

    # TODO 1: Crie uma estrutura if/elif/else para as recompensas.
    # - Se a posição for igual ao 'objetivo': recompensa +20, fim.
    # - Se a posição for igual ao 'buraco': recompensa -50, fim.
    # - Senão: recompensa -1.

    if(posicao_agente == objetivo):
        recompensa_total += 20
        break
    elif(posicao_agente == buraco):
        recompensa_total -= 50
        print(">> Você Caiu!")
        break
    else:
        recompensa_total -= 1
    time.sleep(0.1)

else:
    print("Não foi dessa vez!")
    


print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")

