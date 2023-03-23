# Space Flying

The given code is a Python script for a 2D game called "Space Fly". It uses the Pygame library to create and display game objects on a window.

The code begins by importing the necessary libraries - pygame, os, time, and random. It then initializes the Pygame font and mixer modules.

Next, it defines the game window's dimensions, background, and caption, as well as the font size and frame rate. It also sets the music and sound effects for the game,
and defines their volume levels.

After that, it defines the design and characteristics of the spaceship and stars, including their width, height, velocity, and image. 
It also defines the user event when the spaceship is hit by a star.

Then, it defines the draw_window() function to draw the game window, including the background, the elapsed time, player's health, and the spaceship and stars' positions.

It also defines the handle_player_movement() function to move the spaceship in response to keyboard input.

The handle_stars() function is defined to handle the stars' movement and collision detection with the spaceship.

The main() function is the game's main loop that keeps running until the player loses all health points. The loop updates the elapsed time, adds stars to the game, 
handles user input, and updates the game window using the draw_window() function.

Finally, it starts the game by calling the main() function if the script is run directly.

- The game start with the display of the backround of space, a red spaceship as the player, the health count, and the time counting:

<img width="744" alt="image" src="https://user-images.githubusercontent.com/128277686/227304602-91384604-0f03-41d4-b0ed-1540399e8f05.png">


- Then meteorits are starting to fall down, the spaceship can move in all 4 directions.

<img width="737" alt="image" src="https://user-images.githubusercontent.com/128277686/227304904-580bdcfc-a9e0-48ee-a689-1a64ed3435e2.png">


- When you loose all your lifes a message will pop up saying " You Lost"

<img width="739" alt="image" src="https://user-images.githubusercontent.com/128277686/227305220-ca26ec15-dc79-4074-bc0b-a4be22ef6cfb.png">
