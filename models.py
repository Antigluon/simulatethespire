from enum import Enum
from random import randint
class Target(Enum):
  SELF = 1
  ENEMY = 2
  ALLENEMIES = 3
  ALLY = 4
  ALLALLIES = 5


class Effect:
  def __init__(self):
    pass
  def apply(self, target):
    pass

class Ability:
  effects = []
  def __init__(self, *args):
    """takes in tuples of (target, Effect)"""
    for effect in args:
      self.effects.append( 
          (effect[0], effect[1]) #(target, Effect)
        )
  def use(self, targetPosition):


class Creature:
  hp = 0
  maxHp = 0
  def __init__(self, hp, maxHp):
    self.hp = hp
    self.maxHp = maxHp

  def takeTurn(self, fight):
    pass

class Enemy(Creature):
  player = False
  abilities = []
  def __init__(self, minHp, maxHp, abilities):
    hp = randint(minHp, maxHp)
    super().__init__(self, hp, hp)
    self.abilities = abilities

class Fight:
  #TODO
  pass