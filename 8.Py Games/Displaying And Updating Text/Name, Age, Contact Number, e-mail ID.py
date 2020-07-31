
"""
Take User Input as Name, Age, Contact Number, e-mail ID and Display them on Screen. Display each Input in following Format:

Name : ---------

Age:-----------

Contact No.: --------------------

e-mail ID:---------------------
"""


import pygame 

Name = input("Enter You Name:")
Age = int(input("Enter Your Age:"))
Contact_No = int(input("Enter Your Contact Number:"))
Email_ID = input("Enter Your Email ID:")


pygame.init()



Width = 558
Height = 418

screen = pygame.display.set_mode((Width,Height))



pygame.display.set_caption("User Information")


ScreenImage = pygame.image.load("Iamges/Background Image.png")

screen.blit(ScreenImage,(0,0))




font = pygame.font.SysFont("Comic Sans MS",20)
text=font.render("Your Name Is :"+str(Name),True,(0,0,0))
screen.blit(text,(30,0))

font = pygame.font.SysFont("Comic Sans MS",20)
text=font.render("Your Age Is :"+str(Age),True,(0,0,0))
screen.blit(text,(30,50))

font = pygame.font.SysFont("Comic Sans MS",20)
text=font.render("Your Contact No Is :"+str(Contact_No),True,(0,0,0))
screen.blit(text,(30,100))

font = pygame.font.SysFont("Comic Sans MS",20)
text=font.render("Your Email ID Is :"+str(Email_ID),True,(0,0,0))
screen.blit(text,(30,150))

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





