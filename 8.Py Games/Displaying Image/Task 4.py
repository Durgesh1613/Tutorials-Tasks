
print ("OUR TASK IS:")
print(" ")
print ("Create a window with size 1000x800 dimension and display image at x=80,y=200 coordinates. Image Size is 320x240.")
print(" ")

import pygame

pygame.init()

Width = 1000
Height = 800

screen = pygame.display.set_mode((Width,Height))

pygame.display.set_caption("Juicy Fruits")

screenImg = pygame.image.load("Images/Fruits 320x240.jpg")

screen.blit(screenImg,(80,200))

EventStatus = "None"

while True:
    
           
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            EventStatus="Quit"
            break
        
    if EventStatus == "Quit":
        break
    
print("Closing")
    
    
            