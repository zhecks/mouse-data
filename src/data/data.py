import os

path = os.path.dirname(os.path.abspath(__file__))


class Data:
    def __init__(self):
        self.raw_position = []
        self.normalized_data = []
        self.__total()

    def process(self, width, height):
        self.__preprocessing(width, height)
        self.__save()

    def add_raw_position(self, position: list):
        if position is None or len(position) != 2:
            raise Exception("position is illegal")
        self.raw_position.append(position)

    def __preprocessing(self, width, height):
        if width <= 0 or height <= 0:
            raise Exception("width or height is illegal")
            # normalized data to [0,1]
        for pos in self.raw_position:
            self.normalized_data.append([pos[0] / width, pos[1] / height])

    def __total(self):
        filename = f"{path}/data.txt"
        with open(filename, "r") as f:
            total = len(f.readlines())
        f.close()
        self.total = total

    def __save(self):
        filename = f"{path}/data.txt"
        with open(filename, "a") as f:
            for pos in self.normalized_data:
                f.write(f"{pos[0]},{pos[1]}\n")
        f.close()
