import battleship.game.board
import battleship.game.ships
import battleship.game.coordinate

class BattleShipGame(object):
  def __init__(self):
    self.player1board = battleship.game.board.Board()
    self.player2board = battleship.game.board.Board()

  def player1_attacks_coordinate(self, coordinate):
    self.player2board.receive_attack(coordinate)

  def player2_attacks_coordinate(self, coordinate):
    self.player1board.receive_attack(coordinate)

  def demo01(self):
    self.player1board.deploy_ship(battleship.game.ships.Carrier(battleship.game.coordinate.Coordinate(2,2)))
    self.player1board.deploy_ship(battleship.game.ships.Battleship(battleship.game.coordinate.Coordinate(4,4)))
    self.player1board.deploy_ship(battleship.game.ships.Submarine(battleship.game.coordinate.Coordinate(6,6)))
    self.player1board.deploy_ship(battleship.game.ships.Cruiser(battleship.game.coordinate.Coordinate(7,7)))
    self.player1board.deploy_ship(battleship.game.ships.Patrol(battleship.game.coordinate.Coordinate(8,8)))
    
    self.player2board.deploy_ship(battleship.game.ships.Carrier(battleship.game.coordinate.Coordinate(1,3)))
    self.player2board.deploy_ship(battleship.game.ships.Battleship(battleship.game.coordinate.Coordinate(3,3)))
    self.player2board.deploy_ship(battleship.game.ships.Submarine(battleship.game.coordinate.Coordinate(5,3)))
    self.player2board.deploy_ship(battleship.game.ships.Cruiser(battleship.game.coordinate.Coordinate(7,3)))
    self.player2board.deploy_ship(battleship.game.ships.Patrol(battleship.game.coordinate.Coordinate(9,3)))

  def demo02(self):
    self.player2board.armada_summary()
    self.player1_attacks_coordinate(battleship.game.coordinate.Coordinate(3,3))
    print("Player 1's latest attack was: ", self.player2board.latest_received_attack_successful())
    self.player2board.armada_summary()

    self.player2_attacks_coordinate(battleship.game.coordinate.Coordinate(9,3))
    print("Player 2's latest attack was: ", self.player1board.latest_received_attack_successful())

    self.player2board.armada_summary()
    self.player1_attacks_coordinate(battleship.game.coordinate.Coordinate(9,3))
    print("Player 1's latest attack was: ", self.player2board.latest_received_attack_successful())
    self.player2board.armada_summary()
