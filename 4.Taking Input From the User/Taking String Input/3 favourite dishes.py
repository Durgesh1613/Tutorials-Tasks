
"""
Take input from the user about their 3 favourite dishes and display the dishes on screen
"""


dish1 = "Gulab Jamun"
dish2 = "Pav Bhaji"
dish3 = "Pani Puri"
import pygame

pygame.init()

Width = 1000
Height = 500

screen = pygame.display.set_mode((Width,Height))

pygame.display.set_caption("Dishes")

screenImg = pygame.image.load("Images/Pav Bhaji.png")

screen.blit(screenImg,(0,0))

screenImg = pygame.image.load("Images/PaniPuri.png")

screen.blit(screenImg,(0,200))

screenImg = pygame.image.load("Images/Gulab Jamun.png")

screen.blit(screenImg,(400,200))

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
    
    
            