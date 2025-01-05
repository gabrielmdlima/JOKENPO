import utils

num_partidas = 0
score_player = 0
score_computer = 0

# Gerando um número aleatório de 1 à 3 para definir a escolha do computador.
# Generating a random number between 1 and 3 to set computer decision.
def computer_choice():
  from random import randint
  choice = randint(1, 3)
  return choice


def count_score(result):
  global score_player, score_computer
  if result == 1:
    score_player += 1
  elif result == 2:
    score_computer += 1


def run_game():
  global num_partidas, score_player, score_computer

  while True:
    utils.clear_screen()
    utils.titulo()  # Título do jogo / Game title.
    
    computer = computer_choice()
    # print(computer)  # log da resposta do computador.

    player = utils.escolha_jogador()  # Recebendo a escolha do jogador.
    # print(player)  # log da resposta do jogador.

    utils.jokenpo()  # Imprimindo a frase "Joken...pô" para dar mais realismo ao jogo.

    result = utils.define_results(player, computer)  # Compara as escolhas do jogador e do computador, indicando se houve empate ou quem ganhou.

    count_score(result)  # Contabiliza o placar.

    num_partidas += 1  # Contabiliza a quantidade de partidas.

    print(utils.result(result))  # Apresenta o resultado no console.

    if utils.continuar() == True:  # Recebe a escolha do usuário de continuar ou não.
      run_game()
      break
    else:
      break

  utils.placar(score_player, score_computer, num_partidas)  # Imprime o placar ao final do jogo.

if __name__ == '__main__':
  run_game()
