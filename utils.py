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
    # Título do jogo / Game title.
    # Dá as opções do jogador
    # Give player's options
    if data.language == 'pt':
      titulo()
      ascii.opcoes_dir()
    elif data.language == 'en':
      title()
      ascii.options()
    input_message = data.translations[data.language]['get_choice']
    entrance = str(input(f'{input_message} ')).strip()  # Recebe a escolha do jogar / Receives player's choice.
    choice = entrance.upper()
    # Transforma a escolha do jogador em um número inteiro para ser comparada com a escolha da máquina.
    # Turns the player's choice in an int number to compare with the computer's choice.
    if choice == 'PEDRA' or choice == 'ROCK':
      data.player = 1
      data.entrance = entrance
      break
    elif choice == 'PAPEL' or choice == 'PAPER':
      data.player = 2
      data.entrance = entrance
      break
    elif choice == 'TESOURA' or choice == 'SCISSOR':
      data.player = 3
      data.entrance = entrance
      break
    else:
      message = data.translations[data.language]['invalid_input'].format(entrance= f'\033[1m{entrance}\033[0;31m')
      print(f"\n\033[31m{message}")
      for i in range(3, 0, -1):
        print(f'{i}..', end=' ', flush=True)
        sleep(1)
      print("\033[m")
  return


def jokenpo(data):

  for i in range(3):
    if data.language == 'pt':
      titulo()
      ascii.opcoes_dir()
    elif data.language == 'en':
      title()
      ascii.options()
    print(f'{data.translations[data.language]["get_choice"]}', data.entrance)
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


def result(data):
  print()  # Serve como \n para, se eu colocar junto na linha de baixo fica um espaço antes da impressão
  print('-'*41)
  sleep(0.6)
  if data.result == 1:
    message = f"\033[32m{data.translations[data.language]['you_win']}\033[m"
    return f'\n{message:=^49}'
  if data.result == 2:
    message = f"\033[31m{data.translations[data.language]['you_loose']}\033[m"
    return f'\n{message:=^49}'
  else:
    message = f"\033[33m{data.translations[data.language]['draw']}\033[m"
    return f'\n{message:=^49}'

#  Pergunta se o jogador quer continuar
def continuar(data):
  # print('\n'*10)
  while True:
    entrada = str(input(data.translations[data.language]['play_again'])).strip().upper()[0]
    if entrada in 'N':
      return False
    elif entrada in 'SY':
      return True
    else:
      message = data.translations[data.language]['invalid_input'].format(entrance=entrada)
      print(f"\n\033[31m{message}\033[m")

#  Mostra o placar no console ao final do jogo
def placar(data):
  titulo() if data.language == 'pt' else title()

  matches = data.translations[data.language]['scoreboard'].format(partidas=data.num_partidas)
  print(matches)
  if data.score_player > data.score_computer:
    scoreboard = data.translations[data.language]['score_winner'].format(player=data.score_player, computer=data.score_computer)
    print(scoreboard)
  elif data.score_computer > data.score_player:
    scoreboard = data.translations[data.language]['score_looser'].format(computer=data.score_computer, player=data.score_player)
    print(scoreboard)
  else:
    scoreboard = data.translations[data.language]['score_draw'].format(player=data.score_player, computer=data.score_computer)
    print(scoreboard)
  print()

def set_translation():
  with open('translations.json', 'r', encoding='utf-8') as file:
    translations = json.load(file)
  
  return translations
