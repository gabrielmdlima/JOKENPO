from random import randint
import utils


class GlobalVariables:
  def __init__(self):
    self.num_partidas = 0
    self.score_player = 0
    self.score_computer = 0


# Gerando um número aleatório de 1 à 3 para definir a escolha do computador.
# Generating a random number between 1 and 3 to set computer decision.
def computer_choice():
  choice = randint(1, 3)
  return choice


def count_score(self, result):
  if result == 1:
    self.score_player += 1
  elif result == 2:
    self.score_computer += 1


def run(self):

  while True:    
    computer = computer_choice()
    # print(computer)  # log da resposta do computador.

    player, entrance = utils.escolha_jogador()  # Recebendo a escolha do jogador.
    # print(player)  # log da resposta do jogador.

    utils.jokenpo(entrance)  # Imprimindo a frase "Jokenpô" com intervalos para dar mais realismo ao jogo.

    result = utils.define_results(player, computer)  # Compara as escolhas do jogador e do computador, indicando se houve empate ou quem ganhou.

    count_score(self, result)  # Contabiliza o placar.

    self.num_partidas += 1  # Contabiliza a quantidade de partidas.

    print(utils.result(result))  # Apresenta o resultado no console.

    if not utils.continuar():  # Recebe a escolha do usuário de continuar ou não.
      break

  utils.placar(self.score_player, self.score_computer, self.num_partidas)  # Imprime o placar ao final do jogo.

if __name__ == '__main__':
  self = GlobalVariables()
  run(self)
