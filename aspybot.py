from classes import *

readinstructions = ReadInstructions()
readinstructions.generate()

robot = AspiBot(readinstructions)

for instruction in readinstructions.instructions:
    robot.moving(instruction)
