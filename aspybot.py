from classes import *

"""Run this file to launch the Bot ! """

readinstructions = ReadInstructions()
readinstructions.generate()

robot = AspiBot(readinstructions)

for instruction in readinstructions.instructions:
    robot.moving(instruction)
