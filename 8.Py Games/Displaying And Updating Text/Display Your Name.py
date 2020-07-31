
"""
1. Display Your Name with following Text Properties:

       Font Name ="Impact"

       FontSize = 60

       FontColour ="Blue"
"""


import pygame 


pygame.init()

Width = 558
Height = 418

screen = pygame.display.set_mode((Width,Height))

screen = pygame.display.set_mode((Width,Height))

ScreenImage = pygame.image.load("Iamges/Background Image.png")

screen.blit(ScreenImage,(0,0))

font = pygame.font.SysFont("Imapct",60)
text=font.render("Durgesh Hemant Kavate",True,(51,51,255))
screen.blit(text,(30,160))




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