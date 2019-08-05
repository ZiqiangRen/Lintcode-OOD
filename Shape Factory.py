"""
Your object will be instantiated and called as such:
sf = ShapeFactory()
shape = sf.getShape(shapeType)
shape.draw()
"""
class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')
        

class Triangle(Shape):
    # Write your code here
    def draw(self):
        print '  /\\\n /  \\\n/____\\\n'

class Rectangle(Shape):
    # Write your code here
    def draw(self):
        print ' ----\n|    |\n ----'

class Square(Shape):
    # Write your code here
    def draw(self):
        print ' ----\n|    |\n|    |\n ----'

class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        # Write your code here
        if shapeType == "Square":
            res = Square()
        elif shapeType == "Rectangle":
            res = Rectangle()
        elif shapeType == "Triangle":
            res = Triangle()
        else:
            res = None
        return res
