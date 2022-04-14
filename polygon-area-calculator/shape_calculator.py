class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height 

  def __str__(self):
    return "Rectangle" + "(" + "width=" + str(self.width) + ", " + "height=" + str(self.height) + ")"
    
  def set_width(self, width):
    self.width = width
    return
    
  def set_height(self, height):
    self.height = height
    return

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    picture = ""
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    else :
      for h in range(self.height):
        for w in range(self.width):
          picture += "*"
        picture += "\n"

      return picture
                
  def get_amount_inside(self, shape):
    
    return int(self.get_area()/shape.get_area())

class Square(Rectangle):
    def __init__(self, length):
      super().__init__(length, length)

    def set_side(self, side):
      super().set_width(side)
      super().set_height(side)
  
    def __str__(self):
      return "Square" + "(" + "side=" + str(self.width)      + ")"

    
