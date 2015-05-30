import battleship.game.coordinate

class Ship(object):
  def __init__(self, coordinate):
    self.coordinates=set()
    self.setCoordinates(coordinate)

  def rotate(self):
    for XYPair in self.coordinates:
      XYPair.inverse()

  def take_hit(self, coordinate):
    if coordinate in self.coordinates:
      self.coordinates.remove(coordinate)

  def afloat(self):
    return (len(self.coordinates)>0)

  def setCoordinates(self, XYPair):
    for coordinate in (battleship.game.coordinate.Coordinate(XYPair.x, y) for y in range(XYPair.y, XYPair.y + self.ship_length)):
      self.coordinates.add(coordinate)

class Carrier(Ship):
  def __init__(self, coordinate):
    self.ship_width = 1
    self.ship_length = 5
    Ship.__init__(self, coordinate)

	
class Battleship(Ship):
  def __init__(self, coordinate):
    self.ship_width = 1
    self.ship_length = 4
    Ship.__init__(self, coordinate)
	
class Submarine(Ship):
  def __init__(self, coordinate):
    self.ship_width = 1
    self.ship_length = 3
    Ship.__init__(self, coordinate)

class Cruiser(Ship):
  def __init__(self, coordinate):
    self.ship_width = 1
    self.ship_length = 2
    Ship.__init__(self, coordinate)

class Patrol(Ship):
  def __init__(self, coordinate):
    self.ship_width = 1
    self.ship_length = 1
    Ship.__init__(self, coordinate)
