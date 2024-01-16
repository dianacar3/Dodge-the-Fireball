
# Dodge the Fireball

My project is a simple game that consists of an "Ice Block" that dodges the "Fireball" by moving left or right using the arrow keys. The Fireball will randomly move and bounce off the walls. The user will have 3 “lives”. Meaning if the Ice Block is hit 3 times, then the user will lose, and the screen will showcase “GAME OVER”. The user will be able to play as long as they want until they decide to exit the game. To continue the game the user simply presses the "enter" key.
## Operating Instructions
Prerequisites
- Install Python with the link
    [Python.org](https://www.python.org/downloads/)
- Install Pygame using your computer's command prompt ('pip install pygame')
    - Click the link for instructions on installing
        [Pygame](https://www.geeksforgeeks.org/install-pygame-in-macos/?ref=lbp)

Running the Game
- Download and save the the game onto your computer
- Once you click on the the game, it should run
- Use the left and right arrow keys to move the Ice Block
- Press the enter key to restart the game after losing

Game Controls
- Arrow keys: Move Ice Block
- Enter key: Restart game

## Flowchart

![](https://imgur.com/cnjpYpO.png)


## Pseudocode

```python
##############################   Project Pseudocode   #################################
# Name: Diana Cardona
#
# Purpose: Simulates a dodging game
#
# Algorithm:
#
#    Start
#        from turtle import speed
#        import pygame
#        import sys
#        import random
#
#        Initialize Pygame
#
#        Set up constants
# 
#        Create the screen
#
#        Make a variable for clock
#
#        Make a class for Ball
#            Make Variables
#            Define a draw statement for Ball
#            Define a random movement for Ball
#	Define position for Ball
#
#        Make a class for Fireball
#            Empty balls list
#            Define a start function for Fireball
#            Define a draw statement for Fireball
#            Define a random movement for Fireball
#	Define a reset function for Fireball
#            
#        Make a class for Iceblock
#            Make Variables
#            Define a draw statement for Iceblock
#            Define movements for Iceblock (to move left and right with arrow keys)
#	Define a collision function for Iceblock
#
#        Create a function for fireball object
#        Call to start the fireball
#        Create a function for iceblock object
#
#        Create a Game Loop
#        While True
#            Display Screen
#
#            For loop (event in pygame)
#                If event == QUIT
#                    Quit game
#                    System Exit
#	    elif KEYDOWN:
#	        if ENTER key pressed:
#	            lives = 3
#	            restart the fireball
#
#            Call the fireball draw function
#            Call the fireball movement function
#            Call the iceblock draw function
#            Call the iceblock movement function
#	
#	if collision occurs:
#	    Lose a life
#	    Reset the fireball
#	if lives == 0:
#	    Display “Game Over”
#	    Reset fireball
#	    Display restart message
#
#            Set the clock tick speed
#
#    End
