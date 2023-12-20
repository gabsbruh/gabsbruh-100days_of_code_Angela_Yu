VS_CPU = False # control of the right paddle - by a second player or automatically
PADDLE_HEIGHT = 150 # how long paddle is
SCREEN_WIDTH = 1200 # width of the game screen
SCREEN_HEIGHT = 900 # height of the game screen
BALL_SPEED = 7 # turtle.forward on each tick
BALL_LIMIT = (SCREEN_WIDTH/2)-5 # ball furthest xcor position
PADDLE_COLLISION_LIMIT = (SCREEN_WIDTH/2)-65 # position of collisio
WALL_COLLISION_LIMIT = (SCREEN_HEIGHT/2)-20 # position of ball when collide with the wall
PADDLE_RANGE = PADDLE_HEIGHT/2 # when paddle detects touch with the ball, maximum range
FINAL_SCORE = 2 # score which defines the winner
WRITE_SCORE_LEFT = (-100, (SCREEN_HEIGHT/2)-90) # place to write the left score
WRITE_SCORE_RIGHT = (100, (SCREEN_HEIGHT/2)-90) # place to write the right score
WRITING_OPTIONS = ('center', ('arial', 60, 'normal')) # font settings to write score
ENDGAME_WRITING_OPTIONS = ('center', ('arial', 30, 'normal')) # font settings to write final score