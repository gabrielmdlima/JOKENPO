from os import system, name
from time import sleep
import ascii
import json


def clear_screen():
  system('cls' if name == 'nt' else 'clear')


def title():
  clear_screen()
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
  clear_screen()
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


def escolha_jogador(data):
  while True:
    titulo()  # Título do jogo / Game title.

    # Dá as opções do jogador
    # Give player's options
    ascii.opcoes_dir()
    entrance = str(input('Sua escolha: ')).strip()  # Recebe a escolha do jogar / Receives player's choice.
    choice = entrance.upper()
    # Transforma a escolha do jogador em um número inteiro para ser comparada com a escolha da máquina.
    # Turns the player's choice in an int number to compare with the computer's choice.
    if choice == 'PEDRA':
      data.player = 1
      data.entrance = entrance
      break
    elif choice == 'PAPEL':
      data.player = 2
      data.entrance = entrance
      break
    elif choice == 'TESOURA':
      data.player = 3
      data.entrance = entrance
      break
    else:
      print(f'\033[31mOpção "{entrance}" inválida. Tente novamente!\033[m')
      sleep(2)
  return

def jokenpo(entrance):

  for i in range(3):
    titulo()
    ascii.opcoes_dir()
    print(f'Sua escolha: {entrance}')
    print()
    print('='*41)
    ascii.jokenpo(i)
    print('='*41)
    sleep(0.8)
  print()
  print('-'*41)


#  Nessa função, o lado que aparece a mão do jogador é o esquerdo, deve ser usado com o ascii.opcoes_esq()
def definir_resultado(player, computer):
  # Empate = 0 / Player ganha = 1 / Computador ganha = 2
  saida = 0
  if player == 1 and computer == 1:  # EMPATE PEDRA
    ascii.pedra_pedra()
  elif player == 2 and computer == 2:  # EMPATE PAPEL
    ascii.papel_papel()
  elif player == 3 and computer == 3:  # EMPATE TESOURA
    ascii.tesoura_tesoura()
  elif player == 1 and computer == 3:  # PLAYER GANHA COM PEDRA
    ascii.pedra_tesoura()
    saida = 1
  elif player == 2 and computer == 1:  # PLAYER GANHA COM PAPEL
    ascii.papel_pedra()
    saida = 1
  elif player == 3 and computer == 2:  # PLAYER GANHA COM TESOURA
    ascii.tesoura_papel()
    saida = 1
  elif player == 1 and computer == 2:  # COMPUTADOR GANHA COM PEDRA
    ascii.pedra_papel()
    saida = 2
  elif player == 2 and computer == 3:  # COMPUTADOR GANHA COM PAPEL
    ascii.papel_tesoura()
    saida = 2
  elif player == 3 and computer == 1:  # COMPUTADOR GANHA COM TESOURA
    ascii.tesoura_pedra()
    saida = 2

  return saida


def define_results(data):
  #  Empate = 0 / Player ganha = 1 / Computador ganha = 2
  saida = 0
  if data.player == 1 and data.computer == 1:  # EMPATE PEDRA
    ascii.pedra_pedra()
  elif data.player == 2 and data.computer == 2:  # EMPATE PAPEL
    ascii.papel_papel()
  elif data.player == 3 and data.computer == 3:  # EMPATE TESOURA
    ascii.tesoura_tesoura()
  elif data.player == 1 and data.computer == 3:  # JOGADOR GANHA COM PEDRA
    ascii.tesoura_pedra()
    saida = 1
  elif data.player == 2 and data.computer == 1:  # JOGADOR GANHA COM PAPEL
    ascii.pedra_papel()
    saida = 1
  elif data.player == 3 and data.computer == 2:  # JOGADOR GANHA COM TESOURA
    ascii.papel_tesoura()
    saida = 1
  elif data.computer == 1 and data.player == 3:  # COMPUTADOR GANHA COM PEDRA
    ascii.pedra_tesoura()
    saida = 2
  elif data.computer == 2 and data.player == 1:  # COMPUTADOR GANHA COM PAPEL
    ascii.papel_pedra()
    saida = 2
  elif data.computer == 3 and data.player == 2:  # COMPUTADOR GANHA COM TESOURA
    ascii.tesoura_papel()
    saida = 2

  data.result = saida


def result(entrada):
  print()  # Serve como \n para, se eu colocar junto na linha de baixo fica um espaço antes da impressão
  print('-'*41)
  sleep(0.6)
  if entrada == 1:
    return f'\n{"\033[32m PARABÉNS! VOCÊ GANHOU! \033[m":=^49}'
  if entrada == 2:
    return f'\n{"\033[31m QUE PENA! VOCÊ PERDEU! \033[m":=^49}'
  return f'\n{"\033[33m TEMOS UM EMPATE! \033[m":=^49}'

#  Pergunta se o jogador quer continuar
def continuar(data):
  # print('\n'*10)
  while True:
    entrada = str(input('\nJogar novamente? (S/N) ')).strip().upper()
    if entrada in 'NÃO':
      return False
    elif entrada in 'SIM':
      return True
    else:
      print('\n\033[31mOpção inválida! Tente novamente!\033[m')

#  Mostra o placar no console ao final do jogo
def placar(data):
  titulo()
  print(f'\nO resultado final de {data.num_partidas} partidas foi:\n')
  if data.score_player > data.score_computer:
    print(f'Você {data.score_player} X {data.score_computer} Computador')
  elif data.score_computer > data.score_player:
    print(f'Computador {data.score_computer} X {data.score_player} Você')
  else:
    print(f'EMPATE! {data.score_player} X {data.score_computer}')
  print()

def set_translation():
  with open('translations.json', 'r', encoding='utf-8') as file:
    translations = json.load(file)
  
  return translations