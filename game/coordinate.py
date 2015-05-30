class Coordinate(object):
  def __init__(self, inputX, inputY):
    self.x = inputX
    self.y = inputY

  def __eq__(self, other):
    return (self.x == other.x) and (self.y == other.y)

  def __hash__(self):
    return hash(self.x + self.y)

  def inverse(self):
    temp = self.x
    self.x = self.y
    self.y = temp