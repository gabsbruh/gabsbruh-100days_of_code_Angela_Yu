from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import constants as c
import time
from score import Score

def main():
    # screen setup
    screen = Screen()
    screen.title('Pong Game')
    screen.setup(width=c.SCREEN_WIDTH, height=c.SCREEN_HEIGHT)
    screen.bgcolor('black')
    screen.tracer(0)  # automatic update of animations are turned off
    # paddle creator
    right_paddle = Paddle()
    right_paddle.position('right')
    left_paddle = Paddle()
    left_paddle.position('left')
    
    # add ball
    ball = Ball()
    
    # add score
    score = Score()
    
    # TODO zmien tak aby po jednym kliknieciu caly czas szlo w dol,
    # nie trzeba wtedy bedzie robic przyciskow jednoczesnych 

    
    screen.listen()
    if c.VS_CPU:
        x = screen.onkeypress(left_paddle.up, "Up")
        screen.onkeypress(left_paddle.down, "Down")
        screen.onkeypress(left_paddle.up, "w")
        screen.onkeypress(left_paddle.down, "s")   
    else:
        screen.onkeypress(left_paddle.up, "w")
        screen.onkeypress(left_paddle.down, "s")            
        screen.onkeypress(right_paddle.up, "Up")
        screen.onkeypress(right_paddle.down, "Down")     
    

    # proper game
    game_on = True
    while game_on:
        screen.update()
        ball.move()
        time.sleep(ball.move_speed)
        if (score.score['left'] == c.FINAL_SCORE) or (score.score['right'] == c.FINAL_SCORE):
            ball.ht()
            score.endgame_statement()
            game_on = False
        # detect collision with wall
        if ball.ycor() >= c.WALL_COLLISION_LIMIT or ball.ycor() <= -c.WALL_COLLISION_LIMIT:
            ball.bounce_wall()
            
        # detect collision with paddle    
        if ((ball.xcor() > c.PADDLE_COLLISION_LIMIT and ball.distance(right_paddle) < c.PADDLE_RANGE) or
            (ball.xcor() < -c.PADDLE_COLLISION_LIMIT and ball.distance(left_paddle) < c.PADDLE_RANGE)):
            ball.bounce_paddle()
        
        #score_up, refresh the game
        if ball.xcor() >= c.BALL_LIMIT:
            score.left_score_up()
            time.sleep(1)
            ball.reset()
            score.update()
            
        elif ball.xcor() <= -c.BALL_LIMIT:
            score.right_score_up()
            time.sleep(1)
            ball.reset()
            score.update()
            

        
        
    screen.exitonclick()
    
    
    

if __name__ == "__main__":
    main()