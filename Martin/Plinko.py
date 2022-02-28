from turtle import width
import pygame,sys,pymunk

def _add_static_scenery(self) -> None:
        """
        Create the static bodies.
        :return: None
        """
        window_w = pygame.display.Info().current_w
        window_h = pygame.display.Info().current_h
        static_body = self._space.static_body
        static_lines = [
            pymunk.Segment(static_body, (0, 0), (window_w, 0), 0.0),
            pymunk.Segment(static_body, (0, 0), (0, window_h), 0.0),
            pymunk.Segment(static_body, (window_w, 0), (window_w, window_h), 0.0),
            pymunk.Segment(static_body, (0, window_h), (window_w, window_h), 0.0),
        ]
        for line in static_lines:
            line.elasticity = 0.95
            line.friction = 0.9
        self._space.add(*static_lines)

def create_coin(space,pos):
    body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,30)
    space.add(body,shape)
    return shape

def draw_coins(coins):
    for coin in coins:
        pos_x = int(coin.body.position.x)
        pos_y = int(coin.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),30)
        coin_rect = coin_surface.get_rect(center = (pos_x,pos_y))
        screen.blit(coin_surface,coin_rect)

def static_ball(space,pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,15)
    space.add(body,shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(255,255,255),(pos_x,pos_y),15)

def static_wall(space,pos):
    
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,200)
    space.add(body,shape)
    return shape

def draw_static_wall():
    
    window_w = pygame.display.Info().current_w
    window_h = pygame.display.Info().current_h
    static_body = space.static_body
    static_lines = [
            pymunk.Segment(static_body, (0, 0), (window_w, 0), 0.0),
            pymunk.Segment(static_body, (0, 0), (0, window_h), 0.0),
            pymunk.Segment(static_body, (window_w, 0), (window_w, window_h), 0.0),
            pymunk.Segment(static_body, (0, window_h), (window_w, window_h), 0.0),
        ]
    for line in static_lines:
            line.elasticity = 0.95
            line.friction = 0.9
    space.add(*static_lines)
reset_b = False
def reset():
    pause = True
    reset_b = False
    for b in space.shapes:
        space.remove(b)
    draw_static_wall()
  
    draw_static_ball(balls)


pygame.init()

screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,150)
pygame.display.set_caption("2DPhysicsEducationTool- Plinko Gravity Simulation")
coins = []

coin_surface = pygame.image.load('img/coin.png')

balls = []
#plinko setup
#first row
balls.append(static_ball(space,(100,100)))
balls.append(static_ball(space,(200,100)))
balls.append(static_ball(space,(300,100)))
balls.append(static_ball(space,(400,100)))
balls.append(static_ball(space,(500,100)))
balls.append(static_ball(space,(600,100)))
balls.append(static_ball(space,(700,100)))
balls.append(static_ball(space,(800,100)))
balls.append(static_ball(space,(900,100)))

#second row
balls.append(static_ball(space,(30,175)))
balls.append(static_ball(space,(150,175)))
balls.append(static_ball(space,(250,175)))
balls.append(static_ball(space,(350,175)))
balls.append(static_ball(space,(450,175)))
balls.append(static_ball(space,(550,175)))
balls.append(static_ball(space,(650,175)))
balls.append(static_ball(space,(750,175)))
balls.append(static_ball(space,(850,175)))
balls.append(static_ball(space,(970,175)))

#3rd row
balls.append(static_ball(space,(100,250)))
balls.append(static_ball(space,(200,250)))
balls.append(static_ball(space,(300,250)))
balls.append(static_ball(space,(400,250)))
balls.append(static_ball(space,(500,250)))
balls.append(static_ball(space,(600,250)))
balls.append(static_ball(space,(700,250)))
balls.append(static_ball(space,(800,250)))
balls.append(static_ball(space,(900,250)))

#4th row
balls.append(static_ball(space,(30,325)))
balls.append(static_ball(space,(150,325)))
balls.append(static_ball(space,(250,325)))
balls.append(static_ball(space,(350,325)))
balls.append(static_ball(space,(450,325)))
balls.append(static_ball(space,(550,325)))
balls.append(static_ball(space,(650,325)))
balls.append(static_ball(space,(750,325)))
balls.append(static_ball(space,(850,325)))
balls.append(static_ball(space,(970,325)))
#5th row
balls.append(static_ball(space,(100,400)))
balls.append(static_ball(space,(200,400)))
balls.append(static_ball(space,(300,400)))
balls.append(static_ball(space,(400,400)))
balls.append(static_ball(space,(500,400)))
balls.append(static_ball(space,(600,400)))
balls.append(static_ball(space,(700,400)))
balls.append(static_ball(space,(800,400)))
balls.append(static_ball(space,(900,400)))

#6th row
balls.append(static_ball(space,(30,475)))
balls.append(static_ball(space,(150,475)))
balls.append(static_ball(space,(250,475)))
balls.append(static_ball(space,(350,475)))
balls.append(static_ball(space,(450,475)))
balls.append(static_ball(space,(550,475)))
balls.append(static_ball(space,(650,475)))
balls.append(static_ball(space,(750,475)))
balls.append(static_ball(space,(850,475)))
balls.append(static_ball(space,(970,475)))
#7th row
balls.append(static_ball(space,(100,550)))
balls.append(static_ball(space,(200,550)))
balls.append(static_ball(space,(300,550)))
balls.append(static_ball(space,(400,550)))
balls.append(static_ball(space,(500,550)))
balls.append(static_ball(space,(600,550)))
balls.append(static_ball(space,(700,550)))
balls.append(static_ball(space,(800,550)))
balls.append(static_ball(space,(900,550)))


draw_static_wall()
running = True
pause = True

physics_steps_per_frame = 1
dt = 1.0 / 60.0

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_b = True
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            coins.append(create_coin(space,event.pos))
        if not pause:
                for _ in range(physics_steps_per_frame):
                    space.step(dt)
        if reset_b:
            reset()
    screen.fill((0,150,255))
    draw_coins(coins)
    draw_static_ball(balls)
    
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)


