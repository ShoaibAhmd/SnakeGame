import pygame, random, numpy as np
from os import path

pygame.init()
gameDisplay = pygame.display.set_mode((500,570))
gameDisplay.fill((52, 152, 219))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

moveSnakeEvent = pygame.USEREVENT + 1
pygame.time.set_timer(moveSnakeEvent, 100)

Slither = []
slitherLength = 0
dirX = 0
dirY = 0

def RenderText(textToRender, fontSize, posX, posY):
    basicfont = pygame.font.SysFont("calibri", fontSize, True)
    text = basicfont.render(textToRender, True, (255, 255, 255), (52, 152, 219))
    textrect = text.get_rect()
    textrect.centerx = posX
    textrect.centery = posY
    gameDisplay.blit(text, textrect)

def ShowHighScore():
    highScore = 0
    if path.isfile('highscore.txt'):
        fileObj = open('highscore.txt', 'r')
        highScore = fileObj.read()
        fileObj.close()        
    
    RenderText("High Score: {}".format(highScore), 20, 400, 535)

def UpdateHighScore():
    if path.isfile('highscore.txt'):
        fileObj = open('highscore.txt', 'r')
        highscore = fileObj.read()
        fileObj.close()
        if int(highscore) < slitherLength:
            fileObj = open('highscore.txt', 'w')
            fileObj.write(str(slitherLength))
            fileObj.close()
    else:
        fileObj = open('highscore.txt', 'w')
        fileObj.write(str(slitherLength))
        fileObj.close()

class Border:

    def __init__(self, posX, posY, length, width):
        self.posX = posX
        self.posY = posY
        self.length = length
        self.width = width
        self.borderRect = 0
        self.borderColor = 0
        self.showBorder = 0

    def ShowBorder(self):
        self.borderRect = pygame.Rect(self.posX, self.posY, self.width, self.length)
        self.color = (41, 128, 185)
        self.showBorder = pygame.draw.rect(gameDisplay, self.color, self.borderRect, 0)

class Food:

    def __init__(self):
        self.randomX = 0
        self.randomY = 0
        self.food = 0
        self.color = 0
        self.showFood = 0

    def ShowFood(self):
        self.food = pygame.Rect(self.randomX, self.randomY, 15, 15)
        self.color = (243, 156, 18)
        self.showFood = pygame.draw.ellipse(gameDisplay, self.color, self.food, 0)

    def GenerateFood(self):
        self.randomX = int(random.random() * 465)
        if self.randomX < 15:
            self.randomX += 15
        while (self.randomX % 15) != 0:
            self.randomX -= 1
            
        self.randomY = int(random.random() * 465)
        if self.randomY < 15:
            self.randomY += 15
        while (self.randomY % 15) != 0:
            self.randomY -= 1
            
        self.food = pygame.Rect(self.randomX, self.randomY, 15, 15)
        self.color = (243, 156, 18)
        self.showFood = pygame.draw.ellipse(gameDisplay, self.color, self.food, 0)

class Snake:
    
    def __init__(self):
        self.posX = 45
        self.posY = 45
        self.initial = pygame.Rect(self.posX, self.posY, 15, 15)
        self.color = (52, 152, 219)
        self.snake = pygame.draw.rect(gameDisplay, self.color, self.initial, 0)

    def moveSnake(self, X, Y):
        self.posX += X
        self.posY += Y
        self.initial.x = self.posX
        self.initial.y = self.posY
        self.color = (44, 62, 80)
        self.snake = pygame.draw.rect(gameDisplay, self.color, self.initial, 0)

    def showSnake(self):
        self.initial.x = self.posX
        self.initial.y = self.posY
        self.color = (44, 62, 80)
        self.snake = pygame.draw.rect(gameDisplay, self.color, self.initial, 0)

    def showSnakeOdd(self):
        self.initial.x = self.posX
        self.initial.y = self.posY
        self.color = (52, 73, 94)
        self.snake = pygame.draw.rect(gameDisplay, self.color, self.initial, 0)
    

leftBorder = Border(0,0,500,15)
rightBorder = Border(485,0,500,15)
topBorder = Border(0,0,15,500)
bottomBorder = Border(0,485,15,500)

flagGameOver = False
keyFlag = False
crashed = True

while crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = False
            
        elif event.type == pygame.VIDEOEXPOSE:
            foodObj = Food()
            foodObj.GenerateFood()
            Slither.append(Snake()) 

        elif event.type == pygame.KEYDOWN and keyFlag == False:
            keyFlag = True
            if event.key == pygame.K_DOWN:
                if dirY != -15:
                    dirX = 0
                    dirY = 15
            elif event.key == pygame.K_UP:
                if dirY != 15:
                    dirX = 0
                    dirY = -15
            elif event.key == pygame.K_LEFT:
                if dirX != 15:
                    dirX = -15
                    dirY = 0
            elif event.key == pygame.K_RIGHT:
                if dirX != -15:
                    dirX = 15
                    dirY = 0

        elif event.type == moveSnakeEvent:
            keyFlag = False
            gameDisplay.fill((52, 152, 219))
            if Slither[0].initial.colliderect(foodObj.food) == True:
                slitherLength += 1
                Slither.append(Snake())
                foodObj.GenerateFood()

            elif Slither[0].initial.colliderect(leftBorder.borderRect) == True or Slither[0].initial.colliderect(rightBorder.borderRect) == True or Slither[0].initial.colliderect(topBorder.borderRect) == True or Slither[0].initial.colliderect(bottomBorder.borderRect) == True:
                print("GAME OVER!! :P")
                dirX = 0
                dirY = 0
                crashed = False
                flagGameOver = True
                #break;

            if slitherLength >= 1:
                counter = 1
                while counter <= slitherLength:
                    if Slither[0].initial.colliderect(Slither[counter].initial) == True:
                        print("Slither Collision")
                        dirX = 0
                        dirY = 0
                        crashed = False
                        flagGameOver = True
                        break;
                    counter += 1
            
            foodObj.ShowFood()
            
            oldPosX = Slither[0].posX
            oldPosY = Slither[0].posY
            Slither[0].moveSnake(dirX, dirY)
            
            if slitherLength > 0:
                counter = slitherLength
                while counter >= 1:
                    if counter == 1:
                        Slither[counter].posX = oldPosX
                        Slither[counter].posY = oldPosY
                    else:
                        Slither[counter].posX = Slither[counter - 1].posX
                        Slither[counter].posY = Slither[counter - 1].posY

                    if counter % 2 == 1:
                        Slither[counter].showSnakeOdd()
                    else:
                        Slither[counter].showSnake()
                    counter -= 1

        RenderText('Score: {}'.format(slitherLength), 30, 100, 535)
        ShowHighScore()
        UpdateHighScore()                    
        leftBorder.ShowBorder()
        rightBorder.ShowBorder()
        topBorder.ShowBorder()
        bottomBorder.ShowBorder()
        print(event)

    pygame.display.update()
    #clock.tick(50)

if flagGameOver:
    while flagGameOver:
        for event in pygame.event.get():
            RenderText("Game Over!! :D", 60, gameDisplay.get_rect().centerx, gameDisplay.get_rect().centery - 40)
            print(event)
            if event.type == pygame.QUIT:
                flagGameOver = False
                
            elif event.type == pygame.KEYDOWN:
                flagGameOver = False

        pygame.display.update()

pygame.quit()
quit()
