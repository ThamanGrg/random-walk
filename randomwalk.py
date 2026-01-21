from random import choice

class RandomWalk:
    def __init__(self, num_points= 5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            
            x_steps = get_steps()
            y_steps = get_steps()

            if x_steps == 0 and y_steps == 0:
                continue
            
            next_x = self.x_values[-1] + x_steps
            next_y = self.y_values[-1] + y_steps
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
def get_steps():
    direction = choice([-1,1])
    distance = choice([1,2,3,4,5,6,7,8,9])
    return direction * distance