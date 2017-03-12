import pygame
import os

class Projectile():
    def __init__(self, character, proj_anim, proj_anim_time, width, height, health, position, velocity, accel):
        Particle.__init__(self, character, health, position, velocity, accel)
        self.entityID = None
        self.proj_anim = proj_anim
        self.proj_anim_time = proj_anim_time
        self.width = width
        self.height = height
        self.piercing = False
        self.pierced_objects = list()
        
    def load_graphic(self, gameworld, angle):
        proj_temp = pygame.image.load(os.path.join('data', self.character))
        proj_anim = Display(proj_temp, self.width, self.height, self.proj_anim, self.proj_anim_time)
        proj_anim.rect.center = self.position
        if self.velocity[0] < 0:
            proj_anim.flip = True
            angle = 180 + angle
        if self.velocity[1] > 0:
            angle = -angle
        proj_anim.angle = angle
        proj_c = (proj_anim,)
        self.entityID = gameworld.create_entity(proj_c)
        
    
class Particle():
    def __init__(self, character, health, position, velocity, accel):
        self.health = health
        self.character = character
        self.position = position
        self.velocity = velocity
        self.accel = accel
        self.angle = 0
        

class Display(pygame.sprite.Sprite):
    def __init__(self, character_sheet, width=None, height=None, animations=[1], time=[0]):
        pygame.sprite.Sprite.__init__(self)
        self.self_destruct = False
        self.play_once = False
        self.play_animation = True
        self.flip = False
        self.flip_y = False
        self.play_animation_till_end = False
        self.angle = 0
        if not width:
            width = character_sheet.get_width()
        if not height:
            height = character_sheet.get_height()
            
        self.frames = list()
        self.delay_between_frames = list()
        self.frames = animations
        self.time = time
        
        for f in range(len(self.frames)):
            self.delay_between_frames.append(int(self.time[f] / self.frames[f]))

        self.current_frame_x = 0
        self.current_animation = 0
        self.counter = 0
        self.image_frames = {}

        for animation_number in range(len(animations)):
            self.image_frames[animation_number] = list()
            for frame in range(animations[animation_number]):
                image = pygame.Surface([width, height], pygame.SRCALPHA)
                image.blit(character_sheet, (0, 0), (frame*width, animation_number*height, width, height))
                image.convert_alpha()
                self.image_frames[animation_number].append(image)
                
        self.original = self.image_frames[0][0]
        self.image = self.image_frames[0][0]
        self.rect = self.image.get_rect()

    def set_image(self, x, y=None):
        if not y:
            y = self.current_animation
            
        self.original = self.image_frames[y][x]
        
        if not self.angle == 0:
            self.image = pygame.transform.flip(self.original, self.flip, self.flip_y)
            self.image = self.rotate(self.image, self.angle)
        else:
            self.image = pygame.transform.flip(self.original, self.flip, self.flip_y)
            
    def set_animation_duration(self, anim_index, duration):
        self.time[anim_index] = duration
        self.delay_between_frames[anim_index] = (int(duration / self.frames[anim_index]))
  
    def rotate(self, image, angle):
        orig_rect = image.get_rect()
        rotate_image = pygame.transform.rotate(image, angle)
        rotate_rect = orig_rect.copy()
        rotate_rect.center = rotate_image.get_rect().center
        rotate_image = rotate_image.subsurface(rotate_rect).copy()
        return rotate_image