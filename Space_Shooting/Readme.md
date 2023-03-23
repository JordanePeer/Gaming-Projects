# Space Shooting


The code uses the Pygame library to create a two-player space shooting game. The game screen is set to a width of 900 pixels and a height of 500 pixels. 
The game's background, boundaries, spaceships, bullets, and sounds are defined. There are two spaceships, one controlled by the yellow player, 
and the other controlled by the red player.

The game has a constant frame rate of 60 FPS, and bullets can travel up to a maximum of 5 bullets at once, and their velocity is 6 pixels per frame. 
The game also has a "health bar" feature that displays each spaceship's health on the screen. The game screen is updated every time there is a change in the game state.

The player controls are as follows: for the yellow spaceship, the "A," "D," "W," and "S" keys are used to move the spaceship left, right, up, and down, respectively. 
For the red spaceship, the left, right, up, and down arrow keys are used to move it in the corresponding direction.

The function draw_window() is used to render the game's graphics, including the background, spaceships, bullets, and health bars. 
The handle_yellow_movement() function is used to handle the yellow spaceship's movement based on user input, 
and the handle_red_movement() function is used to handle the red spaceship's movement.

The function handle_bullets() is used to handle the movement of bullets and the detection of collisions between bullets and spaceships. 
If a bullet hits a spaceship, an event is posted, and the bullet is removed from the game. If a spaceship's health reaches zero, it is declared the loser of the game.

- When starting the game, a Game Panel will show up.

<img width="671" alt="image" src="https://user-images.githubusercontent.com/128277686/227311429-fd276e11-c1cc-44dd-adda-8546c3d021d3.png">


- Two players need to play, one will be the red spaceship and the second one will be the yellow spaceship

- the players will move their spaceship with the arrow and a,w,s,d keyboard, to shoot they will use the two ctrl keys.

<img width="667" alt="image" src="https://user-images.githubusercontent.com/128277686/227312022-03530cee-2f69-4ba7-95ac-1d1aae9d4573.png">

- When one of the players lost all their lives, a message will show up with the collor of the winner

<img width="662" alt="image" src="https://user-images.githubusercontent.com/128277686/227312203-aca786bb-0621-42cf-bc45-43ecc0cdfc9a.png">
