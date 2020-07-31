


import pygame 

done = 0


pygame.init()

Width = 558
Height = 418

screen = pygame.display.set_mode((Width,Height))

screen = pygame.display.set_mode((Width,Height))

ScreenImage = pygame.image.load("Iamges/Background Image.png")

screen.blit(ScreenImage,(0,0))


Lenght = int(input("Enter The Lenght OF the Rectangle:"))
Breadth = int(input("Enter The Breadth Of The Rectangle:"))
Area = Lenght * Breadth


font = pygame.font.SysFont("Comic Sans MS",50)
text=font.render("Lenght : "+str(Lenght),True,(0,0,0))
screen.blit(text,(30,0))
    
font = pygame.font.SysFont("Comic Sans MS",50)
text=font.render("Breadth : "+str(Breadth),True,(0,0,0))
screen.blit(text,(30,60))
    
font = pygame.font.SysFont("Comic Sans MS",60)
text=font.render("Area : "+str(Area),True,(0,0,0))
screen.blit(text,(100,200))
    
    
        
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
