print("begin ! ")


class ReadInstructions:
    def __init__(self):
        self.file = "test.txt"

    def generate(self):
        print("generate")
        with open(self.file, "r") as file:
            lines = file.readlines()

            gridsize = []
            startposition = []
            instruction = []

            for sprite in lines[0]:
                if sprite != " " and sprite != "\n":
                    gridsize.append(sprite)

            for sprite in lines[1]:
                if sprite != " " and sprite != "\n":
                    startposition.append(sprite)

            for sprite in lines[2]:
                if sprite != " " and sprite != "\n":
                    instruction.append(sprite)

        print(gridsize)
        print(startposition)
        print(instruction)





