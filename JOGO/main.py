from random import randint
import utils

score_player = 0
score_computer = 0
num_partidas = 0
loop = 0

# Título do jogo / Game title.
utils.titulo()

while loop == 0:
  # Gerando um número aleatório de 1 à 3 para definir a escolha do computador.
  # Generating a random number between 1 and 3 to set computer decision.
  computer = randint(1, 3)
  # print(computer)  # log da resposta do computador.

  # Recebendo a escolha do jogador.
  player = utils.escolha_jogador()
  # print(player)  # log da resposta do jogador.

  # Imprimindo a frase "Joken...pô" para dar mais realismo ao jogo.
  utils.jokenpo()

  # Compara as escolhas do jogador e do computador, indicando se houve empate ou quem ganhou.
  result = utils.define_results(player, computer)

  # Contabiliza o placar
  if result == 1:
    score_player += 1
  elif result == 2:
    score_computer += 1

  # Apresenta o resultado no console.
  utils.result(result)

  num_partidas += 1
  # Recebe a escolha do usuário de continuar ou não.
  loop = utils.continuar()


utils.placar(score_player, score_computer, num_partidas)
