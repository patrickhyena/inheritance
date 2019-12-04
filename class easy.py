class Circle():
    __radius: float 
    __color: str

    def __init__(self, radius = 1.0, color = "red"):
        self.__radius = radius
        self.__color = color

    def getRadius(self) -> float:
        return self.__radius

    def setRadius(self, radius: float):
        self.__radius = radius

    def getColor(self) -> str:
        return self.__color

    def setColor(self, color: str):
        self.__color = color

    def toString(self) -> str:
        return "This circle has radius of " + str(self.__radius) + ", with the color " + str(self.__color)

    def getArea(self) -> float:
         print(3.14 * (self.__radius**2))

class Cylinder(Circle):
    __height: float

    def __init__(self):
        Circle.__init__(self, radius = 1.0, color="red")


    def getHeight(self) -> float:
        return self.__height

    def setHeight(self, height: float):
        self.__height = height
    
    def toString(self) -> str:
        return "the cylinder has a height of " + str(self.__height) + ", and an area of " + str(super().getArea()) + "and with the color of " + str(self.__color)

    def getVolume(self) -> float:
        return super().getArea() * self.__height

theCircle = Circle()

theCircle.setRadius(5)

theCircle.setColor("pink")

print(theCircle.getRadius())

print(theCircle.getColor())

print(theCircle.toString())

print(theCircle.getArea())


theCylinder = Cylinder()

theCylinder.setHeight(8)

print(theCylinder.getHeight())

theCylinder.setColor("Magenta")

print(theCylinder.getColor())

theCylinder.setRadius(6)

print(theCylinder.getRadius())

print(theCylinder.getVolume())

      