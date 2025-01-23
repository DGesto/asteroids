###############
### MODULES ###
###############
import pygame
import constants
import player


#####################
### MAIN FUNCTION ###
#####################
def main():
    
    # Initiate pygame
    pygame.init()
    
    # Create a new GUI window
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    # Create a game clock
    clock = pygame.time.Clock()
    dt = 0 # time difference
    
    # Initiate Player Object
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    player1 = player.Player(x, y)
    
    # Game loop
    while True:
        # If close button is pressed, close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0, 0, 0)) # fills the window in black
        
        player1.draw(screen)
        player1.update(dt)
        
        pygame.display.flip() # Refreshes the screen
        dt = clock.tick(60) / 1000 # runs the game at 60 fps
        
    
    # print("Starting asteoids!")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIrGHT}")
    
   
###################
### ENTRY POINT ###
################### 
if __name__ == "__main__":
    main()