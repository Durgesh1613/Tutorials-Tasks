
print ("OUR TASK IS:")
print(" ")
print ("Create a window with size 800x600 dimension and display image at x=50,y=10 coordinates. Image Size is 800x600.")
print(" ")

import pygame

pygame.init()

Width = 800
Height = 600

screen = pygame.display.set_mode((Width,Height))

pygame.display.set_caption("Juicy Fruits")

screenImg = pygame.image.load("Images/Fruits800x600.jpg")

screen.blit(screenImg,(50,10))

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
    
    
            