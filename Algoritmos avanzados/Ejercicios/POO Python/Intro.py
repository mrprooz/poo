class Rectangle (object):
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle: {self.color}, {self.width}x{self.height}"

r1 = Rectangle('verde', 10, 20)

print (r1)  # imprime: verde

