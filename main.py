import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
		player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
		self.jump_sound.set_volume(0.5)

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
			self.gravity = -20
			self.jump_sound.play()

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def animation_state(self):
		if self.rect.bottom < 300: 
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk):self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		
		if type == 'fly':
			fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
			fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
			self.frames = [fly_1,fly_2]
			y_pos = 210
		else:
			snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
			snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
			self.frames = [snail_1,snail_2]
			y_pos  = 300

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

	def animation_state(self):
		self.animation_index += 0.1 
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()
		self.rect.x -= 6
		self.destroy()

	def destroy(self):
		if self.rect.x <= -100: 
			self.kill()

def display_highscore():
	with open("highscore.txt") as hs:
		hiscore = hs.read()
	
	highscore_surf = test_font.render(f'Highscore: {hiscore}',False,(64,64,64))
	highscore_rect = highscore_surf.get_rect(center = (680,30))
	screen.blit(highscore_surf,highscore_rect)
	return hiscore

def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time

def red_lives():
	global lives,loss_music
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		lives -= 1
		loss_music.play(loops=1)
		obstacle_group.empty()
	return True

def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	else: return True


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1)
bg_music.set_volume(0.8)
loss_music = pygame.mixer.Sound('audio/loss.wav')
hs_music = pygame.mixer.Sound('audio/break.mp3')
hs_music.set_volume(1.0)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

#setting highscore from file
with open("highscore.txt") as hs:
	new_highscore = hs.read()

# Set lives to three everytime the game opens
lives = 3

# To stop music after breaking highscore
flag = 0

#hearts
heart_surface = pygame.image.load('graphics/heart.png').convert_alpha()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
		
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)


	if game_active:
		screen.blit(sky_surface,(0,0))
		screen.blit(ground_surface,(0,300))
		score = display_score()
		highscore = display_highscore()
		
		player.draw(screen)
		player.update()

		obstacle_group.draw(screen)
		obstacle_group.update()

		game_active = red_lives()

		if lives<=0 :
			game_active = False
			flag = 0
			lives = 3

		# to display lives graphically
		for i in range(lives):
			heart_rect = heart_surface.get_rect(center = (20+(32*i),30))
			screen.blit(heart_surface,heart_rect)

		# to update highscore
		if score>int(highscore):
			new_highscore = str(score)
			flag += 1
			# print(flag)
			if flag == 1:hs_music.play()
		else:
			new_highscore = highscore
		
	else:
		screen.fill((94,129,162))
		screen.blit(player_stand,player_stand_rect)
		with open("highscore.txt","w") as hs:
			hs.write(new_highscore)
		score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
		score_message_rect = score_message.get_rect(center = (400,330))
		highscore_message = test_font.render(f'Highscore: {new_highscore}',False,(204,255,255))
		highscore_message_rect = highscore_message.get_rect(center = (400,360))
		screen.blit(game_name,game_name_rect)
		flag = 0
		if score == 0: screen.blit(game_message,game_message_rect)
		else: 
			screen.blit(score_message,score_message_rect)
			screen.blit(highscore_message,highscore_message_rect)

	pygame.display.update()
	clock.tick(60)