from setup import import_folder

class Explosion:

    def __init__(self,pts):
        self.get_assets()
        self.frame_idx = 0
        self.animation_speed = 0.15
        self.image = self.animations[self.frame_idx]
        self.rect = self.image.get_rect(center = pts)
        self.complete = False

    def get_assets(self):
        path = './assets/explosions/'
        self.animations= import_folder(path)

    def animate(self):
        self.frame_idx += self.animation_speed

        if self.frame_idx >= len(self.animations):
            self.complete = True
            return

        image = self.animations[int(self.frame_idx)]
        self.image = image
    
    def update(self):
        return self.complete

