import pygame
import random
import math

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

# ---constantes
BLOCK_SIZE=20

SPEED=1

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
        self.body=[368,367,366]
        self.direction='RIGHT'
        self.food=None
        self.placeFood()

    def placeFood(self):
        x=random.randint(1,32)
        y=random.randint(0,24)
        foodPosition=32*x+y
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
        game_over=False
        if self.collision():
            game_over=True
#4 place new food or just move
        # self.placeFood()
#5 update ui and clock
        self.updateUi()
        self.clock.tick(SPEED)

#6 return game over and score
        
        return game_over,self.score

    def collision(self):
        #hit the boundary
            #border du haut
        if self.body[0]<1:
            return True
            #border du bas
        if self.body[0]>768:
            return True
            #border du droite et gauche
        # rowFirstBodyPart=math.floor(self.body[0]/32)
        # if self.body[0]%32==0:
        #     rowFirstBodyPart-=1

        firstCol=[1,33,65,97,129,161,193,225,257,289,321,353,385,417,449,481,513,545,577,609,641,673,705,737]
        lastCol=[32,64,96,128,160,192,224,256,288,320,352,384,416,448,480,512,544,576,608,640,672,704,736,768]
        isFirstBodyPartFirstCol=False
        isFirstBodyPartLastCol=False
        if self.body[0] in firstCol:
            isFirstBodyPartFirstCol=True
        if self.body[0] in lastCol:
            isFirstBodyPartLastCol=True

        # rowSecondBodyPart=math.floor(self.body[1]/32)
        # if self.body[1]%32==0:
        #     rowSecondBodyPart-=1

        isSecondBodyPartFirstCol=False
        isSecondBodyPartLastCol=False
        if self.body[1] in firstCol:
            isSecondBodyPartFirstCol=True
        if self.body[1] in lastCol:
            isSecondBodyPartLastCol=True

        # notTheSameRow= rowFirstBodyPart != rowSecondBodyPart
        notTheSameCol=False
        if isSecondBodyPartLastCol==True and isSecondBodyPartLastCol==True:
            notTheSameCol=True

        if isFirstBodyPartFirstCol==True and isFirstBodyPartLastCol==True:
            notTheSameCol=True

        print('hello',notTheSameCol)
        if notTheSameCol:
            return True

        #hit itself
        if self.body[0] in self.body[1:]:
            return True
        return False

    def move(self):
        direction=self.direction
        body=self.body.copy()
        if direction=='RIGHT':
            body[0]=body[0]+1
        if direction=='LEFT':
            body[0]=body[0]-1
        if direction=='UP':
            body[0]=body[0]-32
        if direction=='DOWN':
            body[0]=body[0]+32

        for index, bodyPart in enumerate(self.body):
            if index != 0:
                body[index]=self.body[index-1]
        self.body=body

    def updateUi(self):
        self.display.fill(WHITE)
        for point in self.body:
            row=math.floor(point/32)
            if point%32==0:
                row-=1
            xPosition=(point-row*32-1)*BLOCK_SIZE
            yPosition=row*BLOCK_SIZE
            pygame.draw.rect(self.display,BLUE1,pygame.Rect(xPosition,yPosition,BLOCK_SIZE,BLOCK_SIZE))
            pygame.draw.rect(self.display,BLUE2,pygame.Rect(xPosition+4,yPosition+4,12,12))

        rowFood=math.floor(self.food/32)
        if self.food%32==0:
            rowFood-=1
        xPositionFood=(self.food-rowFood*32-1)*BLOCK_SIZE
        yPositionFood=rowFood*BLOCK_SIZE

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
