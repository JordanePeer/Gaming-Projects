from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
game_over = False

def change(x, y):
    "Change snake direction."
    if not game_over and (x, y) != (-aim.x, -aim.y):
        aim.x = x
        aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

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

hideturtle()
tracer(False)

# Draw boundaries
square(-210, -210, 430, 'black')
square(-200, -200, 400, 'white')

listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
