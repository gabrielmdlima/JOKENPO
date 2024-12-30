from random import randint
from time import sleep
import hands

# Título do jogo / Game title
hands.titulo()

# Gerando um número aleatório de 1 à 3 para definir a escolha do computador
# Generating a random number between 1 and 3 to set computer decision
computer = randint(1, 3)
# print(computer)  # log da resposta do computador

player = 1  # Já é 'PEDRA' / Already is rock
while True:
  # Dá as opções do jogador
  # Give player's options
  hands.opcoes()
  # print('Pedra, Papel ou Tesoura?')
  choice = input('Sua escolha: ').strip().upper()  # Recebe a escolha do jogar / Receives player's choice
  if choice == 'PAPEL':
    player = 2
    break
  elif choice == 'TESOURA':
    player = 3
    break
  elif choice == 'PEDRA':
    break
  else:
    print('\n'*20)  # Serve para "limpar" o console caso o player erre a opção, os.system('cls') não funciona
    print(f'\033[31mOpção inválida. Tente novamente!\033[m\n')
# print(player)  # log da resposta do jogador

# print('\n'*30)
print('Joken...', end='')
sleep(1.25)
print('pô')

resultado = 0  # Empate = 0 / Player ganha = 1 / Computador ganha = 2

if player == 1 and computer == 1:  # EMPATE
  hands.pedra_pedra()
elif player == 2 and computer == 2:  # EMPATE
  hands.papel_papel()
elif player == 3 and computer == 3:  # EMPATE
  hands.tesoura_tesoura()
elif player == 1 and computer == 3:  # PLAYER GANHA
  hands.pedra_tesoura()
  resultado = 1
elif player == 2 and computer == 1:  # PLAYER GANHA
  hands.papel_pedra()
  resultado = 1
elif player == 3 and computer == 2:  # PLAYER GANHA
  hands.tesoura_papel()
  resultado = 1
elif computer == 2 and player == 1:  # COMPUTADOR GANHA
  hands.pedra_papel()
  resultado = 2
elif player == 2 and computer == 3:  # COMPUTADOR GANHA
  hands.papel_tesoura()
  resultado = 2
elif player == 3 and computer == 1:  # COMPUTADOR GANHA
  hands.tesoura_pedra()
  resultado = 2

sleep(0.75)
if resultado == 1:
  print('PARABÉNS! VOCÊ GANHOU!')
elif resultado == 2:
  print('QUE PENA! VOCÊ PERDEU!')
else:
  print('TEMOS UM EMPATE!')
