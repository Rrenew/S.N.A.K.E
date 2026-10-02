    # jogo cobrinha
    # enquanto o jogo estiver rodando:
    # 1. Ler os eventos (teclado, fechar janela)
    # 2. Atualizar a lógica (mover a cobra, checar colisão, comer)
    # 3. Desenhar tudo na tela
    # esperar um tiquinho (controlar a velocidade)
import random



LARGURA_GRADE = 20
ALTURA_GRADE = 20

cobra = [[10, 10], [9, 10], [8, 10]]

andar = [1, 0]
comida = random.randint(0, LARGURA_GRADE - 1), random.randint(0, ALTURA_GRADE - 1)
while(True):

 
 nova_cabeca = [cobra[0][0] + andar[0], cobra[0][1] + andar[1] ]

 if nova_cabeca[0] < 0 or nova_cabeca[0] >= LARGURA_GRADE or \
    nova_cabeca[1] < 0 or nova_cabeca[1] >= ALTURA_GRADE:
      print("Game Over! Bateu na parede.")
      break
 
 if nova_cabeca in cobra:
        print("Game Over! Comeu o próprio corpo.")
       
        break

 cobra.insert(0, nova_cabeca)

 if nova_cabeca == (comida):
    comida = [random.randint(0, LARGURA_GRADE - 1), random.randint(0, ALTURA_GRADE - 1)]
 else:
     cobra.pop()
 
 break
