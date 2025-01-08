import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	def __init__(self,ai):
		super().__init__()
		self.screen=ai.screen
		self.image=pygame.image.load('images/alien.bmp')
		self.rect=self.image.get_rect()
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		self.x=float(self.rect.x)
		self.setting=ai.setting

	def check_edges(self):
		screen_rect=self.screen.get_rect()
		if self.rect.right>=screen_rect.right or self.rect.left<=0:
			return True	

	def update(self):
		self.x += (self.setting.alien_speed*self.setting.fleet_dirction)
		self.rect.x=self.x
