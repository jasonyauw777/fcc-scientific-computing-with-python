import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self, **balls):
    self.contents = []
    for key, value in balls.items():
      self.contents += [key] * value

  def draw(self, number):
    if number > len(self.contents):
      return self.contents
    else :
      draw = []
      for i in range(number):
        ball_drawn = random.choice(self.contents)
        self.contents.remove(ball_drawn)
        draw.append(ball_drawn)

      return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_result = 0
  for exp in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    draw = hat_copy.draw(num_balls_drawn)
    successful = True
    for key, value in expected_balls.items():
      if draw.count(key) < value:
        successful = False
        break

    if successful :
      success_result += 1

  return success_result/num_experiments
      
