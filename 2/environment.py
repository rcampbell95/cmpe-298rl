import random
class Environment():
    def __init__(self):
        self.steps_left = 20

    def is_done(self):
        if self.steps_left == 0:
            print ("Game Over!")
            return True
        else:
            return False

    def get_observation(self):
        return [0, 0, 0]

    def get_actions(self):
        return [0, 1]

    def action(self, action):
        if self.is_done():
            raise Exception('EpisodeEnded')
        else:
            self.steps_left -= 1
            return random.randint(0,1000)
