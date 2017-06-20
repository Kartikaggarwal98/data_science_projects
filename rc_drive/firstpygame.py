import pygame
print "Go"
pygame.init()
# events = pygame.event.get()
print "Start"
pygame.key.set_repeat(50, 50)

while True:
	# print "True"
	for event in pygame.event.get():
		print "in loop"
		if event.type == pygame.QUIT:
		    pygame.quit()
		    sys.exit()
		if event.type == pygame.KEYDOWN:
			print "in keydown"
			if event.key == pygame.K_DOWN:
				print "Down"
			if event.key == pygame.K_LEFT:
				print "Left"
			if event.key == pygame.K_RIGHT:
				print "Right"
			if event.key == pygame.K_UP:
				print "Up"
print "exit"