print("begin ! ")


class ReadInstructions:
    def __init__(self):
        self.file = "test.txt"
        self.gridsize = []
        self.startposition = []
        self.instructions = []

    def generate(self):
        print("generate")
        with open(self.file, "r") as file:
            lines = file.readlines()

            self.gridsize = lines[0].split()
            self.startposition = lines[1].split()

            for sprite in lines[2]:
                if sprite != " " and sprite != "\n":
                    self.instructions.append(sprite)

        print(self.gridsize)
        print(self.startposition)
        print(self.instructions)


class AspiBot(ReadInstructions):

    def __init__(self, readinstructions):
        self.x = int(readinstructions.startposition[0])
        self.y = int(readinstructions.startposition[1])
        self.max_x = int(readinstructions.gridsize[0])
        self.max_y = int(readinstructions.gridsize[1])
        self.direction = readinstructions.startposition[2]

    def moving(self, order):
        # print("order is ", order)
        if order != "A":
            if self.x < self.max_x and self.y < self.max_y:
                self.direction = order
                # print(self.direction)
            else:
                print("You hit a wall ! ")

        if order == "A":
            if self.direction == "N":
                self.y = (self.y + 1)
            if self.direction == "S":
                self.y = self.y - 1
            if self.direction == "E":
                self.x = self.x + 1
            if self.direction == "W":
                self.x = self.x - 1
        print(self.x, self.y, self.direction)





