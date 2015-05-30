import battleship.game.ships
import functools
from itertools import chain

class Board(object):
  def __init__(self):
    self.armada=set()
    self.attacks_received=[]

  def deploy_ship(self, ship):
    self.armada.add(ship)

  def receive_attack(self, coordinates):
    self.attacks_received.append((coordinates, self.occupied(coordinates)))
    for ship in self.armada:
      ship.take_hit(coordinates)

  def latest_received_attack_successful(self):
    ## print("BEFORE:", self.attacks_received)
    (latest_attack,attack_success) = self.attacks_received.pop()
    self.attacks_received.append((latest_attack, attack_success))
    ## print ("AFTER: ", latest_attack,attack_success)
    return attack_success

  def armada_summary(self):
    for ship in self.armada:
      for coordinate in ship.coordinates:
        print (ship, coordinate.x, coordinate.y)

  def occupied(self, coordinate):
    # return (coordinate in chain(ship.coordinates for ship in self.armada))
    return (coordinate in functools.reduce(set().union,(ship.coordinates for ship in self.armada)))