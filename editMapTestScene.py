import os
import os.path
import sys

import numpy
import numpy.random

import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.input import Input

from camera import Camera
from pluginManager import PluginManager
from tray import Tray

class CameraController:
    def __init__(self):
        self.fPos = (0.0, 0.0)
        self.pos = (int(self.fPos[0]), int(self.fPos[1]))
        self.xv, self.yv = 0.0, 0.0
        self.speed = 1.2
        self.shift_speed = self.speed * 5.0

    def update(self, keys):
        w, a, s, d, shift = (
            keys[pygame.K_w],
            keys[pygame.K_a],
            keys[pygame.K_s],
            keys[pygame.K_d],
            keys[pygame.K_LSHIFT],
        )

        if shift:
            speed = self.shift_speed
        else:
            speed = self.speed

        self.xv = 0.0
        self.yv = 0.0

        if w:
            self.yv -= speed
        if a:
            self.xv -= speed
        if s:
            self.yv += speed
        if d:
            self.xv += speed

        x, y = self.fPos
        x += self.xv
        y += self.yv
        self.fPos = x, y
        self.pos = (int(self.fPos[0]), int(self.fPos[1]))

class EditMapTestScene(Scene):
    def on_escape(self):
        sys.exit()

    def blit(self):
        Camera.blitView()
        for tray in self.trays:
            tray.blit(utils.screen)

    def update(self):
        keys = pygame.key.get_pressed()
        self.camera_controller.update(keys)
        Camera.update()
        if self.mouse_buttons[0]:
            for tray in self.trays:
                tray.handle(self.mouse_pos, self.mouse_rel)
        else:
            for tray in self.trays:
                tray.should_move = False
                tray.should_resize = False
                tray.edge = 0b0000

    def __init__(self):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        PluginManager.loadPlugins()
        Camera.init()
        self.camera_controller = CameraController()
        Camera.lock(self.camera_controller)
        self.trays = set()
        self.trays.add(
            Tray(
                (utils.SCREEN_W - 270, 20),
                (250, 800),
                min_width=250, max_width=800,
                min_height=250, max_height=800
            )
        )
