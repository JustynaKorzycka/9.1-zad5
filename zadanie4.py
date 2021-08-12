class Card:
  def __init__(self, value, figure):
    self.value = value
    self.figure = figure

class Deck:
  possible_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jupek', 'Dama', 'Król', 'As']
  possible_figure = ['diamont', 'heart', 'club', 'peak']
  pile_of_cards = []

  def __init__(self):
    for i in range(len(Deck.possible_figure)):
      for j in range(len(Deck.possible_value)):
        card = Card(Deck.possible_value[j], Deck.possible_figure[i])
        Deck.pile_of_cards.append(card)
  
  def shuffle(self):
    import random
    random.shuffle(Deck.pile_of_cards)
    
  def deal(self):
    last_card = Deck.pile_of_cards.pop()
    return(f'Wartość: {last_card.value} figura: {last_card.figure}')


def main():
  deck = Deck()
  deck.shuffle()
  print(len(deck.pile_of_cards))
  print(deck.deal())
  print(len(deck.pile_of_cards))

  
if __name__ == "__main__":
  main()