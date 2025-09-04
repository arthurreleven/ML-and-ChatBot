import time

# Ambiente
posicoes = [0, 1, 2, 3, 4]
posicao_agente = 0
posicao_comida = 4
recompensa_total = 0

while posicao_agente != posicao_comida:
    # O agente só sabe andar para a direita
    posicao_agente+=1

    # Recompensa do passo
    Recompensa = -1

    # Se chegou na comida
    if posicao_agente == posicao_comida:
     Recompensa+20

    recompensa_total+=Recompensa

    print(f"Agente na posição {posicao_agente}, Recompensa: {Recompensa}, Total: {recompensa_total}")

print("\nFim do episódio! O agente encontrou a comida 🍖")


