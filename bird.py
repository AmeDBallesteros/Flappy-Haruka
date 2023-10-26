# bird.py
import pygame 
from settings import import_sprite

class Haruka(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # Información de Haruka
        self.frame_index = 0
        self.animation_delay = 3
        self.jump_move = -9
        # Animación 
        self.haruka_img = import_sprite("assets/haruka")
        self.image = self.haruka_img[self.frame_index]
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)
        # Posición de Haruka
        self.direction = pygame.math.Vector2(0,0)
        self.score = 0
    
    # Animación de Haruka volando
    def _animate(self):
        sprites = self.haruka_img
        sprite_index = (self.frame_index // self.animation_delay) % len(sprites)
        self.image = sprites[sprite_index]
        self.frame_index += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.frame_index // self.animation_delay > len(sprites):
            self.frame_index = 0
    
    # Para que Haruka vuele más alto
    def _jump(self):
        self.direction.y = self.jump_move
    
    # Actualizar el estado de Haruka
    def update(self, is_jump):
        if is_jump:
            self._jump()
        self._animate()