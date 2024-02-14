import random
import turtle

def setup_game():
    global wn, player, score, score_display, timer, timer_display

    # Set up the screen
    wn = turtle.Screen()
    wn.title("Click the Turtle Game")
    wn.bgcolor("#ffffff")

    # Create the turtle
    player = turtle.Turtle()
    player.shape("circle")
    player.color("green")
    player.shapesize(2)  # Set the turtle size to be larger
    player.penup()
    player.speed(0)
    player.goto(0, 0)

    # Display score
    score = 0
    score_display = turtle.Turtle()
    score_display.speed(0)
    score_display.color("black")
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(0, 260)
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Timer
    timer = 60
    timer_display = turtle.Turtle()
    timer_display.speed(0)
    timer_display.color("black")
    timer_display.penup()
    timer_display.hideturtle()
    timer_display.goto(0, -260)
    timer_display.write("Time left: {}".format(timer), align="center", font=("Courier", 24, "normal"))

    # Function to update the timer
    def update_timer():
        global timer
        timer -= 1
        timer_display.clear()
        timer_display.write("Time left: {}".format(timer), align="center", font=("Courier", 24, "normal"))
        if timer > 0:
            wn.ontimer(update_timer, 1000)
        else:
            player.hideturtle()
            score_display.clear()
            timer_display.clear()
            wn.update()
            play_again = wn.textinput("Play Again", "Do you want to play again? (yes/no)").lower()
            if play_again == "yes":
                setup_game()
            else:
                wn.bye()

    # Function to handle click on the turtle
    def click(x, y):
        global score
        if player.distance(x, y) < 20:
            player.goto(random.randint(-290, 290), random.randint(-290, 290))
            score += 1
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Bind click event
    wn.onclick(click)

    # Start the game
    update_timer()

    # Clear initial instructions
    score_display.clear()
    timer_display.clear()

    # Main loop
    turtle.done()

# Start the game initially
setup_game()
