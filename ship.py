import pygame
class Ship:
	'''管理飞船的类'''
	def __init__(self,game_ship):
		'''初始化飞船并设定初始位置，game_ship是一个从AlienInvasion中实例化出来的对象'''
		self.screen=game_ship.screen
		self.screen_rect=game_ship.screen.get_rect()
		self.ship_speed=0.5

		#加载飞船图像并获取其外接矩形
		self.image=pygame.image.load('C:\\python_work\\alien_invasion\\images\\ship.bmp')
		self.rect=self.image.get_rect()

		#对于每艘飞船，将其放在屏幕底部
		self.rect.midbottom=self.screen_rect.midbottom

		self.x=float(self.rect.x)

		#设置飞船移动标签
		self.move_right=False
		self.move_left=False

	def blitme(self):
		'''在指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)

	def moving(self):
		'''飞船移动的方法'''
		if self.move_right==True and self.rect.right<=self.screen_rect.right:
			self.x+=self.ship_speed
		elif self.move_left==True and self.rect.left>0:
			self.x-=self.ship_speed

		self.rect.x=self.x	
