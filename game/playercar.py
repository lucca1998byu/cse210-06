from game.abstractcar import AbstractCar
import game.constants


#this class sets the start position and velocity of the car
class PlayerCar(AbstractCar):
    IMG = game.constants.RED_CAR
    START_POS = (180, 200)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel
        self.move()