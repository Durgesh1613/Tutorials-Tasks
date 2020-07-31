import pygame 
import rotateImage as rotator
import time

pygame.init()

Width = 1000
Height = 1000


screen = pygame.display.set_mode((Width,Height))



pygame.display.set_caption("User Information")


Image = pygame.image.load("Images/Stepper Motor Symbol 2.png")



EventStatus="None"
angle=5


while True:
             
    
    
   
    pygame.display.update()
    angle = angle-20
    rotator.blitRotate(screen,Image,(200,100),angle)
    time.sleep(1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            EventStatus="Quit"
            break
       
        
    if EventStatus == "Quit":
        break
    
print("Closing")
