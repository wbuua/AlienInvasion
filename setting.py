class Settings:
	'''储存所有的设置。。。'''
	def __init__(self):
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(230,230,230)
		self.fleet_drop_speed=0.5
		self.fleet_dirction=1
		self.alien_speed=0.2
		self.bullets_allowed=3

	def change_width(self):
		new_width=input('Enter width:\n')
		i=int(new_width)
		self.screen_width=i

	def change_height(self):
		new_height=input('Enter height:\n')
		i=int(new_height)
		self.screen_height=new_height

	def change_bg(self):
		new_bg=input('Enter bg_color:\n')
		i=int(new_bg)
		self.bg_color=new_bg