
print ("OUR TASK IS:")
print(" ")
print ("Create a Window of 500 x 500 dimension and display image of size 500x500 in it. (Download the any image with 320x240 size)")
print(" ")

import pygame

pygame.init()

Width = 500
Height = 500

screen = pygame.display.set_mode((Width,Height))

pygame.display.set_caption("Juicy Fruits")

screenImg = pygame.image.load("Images/Fruits 320x240.jpg")

screen.blit(screenImg,(0,0))

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
    
    
            