from time import sleep
import hands


def title():
  print('-=-'*10)
  print("""  ┬─┐┌─┐┌─┐┬┌─          
  ├┬┘│ ││  ├┴┐          
  ┴└─└─┘└─┘┴ ┴          
  ┌─┐┌─┐┌─┐┌─┐┬─┐       
  ├─┘├─┤├─┘├┤ ├┬┘       
  ┴  ┴ ┴┴  └─┘┴└─       
  ┌─┐┌─┐┬┌─┐┌─┐┌─┐┬─┐┌─┐
  └─┐│  │└─┐└─┐│ │├┬┘└─┐
  └─┘└─┘┴└─┘└─┘└─┘┴└─└─┘""")
  print('-=-'*10)


def titulo():
  print('-=-'*10)
  print("""  ┌─┐┌─┐┌┬┐┬─┐┌─┐      
  ├─┘├┤  ││├┬┘├─┤      
  ┴  └─┘─┴┘┴└─┴ ┴      
  ┌─┐┌─┐┌─┐┌─┐┬        
  ├─┘├─┤├─┘├┤ │        
  ┴  ┴ ┴┴  └─┘┴─┘      
  ┌┬┐┌─┐┌─┐┌─┐┬ ┬┬─┐┌─┐
   │ ├┤ └─┐│ ││ │├┬┘├─┤
   ┴ └─┘└─┘└─┘└─┘┴└─┴ ┴""")
  print('-=-'*10)


def escolha_jogador():
  while True:
    # Dá as opções do jogador
    # Give player's options
    hands.opcoes_dir()
    choice = str(input('Sua escolha: ')).strip().upper()  # Recebe a escolha do jogar / Receives player's choice.

    # Transforma a escolha do jogador em um número inteiro para ser comparada com a escolha da máquina.
    # Turns the player's choice in an int number to compare with the computer's choice.
    if choice == 'PEDRA':
      player = 1
      break
    elif choice == 'PAPEL':
      player = 2
      break
    elif choice == 'TESOURA':
      player = 3
      break
    else:
      print(f'\033[31mOpção "{choice}" inválida. Tente novamente!\033[m')
  return player


def jokenpo():
  print('Joken...', end='')
  sleep(1.25)
  print('pô')


#  Nessa função, o lado que aparece a mão do jogador é o esquerdo, deve ser usado com o hands.opcoes_esq()
def definir_resultado(player, computer):
  # Empate = 0 / Player ganha = 1 / Computador ganha = 2
  saida = 0
  if player == 1 and computer == 1:  # EMPATE PEDRA
    hands.pedra_pedra()
  elif player == 2 and computer == 2:  # EMPATE PAPEL
    hands.papel_papel()
  elif player == 3 and computer == 3:  # EMPATE TESOURA
    hands.tesoura_tesoura()
  elif player == 1 and computer == 3:  # PLAYER GANHA COM PEDRA
    hands.pedra_tesoura()
    saida = 1
  elif player == 2 and computer == 1:  # PLAYER GANHA COM PAPEL
    hands.papel_pedra()
    saida = 1
  elif player == 3 and computer == 2:  # PLAYER GANHA COM TESOURA
    hands.tesoura_papel()
    saida = 1
  elif player == 1 and computer == 2:  # COMPUTADOR GANHA COM PEDRA
    hands.pedra_papel()
    saida = 2
  elif player == 2 and computer == 3:  # COMPUTADOR GANHA COM PAPEL
    hands.papel_tesoura()
    saida = 2
  elif player == 3 and computer == 1:  # COMPUTADOR GANHA COM TESOURA
    hands.tesoura_pedra()
    saida = 2

  return saida


def define_results(player, computer):
  #  Empate = 0 / Player ganha = 1 / Computador ganha = 2
  saida = 0
  if player == 1 and computer == 1:  # EMPATE PEDRA
    hands.pedra_pedra()
  elif player == 2 and computer == 2:  # EMPATE PAPEL
    hands.papel_papel()
  elif player == 3 and computer == 3:  # EMPATE TESOURA
    hands.tesoura_tesoura()
  elif player == 1 and computer == 3:  # JOGADOR GANHA COM PEDRA
    hands.tesoura_pedra()
    saida = 1
  elif player == 2 and computer == 1:  # JOGADOR GANHA COM PAPEL
    hands.pedra_papel()
    saida = 1
  elif player == 3 and computer == 2:  # JOGADOR GANHA COM TESOURA
    hands.papel_tesoura()
    saida = 1
  elif computer == 1 and player == 3:  # COMPUTADOR GANHA COM PEDRA
    hands.pedra_tesoura()
    saida = 2
  elif computer == 2 and player == 1:  # COMPUTADOR GANHA COM PAPEL
    hands.papel_pedra()
    saida = 2
  elif computer == 3 and player == 2:  # COMPUTADOR GANHA COM TESOURA
    hands.tesoura_papel()
    saida = 2

  return saida  # Devolve o resultado


def result(entrada):
  sleep(0.75)
  if entrada == 1:
    print('\033[32mPARABÉNS! VOCÊ GANHOU!\033[m')
  elif entrada == 2:
    print('\033[31mQUE PENA! VOCÊ PERDEU!\033[m')
  else:
    print('\033[33mTEMOS UM EMPATE!\033[m')
