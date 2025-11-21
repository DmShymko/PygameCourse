import pygame

#Initialize pygame
pygame.init()

#Create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
surface_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding sounds!")

#Load the sounds effects
sound_1 = pygame.mixer.Sound("resources/sounds/sound_1.wav")
sound_2 = pygame.mixer.Sound("resources/sounds/sound_2.wav")



#Play the sounds effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

#Change the volume of a sound effect
sound_2.set_volume(.1)
sound_2.play()

#Load background music
pygame.mixer.music.load("resources/sounds/music.wav")

#Play and stop the music
pygame.mixer.music.play(-1, .0)
pygame.time.delay(5000)
pygame.mixer.music.stop()

#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update surface
    pygame.display.update()

#End the game
pygame.quit()