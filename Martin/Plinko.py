from turtle import width
import pygame,sys,pymunk

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

def draw_static_wall(walls):
    for wall in walls:
        pos_x = int(wall.body.position.x)
        pos_y = int(wall.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),200)
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




walls = []
#walls left side
walls.append(static_wall(space,(-190,0)))
walls.append(static_wall(space,(-190,50)))
walls.append(static_wall(space,(-190,100)))
walls.append(static_wall(space,(-190,150)))
walls.append(static_wall(space,(-190,200)))
walls.append(static_wall(space,(-190,250)))
walls.append(static_wall(space,(-190,300)))
walls.append(static_wall(space,(-190,350)))
walls.append(static_wall(space,(-190,400)))
walls.append(static_wall(space,(-190,450)))
walls.append(static_wall(space,(-190,500)))
walls.append(static_wall(space,(-190,550)))
walls.append(static_wall(space,(-190,600)))


#walls right side
walls.append(static_wall(space,(1190,0)))
walls.append(static_wall(space,(1190,50)))
walls.append(static_wall(space,(1190,100)))
walls.append(static_wall(space,(1190,150)))
walls.append(static_wall(space,(1190,200)))
walls.append(static_wall(space,(1190,250)))
walls.append(static_wall(space,(1190,300)))
walls.append(static_wall(space,(1190,350)))
walls.append(static_wall(space,(1190,400)))
walls.append(static_wall(space,(1190,450)))
walls.append(static_wall(space,(1190,500)))
walls.append(static_wall(space,(1190,550)))
walls.append(static_wall(space,(1190,600)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            coins.append(create_coin(space,event.pos))
    screen.fill((0,150,255))
    draw_coins(coins)
    draw_static_ball(balls)
    draw_static_wall(walls)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)


