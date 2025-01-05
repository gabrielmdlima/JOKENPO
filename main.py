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
    # Título do jogo / Game title.
    utils.titulo()
    
    computer = computer_choice()
    # print(computer)  # log da resposta do computador.

    # Recebendo a escolha do jogador.
    player = utils.escolha_jogador()
    # print(player)  # log da resposta do jogador.

    # Imprimindo a frase "Joken...pô" para dar mais realismo ao jogo.
    utils.jokenpo()

    # Compara as escolhas do jogador e do computador, indicando se houve empate ou quem ganhou.
    result = utils.define_results(player, computer)

    # Contabiliza o placar
    count_score(result)

    # Contabiliza a quantidade de partidas
    num_partidas += 1

    # Apresenta o resultado no console.
    print(utils.result(result))

    # Recebe a escolha do usuário de continuar ou não.
    if utils.continuar() == True:
      run_game()
      break
    else:
      break

  utils.placar(score_player, score_computer, num_partidas)

if __name__ == '__main__':
  run_game()
