To run the demo:
- Download the standalone Jython from http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar
- Copy jython-standalone-2.7.0.jar and the *.py files to a temporary directory
- Enter the directory and execute:
  - java -jar jython-standalone-2.7.0.jar
  - from battleshipgame import *
  - PoC=BattleShipGame()
  - PoC.demo01()

Assumptions:
 - The following features are absent due to time constraints:
  - Creating a board with random valid ship placements is missing due to time constraints
  - A straightforward API function to determine the current state of the game, who finished (and who won)