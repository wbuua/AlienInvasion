import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	'''创建管理子弹的类，从sprite创建子类'''
	def __init__(self,ai):
		super().__init__()
		self.image=pygame.image.load('C:\\python_work\\alien_invasion\\images\\bullet.bmp')
		self.speed=0.3
		self.screen=ai.screen
		self.setting=ai.setting
		#在0，0处创建一个3*15的矩形
		self.rect=pygame.Rect(0,0,30,150)
		self.rect.midtop=ai.ship.rect.midtop
		#子弹的x位置始终跟随ship的位置，所以只要存储子弹的y位置
		self.y=float(self.rect.y)

	def update(self):
		self.y-=self.speed
		self.rect.y=self.y

	def draw_bullet(self):
		self.screen.blit(self.image,self.rect)
