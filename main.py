###############
### MODULES ###
###############
import pygame
# Imports the game constants from the constants.py file
import constants


#####################
### MAIN FUNCTION ###
#####################
def main():
    
    # Initiate pygame
    pygame.init()
    
    # Create a new GUI window
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    # Game loop
    while True:
        # If close button is pressed, close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0, 0, 0)) # fills the window in black
        pygame.display.flip() # Refreshes the screen
        
    
    # print("Starting asteoids!")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIrGHT}")
    
   
###################
### ENTRY POINT ###
################### 
if __name__ == "__main__":
    main()