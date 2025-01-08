#控制整体游戏；创建一个整体游戏的类，并实例化一个游戏出来。整体游戏初始化的属性只有屏幕尺寸。整体游戏的行为只有退出和刷屏。
#模块pygame包含开发游戏所含的功能
#pygame.init（）初始化背景
#pygame.dispaly.set_mode()创建一个显示窗口, 返回一个surface对象
#pygame.event.get() 检测事件，并返回一个列表，包含上一次被调用后所发生的所有事件
#模块sys 提供游戏退出工具

import pygame
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
class AlienInvasion:
	'''从Settings类中创建一个实例'''
	def __init__(self):
		pygame.init()
		self.setting=Settings()
		self.screen=pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
		pygame.display.set_caption('AlienInvasion')
		#初始化飞船
		self.ship=Ship(self)
		self.bullets=pygame.sprite.Group()
		self.aliens=pygame.sprite.Group()
		self._create_fleet()

	def run_game(self):
		'''开始游戏的主循环'''
		while True:
			self._event()
			self.ship.moving()
			self._update_bullet()
			self._update_alien()
			self._screen()

	def _event(self):
		'''监视键盘和鼠标事件'''
		for event in pygame.event.get():
			#退出游戏
			if event.type==pygame.QUIT:
				sys.exit()
			#移动飞船	
			elif event.type==pygame.KEYDOWN:
				self._keydown_event(event)
			elif event.type==pygame.KEYUP:
				self._keyup_event(event)
				
	def _keydown_event(self,arg=None):
		if arg.key==pygame.K_RIGHT:
			self.ship.move_right=True	
		elif arg.key==pygame.K_LEFT:
			self.ship.move_left=True
		elif arg.key==pygame.K_q:
			sys.exit()
		elif arg.key==pygame.K_SPACE:
			self._fire_bullet()

	def _keyup_event(self,arg=None):
		if arg.key==pygame.K_RIGHT:
			self.ship.move_right=False
		elif arg.key==pygame.K_LEFT:
			self.ship.move_left=False

	def _fire_bullet(self):
		if len(self.bullets) < self.setting.bullets_allowed:
			new_bullet=Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullet(self):
		self.bullets.update()

		#删除子弹
		for bullet in self.bullets.copy():
			if bullet.rect.bottom<=0:
				self.bullets.remove(bullet)
		collisons = pygame.sprite.groupcollide(
		self.bullets,self.aliens,True,True)

		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()

	def _create_fleet(self):
		alien=Alien(self)
		alien_width,alien_height=alien.rect.size
		avaliable_space_x=self.setting.screen_width-(2*alien_width)
		num_alien_x=avaliable_space_x//(2*alien_width)
		ship_height=self.ship.rect.height
		avaliable_space_y=(self.setting.screen_height-(3*alien_height)-ship_height)
		num_rows=avaliable_space_y//(2*alien_height)
		for row_num in range(num_rows):
			for alien_num in range(num_alien_x):
				self._create_alien(alien_num,row_num)

	def _create_alien(self,alien_num,row_num):
		alien=Alien(self)
		alien_width,alien_height=alien.rect.size
		alien.x=alien_width+2*alien_width*alien_num
		alien.rect.x=alien.x
		alien.rect.y=alien.rect.height+2*alien.rect.height*row_num
		self.aliens.add(alien)

	def _update_alien(self):
		self._check_fleet_edges()
		self.aliens.update()

	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges()==True:
				self._change_fleet_dirction()
				break

	def _change_fleet_dirction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.setting.fleet_drop_speed
		self.setting.fleet_dirction *= -1		

	def _screen(self):
		#每次循环都填充颜色
		self.screen.fill(self.setting.bg_color)
		#把飞船初始化在底部
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)	
		pygame.display.flip()

if __name__=='__main__':
	#创建游戏实例，并运行
	ai=AlienInvasion()
	ai.run_game()
