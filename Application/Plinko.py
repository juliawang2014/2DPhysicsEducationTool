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
    shape = pymunk.Circle(body,27)
    space.add(body,shape)
    return shape

def draw_coins(coins):
    for coin in coins:
        pos_x = int(coin.body.position.x)
        pos_y = int(coin.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),27)
        coin_rect = coin_surface.get_rect(center = (pos_x,pos_y))
        screen.blit(coin_surface,coin_rect)

def static_ball(space,pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,18)
    space.add(body,shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(255,255,255),(pos_x,pos_y),18)

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
    for c in coins:
        space.remove(c)
    coins.clear()
    return False


pygame.init()

screen = pygame.display.set_mode((1000,750))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,150)
pygame.display.set_caption("2DPhysicsEducationTool- Plinko Gravity Simulation")
coins = []

coin_surface = pygame.image.load('img/coin.png')

balls = []
#plinko setup
#first row
balls.append(static_ball(space,(100,140)))
balls.append(static_ball(space,(300,140)))
balls.append(static_ball(space,(400,140)))
balls.append(static_ball(space,(500,140)))
balls.append(static_ball(space,(600,140)))
balls.append(static_ball(space,(700,140)))
balls.append(static_ball(space,(900,140)))
#second row
balls.append(static_ball(space,(0,215)))
balls.append(static_ball(space,(200,215)))
balls.append(static_ball(space,(350,215)))
balls.append(static_ball(space,(450,215)))
balls.append(static_ball(space,(550,215)))
balls.append(static_ball(space,(650,215)))
balls.append(static_ball(space,(800,215)))
balls.append(static_ball(space,(1000,215)))
#3rd row
balls.append(static_ball(space,(100,290)))
balls.append(static_ball(space,(300,290)))
balls.append(static_ball(space,(400,290)))
balls.append(static_ball(space,(500,290)))
balls.append(static_ball(space,(600,290)))
balls.append(static_ball(space,(700,290)))
balls.append(static_ball(space,(900,290)))
#4th row
balls.append(static_ball(space,(0,365)))
balls.append(static_ball(space,(150,365)))
balls.append(static_ball(space,(250,365)))
balls.append(static_ball(space,(350,365)))
balls.append(static_ball(space,(450,365)))
balls.append(static_ball(space,(550,365)))
balls.append(static_ball(space,(650,365)))
balls.append(static_ball(space,(750,365)))
balls.append(static_ball(space,(850,365)))
balls.append(static_ball(space,(1000,365)))
#5th row
balls.append(static_ball(space,(75,440)))
balls.append(static_ball(space,(200,440)))
balls.append(static_ball(space,(300,440)))
balls.append(static_ball(space,(400,440)))
balls.append(static_ball(space,(500,440)))
balls.append(static_ball(space,(600,440)))
balls.append(static_ball(space,(700,440)))
balls.append(static_ball(space,(800,440)))
balls.append(static_ball(space,(925,440)))
#6th row
balls.append(static_ball(space,(0,515)))
balls.append(static_ball(space,(150,515)))
balls.append(static_ball(space,(250,515)))
balls.append(static_ball(space,(350,515)))
balls.append(static_ball(space,(450,515)))
balls.append(static_ball(space,(550,515)))
balls.append(static_ball(space,(650,515)))
balls.append(static_ball(space,(750,515)))
balls.append(static_ball(space,(850,515)))
balls.append(static_ball(space,(1000,515)))
#7th row
balls.append(static_ball(space,(100,590)))
balls.append(static_ball(space,(200,590)))
balls.append(static_ball(space,(300,590)))
balls.append(static_ball(space,(400,590)))
balls.append(static_ball(space,(500,590)))
balls.append(static_ball(space,(600,590)))
balls.append(static_ball(space,(700,590)))
balls.append(static_ball(space,(800,590)))
balls.append(static_ball(space,(900,590)))
#floor
balls.append(static_ball(space,(0,745)))
balls.append(static_ball(space,(175,745)))
balls.append(static_ball(space,(325,745)))
balls.append(static_ball(space,(450,745)))
balls.append(static_ball(space,(575,745)))
balls.append(static_ball(space,(725,745)))
balls.append(static_ball(space,(850,745)))
balls.append(static_ball(space,(1000,745)))
draw_static_wall()
running = True
pause = True

physics_steps_per_frame = 1
dt = 1.0 / 60.0


def draw_boundary():
    
    draw_static_ball(balls)

    draw_static_wall()
    pygame.display.update()
def draw_letters():
    Brown = (138,79,3) 
    Red = (255,0,0)
    Orange = (255,128,0)
    Yellow = (255,255,0)
    Green = (0,255,0)
    Blue = (0,225,225)
    Purple = (127,0,255)
    White = (255,255,255)



    font1 = pygame.font.Font("fonts/Xolonium-Regular.ttf", 35)
    font2 = pygame.font.Font("fonts/Xolonium-Regular.ttf", 16)
    text1 = font1.render('O', True, Brown)
    text2 = font1.render('A', True, Brown)
    text3 = font1.render('K', True, Brown)
    text4 = font1.render('L', True, Brown)
    text5 = font1.render('A', True, Brown)
    text6 = font1.render('N', True, Brown)
    text7 = font1.render('D', True, Brown)

    text8 = font1.render('P', True, Red)
    text9 = font1.render('L', True, Orange)
    text10 = font1.render('I', True, Yellow)
    text11 = font1.render('N', True, Green)
    text12 = font1.render('K', True, Blue)
    text13 = font1.render('O', True, Purple)
    text14 = font2.render('Click to spawn coin. Click "r" on keyboard to remove coins', True, White)

    screen.blit(text1,(90,700))
    screen.blit(text2,(225,700))
    screen.blit(text3,(375,700))
    screen.blit(text4,(500,700))
    screen.blit(text5,(625,700))
    screen.blit(text6,(775,700))
    screen.blit(text7,(900,700))

    screen.blit(text8,(375,0))
    screen.blit(text9,(430,0))
    screen.blit(text10,(490,0))
    screen.blit(text11,(530,0))
    screen.blit(text12,(585,0))
    screen.blit(text13,(630,0))
    screen.blit(text14,(275,40))

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
            reset_b = reset()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            reset_b = False
            draw_boundary()
            
    screen.fill((0,150,255))
    draw_coins(coins)
    draw_static_ball(balls)
    draw_letters()
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)


