from random import randint
import utils


class GameData:
  def __init__(self):
    self.num_partidas = 0
    self.score_player = 0
    self.score_computer = 0


  def get_language(self):
    while True:
      print("""
Idioma / Language
[1] Português
[2] Inglês
""")
      choice = int(input('Idioma / Language: '))
      if str(choice) in '12':
        break
      else:
        print('Tente novamente! / Try again!')

    self.language = 'pt' if choice == 1 else 'en'


  def set_translations(self):
    self.translations = utils.set_translation()
    
  
  

# Gerando um número aleatório de 1 à 3 para definir a escolha do computador.
# Generating a random number between 1 and 3 to set computer decision.
def computer_choice():
  choice = randint(1, 3)
  return choice


def count_score(data, result):
  if result == 1:
    data.score_player += 1
  elif result == 2:
    data.score_computer += 1



def run(data):
  utils.clear_screen()
  data.get_language()
  data.set_translations()

  while True:    
    computer = computer_choice()
    # print(computer)  # log da resposta do computador.

    player, entrance = utils.escolha_jogador()  # Recebendo a escolha do jogador.
    # print(player)  # log da resposta do jogador.

    utils.jokenpo(entrance)  # Imprimindo a frase "Jokenpô" com intervalos para dar mais realismo ao jogo.

    result = utils.define_results(player, computer)  # Compara as escolhas do jogador e do computador, indicando se houve empate ou quem ganhou.

    count_score(data, result)  # Contabiliza o placar.

    data.num_partidas += 1  # Contabiliza a quantidade de partidas.

    print(utils.result(result))  # Apresenta o resultado no console.

    if not utils.continuar():  # Recebe a escolha do usuário de continuar ou não.
      break

  utils.placar(data)  # Imprime o placar ao final do jogo.

if __name__ == '__main__':
  data = GameData()
  run(data)
