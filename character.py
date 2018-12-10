import models

class Pile:
  cards = []
  def __init__(self, cards):
    self.cards = cards

  def take(self, ind):
    """returns a card from the pile, removing it."""
    card = self.cards[:][ind]
    del self.cards[ind]
    return card

  def shuffle(self):
    #TODO
    pass

class Character(Creature):
  player = True
  deck = Pile([])
  hand = Pile([])
  discard = Pile([])
  exhaust = Pile([])
  def __init__(self, hp, maxHp, deck, relics):
    #TODO
    pass