from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
game_over = False

# This function changes the direction of the snake by modifying the aim vector based on the given x and y values
# It does not allow the snake to reverse its direction and ignores input during game over state
def change(x, y):
    "Change snake direction."
    if not game_over and (x, y) != (-aim.x, -aim.y):
        aim.x = x
        aim.y = y

# This function returns True if the given head vector is inside the boundaries of the game area 
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# This function moves the snake forward one segment by creating a new head vector based on the current head position and the aim vector,
# It also checks if the snake has hit a boundary or its own body, and ends the game if that's the case
# It updates the food location if the snake has reached it, and redraws the game screen based on the updated snake and food positions.
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        game_over = True
        score = len(snake)
        goto(0, -50)
        write(f"Game over! Score: {score}", align="center", font=("Courier", 24, "normal"))
        goto(0, -80)
        restart_button = Turtle()
        restart_button.hideturtle()
        restart_button.penup()
        restart_button.goto(0, -100)
        restart_button.write("Relaunch The Game To Play Again", align="center", font=("Courier", 16, "normal"))
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Draw boundaries
    square(-210, -210, 430, 'black')
    square(-200, -200, 400, 'white')

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)

# This function hides the turtle cursor (which is not needed for this game)
hideturtle()

# This function turns off the turtle drawing animation to make the game run faster
tracer(False)

# Draw boundaries
square(-210, -210, 430, 'black')
square(-200, -200, 400, 'white')

# This function sets up the turtle window to listen for keyboard events
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()

# This function enters the turtle event loop, allowing the game to respond to keyboard input and run the move function repeatedly
done()
