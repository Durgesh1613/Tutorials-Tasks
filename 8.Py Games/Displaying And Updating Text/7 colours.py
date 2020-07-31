import pygame 
import time

pygame.init()

Width = 558
Height = 418

screen = pygame.display.set_mode((Width,Height))

screen = pygame.display.set_mode((Width,Height))

ScreenImage = pygame.image.load("Iamges/Background Image.png")

screen.blit(ScreenImage,(0,0))


font = pygame.font.SysFont("Imapct",60)
text=font.render("Red",True,(0,0,0),(255,0,0))
screen.blit(text,(30,160))
time.sleep(10)
font = pygame.font.SysFont("Imapct",60)
text=font.render("Red",True,(0,0,0),(255,0,0))
screen.blit(text,(30,100))


EventStatus="None"


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

