#Note: As this module is imported into quiz.py, all paths become
#      relative to where quiz.py is
import csv
import json
import pygame
from pygame.locals import *
from pygame.time import Clock
from src.scene import Scene

global FPS

class Game():
    class __Game():
        def __init__(self, config_info):
            global FPS
            FPS = config_info["FPS"]

            self.is_start = False
            self.is_run = False
            self.delta = 0
            self.time_since_started = 0
            self.clock = Clock()

            pygame.init()
            self.screen = pygame.display.set_mode((config_info["WIDTH"],
                                                   config_info["HEIGHT"]))
            pygame.display.set_caption(config_info["CAPTION"])
            self.time_since_started = pygame.time.get_ticks()

            reader_data = []
            with open("./src/data/questions.csv", newline="") as questions,\
                 open("./src/data/scene_data.json") as scene_info:
                q_reader = csv.reader(questions)
                reader_data.extend([row for row in q_reader])
                scene_cfg = json.load(scene_info)
            self.scene = Scene(q_reader, scene_cfg)
            self.is_start = pygame.get_init()
            self.is_run = True

        def process_events(self):
            for evt in pygame.event.get():
                if evt.type == QUIT:
                    self.quit()
                    
        def update(self, delta):
            self.scene.update(delta)

        def render(self, target):
            self.scene.render(target)
            pygame.display.flip()

        def run(self):
            if not self.is_start:
                return
            while self.is_run:
                self.process_events()
                self.update(self.delta)
                self.render(self.screen)
                self.delta = self.clock.tick(FPS)
                self.time_since_started = pygame.time.get_ticks()
            pygame.quit()

        def quit(self):
            self.is_run = False

    #Singleton:
    instance = None
    def __init__(self, cfg_info):
        if not Game.instance:
            Game.instance = Game.__Game(cfg_info)

    def __getattr__(self, name):
        return getattr(self.instance, name)
