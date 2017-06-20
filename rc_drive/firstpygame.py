import pygame
import time,os
print "Go"
pygame.init()
# events = pygame.event.get()
print "Start"
pygame.key.set_repeat(50, 50)
i=0
while True:
	# print "True"
	for event in pygame.event.get():
		print "in loop"
		if event.type == pygame.QUIT:
		    pygame.quit()
		    sys.exit()
		t1=time.time()
		if event.type == pygame.KEYDOWN:
			t2=time.time()
			os.system('screencapture screenshot%s.jpg'%i)
			i+=1
			t3=time.time()
			print "in keydown"
			if event.key == pygame.K_DOWN:
				print "Down"
			if event.key == pygame.K_LEFT:
				print "Left"
			if event.key == pygame.K_RIGHT:
				print "Right"
			if event.key == pygame.K_UP:
				print "Up"
			t4=time.time()
			print "cap time %s"%(t3-t2)
			print "lab_time %s"%(t4-t2)
print "exit"