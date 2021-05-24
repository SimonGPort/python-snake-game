import pygame
import random

pygame.init()

BLOCK_SIZE=20

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
        self.body=[492]
        self.food=None
        self.directino='RIGHT'

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

#2 move

#3 check if game over

#4 place new food or just move

#5 update ui and clock
# //

#6 return game over and score
        game_over=false
        return game_over,self.score


if __name__=='__main__':
    game=SnakeGame()

    while True:
        game_over,score=game.play_step()
        if game_over==True:
            break

    pygame.quit()
