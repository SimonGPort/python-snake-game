import pygame
import random
import math

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

# ---constantes
BLOCK_SIZE=20

SPEED=10

# rgb colors
WHITE=(255,255,255)
RED=(200,0,0)
BLUE1=(0,0,255)
BLUE2=(0,100,255)
BLACK=(0,0,0)



class SnakeGame:
    def __init__(self,w=640,h=480):
        self.w=w
        self.h=h
        self.display=pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption("Snake")
        self.clock=pygame.time.Clock()

        # init game state
        self.score=0
        # l'array des lives represente la position de chanque morceau du corps, a l'index 0 il y a la tete
        self.body=[280,279,278]
        self.direction='RIGHT'
        self.food=None
        self.placeFood()

    def placeFood(self):
        x=random.randint(1,32)
        y=random.randint(1,24)
        foodPosition=24*y+x
        if foodPosition in self.body:
            self.placeFood
        else:
            self.food=foodPosition

    def play_step(self):
#1 collect user input
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.direction='LEFT'
                if event.key==pygame.K_RIGHT:
                    self.direction='RIGHT'
                if event.key==pygame.K_UP:
                    self.direction='UP'
                if event.key==pygame.K_DOWN:
                    self.direction='DOWN'

#2 move
        self.move()
#3 check if game over

#4 place new food or just move
        # self.placeFood()
#5 update ui and clock
        self.updateUi()
        self.clock.tick(SPEED)

#6 return game over and score
        game_over=False
        return game_over,self.score

    def move(self):
        direction=self.direction
        body=self.body.copy()
        print('old body:',body)
        print('direction:',direction)
        if direction=='RIGHT':
            print('body1:',body[0],body[0]+1)
            body[0]=body[0]+1
            print('body2:',body[0],body[0]+1)
        if direction=='LEFT':
            body[0]=body[0]-1
        if direction=='UP':
            body[0]=body[0]-24
        if direction=='DOWN':
            body[0]=body[0]+24
        print('new body:',body)

        for index, bodyPart in enumerate(self.body):
            if index != 0:
                body[index]=self.body[index-1]
        self.body=body

    def updateUi(self):
        self.display.fill(WHITE)
        for point in self.body:
            xPosition=((point-math.floor(point/24)*24)-1)*BLOCK_SIZE
            yPosition=math.floor(point/24)*BLOCK_SIZE
            pygame.draw.rect(self.display,BLUE1,pygame.Rect(xPosition,yPosition,BLOCK_SIZE,BLOCK_SIZE))
            pygame.draw.rect(self.display,BLUE2,pygame.Rect(xPosition+4,yPosition+4,12,12))

        xPositionFood=((self.food-math.floor(self.food/24)*24)-1)*BLOCK_SIZE
        yPositionFood=math.floor(self.food/24)*BLOCK_SIZE
        pygame.draw.rect(self.display,RED,pygame.Rect(xPositionFood,yPositionFood,BLOCK_SIZE,BLOCK_SIZE))

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.update()

if __name__=='__main__':
    game=SnakeGame()

    while True:
        game_over,score=game.play_step()
        if game_over==True:
            break

    pygame.quit()
