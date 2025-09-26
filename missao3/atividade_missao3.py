'''
Integrantes:
Arthur Luiz da Silva - 93729
Guilherme Castro Pires - 107802 
Lucas David Pereira Esteves - 98326
Marcelo Henrique da Silva Nunes - 82893
Otávio Henrique de Souza Silva - 102226
Pedro Henrique Carvilhe Silva - 8121
Victor Vicente - 

Navegue pelos exercícios dessa forma: Exercício 1, Exercício 2, Exercício 3...
'''

#Exercício 1
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

#Exercício 2
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

#Exercício 3
import time
import numpy as np

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

#Exercício 4
import time
import numpy as np

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

#Exercício 5
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