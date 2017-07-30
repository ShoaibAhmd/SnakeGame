import pygame, random, numpy as np

pygame.init()
gameDisplay = pygame.display.set_mode((500,500))
gameDisplay.fill((0,0,0))
pygame.display.set_caption("Saanp Wali Game")
clock = pygame.time.Clock()

class Food:

    def __init__(self):
        self.randomX = 0
        self.randomY = 0
        self.food = 0
        self.color = 0
        self.showFood = 0

    def ShowFood(self):
        self.food = pygame.Rect(self.randomX, self.randomY, 15, 15)
        self.color = (0,255,0)
        self.showFood = pygame.draw.rect(gameDisplay, self.color, self.food, 0)

    def GenerateFood(self):
        self.randomX = int(random.random() * 480)
        while (self.randomX % 15) != 0:
            self.randomX -= 1
        self.randomY = int(random.random() * 480)
        while (self.randomY % 15) != 0:
            self.randomY -= 1
        self.food = pygame.Rect(self.randomX, self.randomY, 15, 15)
        self.color = (0,255,0)
        self.showFood = pygame.draw.rect(gameDisplay, self.color, self.food, 0)

class Snake:
    
    def __init__(self):
        self.posX = 45
        self.posY = 45
        self.initial = pygame.Rect(self.posX, self.posY, 15, 15)
        self.color = (100,100,100)
        self.snake = pygame.draw.rect(gameDisplay, self.color, self.initial, 0)
        

    def moveSnake(self, X, Y):
        self.posX += X
        self.posY += Y
        self.initial.x = self.posX
        self.initial.y = self.posY
        self.color = (100,100,100)
        self.snake = pygame.draw.rect(gameDisplay, self.color, self.initial, 0)

    def showSnake(self):
        self.initial.x = self.posX
        self.initial.y = self.posY
        self.color = (100,100,100)
        self.snake = pygame.draw.rect(gameDisplay, self.color, self.initial, 0)
    

Slither = [0,0]
                        
crashed = True

while crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = False
        elif event.type == pygame.VIDEOEXPOSE:
            foodObj = Food()
            foodObj.GenerateFood()
            Slither[0] = Snake()
        elif event.type == pygame.KEYDOWN:
            gameDisplay.fill((0,0,0))
            if event.key == pygame.K_DOWN:
                if Slither[0].initial.colliderect(foodObj.food) == True:
                    Slither[1] = Snake()
                    foodObj.GenerateFood()
                foodObj.ShowFood()
                oldPosX = Slither[0].posX
                oldPosY = Slither[0].posY
                Slither[0].moveSnake(0, 15)
                if Slither[1] != 0:
                    Slither[1].posX = oldPosX
                    Slither[1].posY = oldPosY
                    Slither[1].showSnake()
            elif event.key == pygame.K_UP:
                if Slither[0].initial.colliderect(foodObj.food) == True:
                    Slither[1] = Snake()
                    foodObj.GenerateFood()
                foodObj.ShowFood()
                oldPosX = Slither[0].posX
                oldPosY = Slither[0].posY
                Slither[0].moveSnake(0, -15)
                if Slither[1] != 0:
                    Slither[1].posX = oldPosX
                    Slither[1].posY = oldPosY
                    Slither[1].showSnake()
            elif event.key == pygame.K_LEFT:
                if Slither[0].initial.colliderect(foodObj.food) == True:
                    Slither[1] = Snake()
                    foodObj.GenerateFood()
                foodObj.ShowFood()
                oldPosX = Slither[0].posX
                oldPosY = Slither[0].posY
                Slither[0].moveSnake(-15, 0)
                if Slither[1] != 0:
                    Slither[1].posX = oldPosX
                    Slither[1].posY = oldPosY
                    Slither[1].showSnake()
            elif event.key == pygame.K_RIGHT:
                if Slither[0].initial.colliderect(foodObj.food) == True:
                    Slither[1] = Snake()
                    foodObj.GenerateFood()
                foodObj.ShowFood()
                oldPosX = Slither[0].posX
                oldPosY = Slither[0].posY
                Slither[0].moveSnake(15, 0)
                if Slither[1] != 0:
                    Slither[1].posX = oldPosX
                    Slither[1].posY = oldPosY
                    Slither[1].showSnake()
        print(event)

    pygame.display.update()
    #clock.tick(50)

pygame.quit()
quit()

Hello World!!
