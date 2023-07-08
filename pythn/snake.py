# Import required modules
from turtle import *
from random import randrange
from freegames import square, vector

# Set the initial position of the food and the snake
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Define a function to change the direction of the snake
def change(x, y):
    aim.x = x
    aim.y = y

# Define a function to check if the head of the snake is inside the boundaries
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

# Define the main function to move the snake
def move():
    head = snake[-1].copy()  # Make a copy of the head of the snake
    head.move(aim)  # Move the head in the current direction
    
    # Check if the head has hit the wall or the snake's body
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # Draw a red square to represent the dead snake
        update()  # Update the screen
        return  # End the game
    
    snake.append(head)  # Add the new head to the snake
    
    # Check if the snake has eaten the food
    if head == food:
        print('Snake:', len(snake))  # Print the length of the snake
        food.x = randrange(-15, 15) * 10  # Move the food to a new random position
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)  # Remove the tail of the snake
    
    clear()  # Clear the screen
    
    # Draw the snake and the food
    for body in snake:
        square(body.x, body.y, 9, 'black')  # Draw a black square for each body segment of the snake
    square(food.x, food.y, 9, 'green')  # Draw a green square to represent the food
    
    update()  # Update the screen
    ontimer(move, 100)  # Call this function again after 100ms

# Bind the arrow keys to the change function
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Set up the screen
setup(420, 420, 370, 0)
hideturtle()
tracer(False)

# Call the move function to start the game
move()

# Call the done function to finish the game
done()
