from Point import Point


class Fruit:

    def __init__(self, name, energy, point: Point, image):
        self.name = name
        self.energy = energy
        self.point = point

    def getname(self) -> str:
        return self.name

    def getenerergy(self) -> str:
        return self.energy

    def getpoint(self) -> Point :
        return self.point







