import pygame
import random


# pipe head
class pipeHead(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.pipe_head = pygame.image.load("./resources/images/pipe_head.png")
		self.img = self.pipe_head
		self.rect = self.pipe_head.get_rect()
		self.height = self.pipe_head.get_height()
		self.width = self.pipe_head.get_width()


# pipe body
class pipeBody(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.pipe_body = pygame.image.load("./resources/images/pipe_body.png")
		self.img = self.pipe_body
		self.rect = self.pipe_body.get_rect()
		self.height = self.pipe_body.get_height()
		self.width = self.pipe_body.get_width()


# pipe kinds
class Pipe():
	def __init__(self, HEIGHT, WIDTH):
		# Game interface height and width
		self.HEIGHT = HEIGHT
		self.WIDTH = WIDTH
		# maximum pipe body
		self.max_pipe_body = (self.HEIGHT - 2 * pipeHead().height) // pipeBody().height
		# space(For bird pass，pipeBody().height as unit distance)
		self.interspace = 8
		# upper pipe body
		self.n_up_pipe_body = random.randint(0, self.max_pipe_body-self.interspace)
		# bottom pipe body
		self.n_down_pipe_body = self.max_pipe_body - self.interspace - self.n_up_pipe_body
		# position
		self.x = 600
		# speed(bird movement speed)
		self.speed = 100
		# change to true after bird pass the pipe，prevent bug
		self.add_score = False
		self.construct_pipe()
	# construct pipe with pipe head and pipe body
	def construct_pipe(self):
		# pipe
		self.pipe = pygame.sprite.Group()
		# upper half part
		for i in range(self.n_up_pipe_body):
			pipe_body = pipeBody()
			pipe_body.rect.left, pipe_body.rect.top = self.x, i * pipe_body.height
			self.pipe.add(pipe_body)
		pipe_head = pipeHead()
		pipe_head.rect.left, pipe_head.rect.top = self.x - (pipeHead().width - pipeBody().width) / 2, self.n_up_pipe_body * pipeBody().height
		self.pipe.add(pipe_head)
		# bottom half part
		for i in range(self.n_down_pipe_body):
			pipe_body = pipeBody()
			pipe_body.rect.left, pipe_body.rect.top = self.x, self.HEIGHT - (i + 1) * pipeBody().height
			self.pipe.add(pipe_body)
		pipe_head = pipeHead()
		pipe_head.rect.left, pipe_head.rect.top = self.x - (pipeHead().width - pipeBody().width) / 2, self.HEIGHT - self.n_down_pipe_body * pipeBody().height - pipeHead().height
		self.pipe.add(pipe_head)
	# update pipe
	def update(self, time_passed):
		self.x -= time_passed * self.speed
		self.construct_pipe()
