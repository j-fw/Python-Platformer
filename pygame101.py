import pygame, random


pygame.init()
 
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0,0,0)
ORANGE = (255,165,0)

SCREENWIDTH=800
SCREENHEIGHT=600
clock=pygame.time.Clock()
all_sprites_list = pygame.sprite.Group()

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("LEAP")
largeText = pygame.font.Font('freesansbold.ttf',115)
regText = pygame.font.Font('freesansbold.ttf',25)



 
rightKnightM = pygame.image.load('knight_m_run_anim_f1.png')
leftKnightM  = pygame.image.load('knight_m_run_anim_Left.png')
rightJumpKnightM = pygame.image.load('knight_m_jump_anim_f0.png')
leftJumpKnightM = pygame.image.load('knight_m_jump_anim_Left.png')
idleKnightM = pygame.image.load('knight_m_idle_anim_f1.png')

rightSlime = pygame.image.load('swampy_idle_anim_f3.png')
leftSlime = pygame.image.load('swampy_idle_anim_f3_left.png')
rightOgre = pygame.image.load('ogre_run_anim_f3.png')
leftOgre = pygame.image.load('ogre_run_anim_f3_left.png')

speedPot = pygame.image.load('flask_big_yellow.png')
jumpPot = pygame.image.load('ironRing.png')
bg = pygame.image.load('big_floor_2.png')
wall = pygame.image.load('wall.png')
lava = pygame.image.load('lava.png')
spikes = pygame.image.load('spike_block.png')

playButton = pygame.image.load('play_button.png')
howToButton = pygame.image.load('howto_button.png')
menuButton = pygame.image.load('menu_button.png')
quitButton = pygame.image.load('quit_button.png')
fullHeart = pygame.image.load('ui_heart_full.png')
emptyHeart = pygame.image.load('ui_heart_empty.png')
leapLogo = pygame.image.load('leap_logo.png')

frame = pygame.image.load('frame_copy.png')
rightCorner = pygame.image.load('wall_corner.png')
leftWall = pygame.image.load('wall_corner_left.png')
rightWall = pygame.image.load('wall_corner_right.png')
topWall = pygame.image.load('wall_corner_top.png')
botWall = pygame.image.load('wall_corner_bot.png')
blue_fountain = pygame.image.load('blue_fountain.png')
red_fountain = pygame.image.load('red_fountain.png')
ladder = pygame.image.load('ladder.png')
door = pygame.image.load('door.png')

left = False
right = False
lJump = False
rJump = False


#walkCount = 0

def text_objects(text, font):
        
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect()

def redrawGameWindow(p1, blockList, left, right, lJump, rJump, enemyList,lives, points, collectibleList):
        #global walkCount

        #Drawing on Screen
        j = 0
        i = 0
        while j < SCREENWIDTH: 
            i = 0
            while i < SCREENHEIGHT:
                screen.blit(bg, (j,i))
                i+=40
            j+=40
        
        for enemies in enemyList:
                enemies.draw(screen)
        
        
        for blocks in blockList:
                blocks.draw(screen)
                
        for c in collectibleList:
                c.draw(screen)
                
        screen.blit(ladder,(740,575))
        screen.blit(door, (490,73))
        p1.draw(screen, left, right, lJump, rJump)
        for i in range(lives):
                screen.blit(fullHeart, (50 + 30*i, 25))
        
        TextSurf1, TextRect1 = text_objects("Points: " + " " + str(points), regText)
        TextRect1.center = (690,38)
        
        screen.blit(TextSurf1, TextRect1)
        
        all_sprites_list.update()
        
        #Refresh Screen
        pygame.display.flip()

        #Number of frames per second e.g. 60
        clock.tick(30)
    
def game_intro():
        intro = True
        index = 1
        pygame.time.delay(500)
        
        
        while intro:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                keys = pygame.key.get_pressed()
                screen.fill((74,50,40))

                screen.blit(blue_fountain, (0,0))
                screen.blit(blue_fountain, (SCREENWIDTH-16,SCREENHEIGHT-16))
                
                j=16
                while j < SCREENHEIGHT-16:
                        screen.blit(leftWall, (0,j))
                        j+=16
                j=16
                while j < SCREENHEIGHT-16:
                        screen.blit(rightWall, (SCREENWIDTH-16,j))
                        j+=16
                j=16
                while j < SCREENWIDTH-16:
                        screen.blit(topWall, (j,0))
                        j+=16
                j=16
                while j < SCREENWIDTH-16:
                        screen.blit(botWall, (j,SCREENHEIGHT-16))
                        j+=16

                
                screen.blit(playButton,(350,350))
                screen.blit(howToButton,(350,425))
                screen.blit(quitButton,(350,500))

                screen.blit(leapLogo, (100,100))


                if keys[pygame.K_RETURN]:
                        if index ==1:
                                game_run()
                        elif index == 2:
                                characterSelect()
                        elif index ==3:
                                pygame.quit()
                                quit()
                elif keys[pygame.K_DOWN]:
                        index+=1
                elif keys[pygame.K_UP]:
                        index-=1
                if(index>3):
                        index=3
                elif(index<1):
                        index = 1
                
                highlight(index)
                pygame.display.flip()
                clock.tick(15)

def highlight(ind):
        if ind ==1:
                screen.blit(frame, (346,348))
                
        elif ind == 2:
                screen.blit(frame, (346, 423))
                
        elif ind == 3:
                screen.blit(frame, (346, 498))
                
def characterSelect():
    select = True
    while(select):
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
            keys = pygame.key.get_pressed()
            screen.fill(WHITE)

            pygame.display.update()
            clock.tick(15)

def youWin():
      
            index = 1
            gOver = True
            while gOver:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        quit()
                        keys = pygame.key.get_pressed()
                        screen.fill((74,50,40))
                        
                        screen.blit(menuButton, (350,350))
                        screen.blit(quitButton, (350,425))
                        
                        TextSurf, TextRect = text_objects("You Win!", largeText)
                        TextRect.center = ((SCREENWIDTH/2),(200))
                        screen.blit(TextSurf, TextRect)

                        if keys[pygame.K_RETURN]:
                                if index ==1:
                                        game_intro()
                                        
                                elif index ==2:
                                        pygame.quit()
                                        quit()
                        elif keys[pygame.K_DOWN]:
                                index+=1
                        elif keys[pygame.K_UP]:
                                index-=1
                        if(index>2):
                                index=2
                        elif(index<1):
                                index = 1
                        
                        highlight(index)
                        pygame.display.update()
                        clock.tick(15)

def game_over():

        index = 1
        gOver = True
        while gOver:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                keys = pygame.key.get_pressed()
                screen.fill((74,50,40))
                
                screen.blit(menuButton, (350,350))
                screen.blit(quitButton, (350,425))
                
                TextSurf, TextRect = text_objects("Game Over", largeText)
                TextRect.center = ((SCREENWIDTH/2),(200))
                screen.blit(TextSurf, TextRect)

                if keys[pygame.K_RETURN]:
                        if index ==1:
                                game_intro()
                                
                        elif index ==2:
                                pygame.quit()
                                quit()
                elif keys[pygame.K_DOWN]:
                        index+=1
                elif keys[pygame.K_UP]:
                        index-=1
                if(index>2):
                        index=2
                elif(index<1):
                        index = 1
                
                highlight(index)
                pygame.display.update()
                clock.tick(15)
        

            
                
        
class Player(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
        def __init__(self, color, width, height,x,y):
                
                # Call the parent class (Sprite) constructor
                super(Player,self).__init__()
                # Pass in the color of the car, and its x and y position, width and height.
                # Set the background color and set it to be transparent
                self.image = pygame.Surface([width, height])
                self.image.fill(WHITE)
                self.image.set_colorkey(WHITE)
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.rect = self.image.get_rect()
                self.hitbox = (self.x,self.y,self.width,self.height)

        def draw(self, screen, left, right, lJump, rJump):
                self.hitbox = (self.x,self.y,self.width,self.height)
                #pygame.draw.rect(screen, (255,0,0),self.hitbox,2)
                if left:
                    screen.blit(leftKnightM, (self.x,self.y-7))
                elif right:
                    screen.blit(rightKnightM, (self.x,self.y-7))
                elif lJump:
                    screen.blit(leftJumpKnightM, (self.x,self.y-7))
                elif rJump:
                    screen.blit(rightJumpKnightM, (self.x,self.y-7))
                else:
                    screen.blit(idleKnightM, (self.x,self.y-7))
class Enemy(pygame.sprite.Sprite):
        def __init__(self, monster, width,  height, x, y, block):
                super(Enemy,self).__init__()

                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.monster = monster
                self.image = pygame.Surface([self.width, self.height])
                self.image.fill(WHITE)
                self.image.set_colorkey(WHITE)
                self.rect = self.image.get_rect()
                self.hitbox = (self.x,self.y,self.width,self.height)
                
                self.xMin = block.x
                self.xMax = block.x + block.width
                self.neg = -1

                if monster == 1:
                        self.rightAnim = rightSlime
                        self.leftAnim = leftSlime
                elif monster == 2:
                        self.rightAnim = rightOgre
                        self.leftAnim = leftOgre
                        
                

        def draw(self, screen):
                self.hitbox = (self.x,self.y,self.width,self.height)
                #pygame.draw.rect(screen, (255,0,0),self.hitbox,2)
                
                if(self.neg==1):                                         
                        screen.blit(self.rightAnim, (self.x,self.y))
                else:
                        screen.blit(self.leftAnim, (self.x,self.y))
                
                
class Block(pygame.sprite.Sprite):
        def __init__(self, bType, width, height, x, y):
                super(Block,self).__init__()               
                
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.bType = bType
                self.image = pygame.Surface([self.width, self.height])
                self.image.fill(WHITE)
                self.image.set_colorkey(WHITE)
                self.rect = self.image.get_rect()
                self.hitbox = (self.x,self.y,self.width,self.height)
                
                if bType == 1:
                        self.image = wall
                elif bType == 2:
                        self.image = lava
                elif bType ==3:
                        self.image = spikes

        def draw(self,screen):
                #self.hitbox = (self.x,self.y,self.width,self.height)
                pygame.draw.rect(screen, RED,self.hitbox)
                j = 0
                i = 0
                while j < self.height:
                    i = 0
                    while i < self.width:
                        screen.blit(self.image, (self.x + i,self.y + j))
                        i += 20
                    j += 20

                
class collectible(pygame.sprite.Sprite):
        def __init__(self, potType, width, height, x, y):
                super(collectible,self).__init__()               
                
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.potType = potType
                self.image = pygame.Surface([self.width, self.height])
                self.image.fill(WHITE)
                self.image.set_colorkey(WHITE)
                self.rect = self.image.get_rect()
                self.hitbox = (self.x,self.y,self.width,self.height)
                if(potType==1):
                        self.potImage = speedPot
                if(potType==2):
                        self.potImage = jumpPot
                

        def draw(self,screen):
                self.hitbox = (self.x,self.y,self.width,self.height)
                #pygame.draw.rect(screen, RED,self.hitbox,2)
                screen.blit(self.potImage, (self.x,self.y))



def isCollide(p1, p2):
        collisionY = False
        collisionX = False
        if p1.y + p1.height > p2.y and p1.y + p1.height< p2.y + p2.height:
                collisionY = True
        if (p1.x>p2.x and p1.x<p2.x+p2.width) or (p1.x+p1.width > p2.x and p1.x+p1.width<p2.x+p2.width):
                collisionX = True
        return collisionY and collisionX
        
def topCollide(p1,p2):
        collisionX = False
        collisionY = False
        if (p1.x>p2.x and p1.x<p2.x+p2.width) or (p1.x+p1.width > p2.x and p1.x+p1.width<p2.x+p2.width):
                collisionX = True
        if p1.y < p2.y + p2.height and p1.y > p2.y:
                collsiionY = True
        return collisionX and collisionY

def xCollide(p1,p2):
        if ((p1.x > p2.x) and p1.x<p2.x+p2.width) or (p1.x+p1.width>p2.x and p1.x+p1.width<p2.x+p2.width):
                return True
        else:
                return False

def enemyCollide(p1,p2):
        collisionY = False
        collisionX = False
        if p1.y + p1.height >= p2.y and p1.y + p1.height <= p2.y + p2.height:
                collisionY = True
        if (p1.x >= p2.x and p1.x <= p2.x+p2.width) or (p1.x+p1.width >= p2.x and p1.x+p1.width <= p2.x+p2.width):
                collisionX = True

        return collisionY and collisionX
#This will be a list that will contain all the sprites we intend to use in our game.
 
#Allowing the user to close the window...

def game_run():
        vel = 5
        carryOn = True
        
        p1 = Player(RED, 19, 30,740,500)

        
        #floor and walls
        b1 = Block(1, 710,50,40,575)
        b3 = Block(1,40,600,0,0)
        b4 = Block(1,40,600,760,0)
        b12 = Block(1, 710, 20, 40,0)
        
        #interactable blocks
        b2 = Block(1,100,20,550,475)
        b5 = Block(1, 200,20,350,400)
        b6 = Block(1, 60,40,640,350)
        b7 = Block(1, 40,60, 40,475)
        
        b8 = Block(1, 20,20, 120, 390)
        b9 = Block(1, 20, 20, 220, 295)
        b10 = Block(1, 20, 20, 320, 200)
        b11 = Block(1, 20,20, 420, 105)
        
        b13 = Block(1, 100,20, 490, 105)
        b14 = Block(1,40,20,720,245)
        b15 = Block(1, 160,20,500,200)
        b16 = Block(1, 80,20,80,200)
        b17 = Block(1, 40, 20, 40, 260)
        b18 = Block(1, 60,20,40,100)

        
        #interactable lava
        s1 = Block(2, 100, 20, 200, 500)
        s4 = Block(2, 40,40,600,350 )
        s5 = Block(2, 20,20,160,200)
        s6 = Block(2, 20,20,40,200)
        s7 = Block(2, 80,60,460,575)
        s8 = Block(2, 60,20,440,300)
        
        #decorative lava
        s2 = Block(2, 40,40,0,575)
        s3 = Block(2, 40,40, 760,575)

        lavaList = [s1,s4,s5,s6,s7,s8]
        blockList = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,s1,s2,s3,s4,s5,s6,s7,s8]

        e1 = Enemy(1, 20,20, 570,455,b2)
        e2 = Enemy(2, 33,48,300,535,b1)
        e3 = Enemy(1, 20,20,520,180, b15)
        e4 = Enemy(2, 33,48,380,365,b5)
        
        enemyList = [e1,e2,e3,e4]
        
        c1 = collectible(1, 16,16,300,559)
        c2 = collectible(2, 24,26,550,550)
        c3 = collectible(2, 24,26,40,75)
        c4 = collectible(2, 24,26,217,270)
        c5 = collectible(2, 24,26,417,80)
        c6 = collectible(2, 24,26,40,235)
        c7 = collectible(2, 24,26,40,550)
        c8 = collectible(2, 24,26, 500,175)
        
        collectibleList = [c2,c3,c4,c5,c6,c7,c8]

        
        falling = False
        isJump = False
        jumpCount = 8
        lives = 8
        points = 7
        cd = 60
        sBoost = False

        blockCDTime = 60
        blockCD = False
        
        sboostTime = 90
 
        while carryOn:
                
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                carryOn=False
                        elif event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                                        carryOn=False
                if lives == 0:
                        game_over()
                        
                if (p1.x< 512 and p1.x>490) and (p1.y> 72 and p1.y<105) and points>=7:
                        youWin()
                
                
                #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
                all_sprites_list.draw(screen)
                
                keys = pygame.key.get_pressed()

                #movement
                        
                
                for e in enemyList:
                        if(e.x<=e.xMin or e.x+e.width>=e.xMax):
                                e.neg*=-1
                        e.x+=3*e.neg
                        if cd == 0:
                                cd=60
                        if cd<60:
                                cd-=1
                        if enemyCollide(p1,e) and cd == 60:
                                lives-=1
                                cd-=1
                
                for c in collectibleList:
                        if(enemyCollide(p1,c)):
                                if c.potType == 1:
                                        sBoost = True
                                elif c.potType == 2:
                                        points +=1
                                collectibleList.remove(c)
                                
                if sboostTime == 0:
                        sBoost=False
                        sboostTime = 90
                        jumpCount = 8
                        
                if sBoost:
                        sboostTime-=1
                else:
                        vel = 5

                
                
                        
                if keys[pygame.K_LEFT]:
                        moved = False
                        if isJump or falling:
                            lJump = True
                            left = False
                            right = False
                            rJump = False
                        else:
                            left = True
                            right = False
                            lJump = False
                            rJump = False
                        
                        for blocks in blockList:
                                if p1.x > blocks.x + blocks.width:
                                        if p1.x - vel == blocks.x + blocks.width:
                                                p1.x -= vel
                                                moved = True
                                        elif p1.x - vel < blocks.x + blocks.width and p1.y>blocks.y and p1.y<blocks.y+blocks.height and not moved:
                                                p1.x -= vel - (p1.x - (blocks.x+blocks.width))
                                                moved = True
                                        if not moved:
                                                if(p1.x>vel):
                                                        p1.x -= vel
                                                        moved = True
                                                elif p1.x == vel:
                                                        p1.x -= vel
                                                        moved = True

                elif keys[pygame.K_RIGHT]:
                        moved = False
                        if isJump or falling:
                            lJump = False
                            left = False
                            right = False
                            rJump = True
                        else:
                            left = False
                            right = True
                            lJump = False
                            rJump = False


                            
                        for blocks in blockList:
                                if p1.x + p1.width < blocks.x:
                                        if p1.x + p1.width + vel == blocks.x:
                                                p1.x += vel
                                                moved = True
                                        elif p1.x + vel + p1.width > blocks.x and p1.y>blocks.y and p1.y<blocks.y+blocks.height and not moved:
                                                p1.x += blocks.x-(p1.x+p1.width)
                                                moved = True
                                        if not moved:
                                                if(p1.x<(800-vel-p1.width)):
                                                        p1.x += vel
                                                        moved = True
                                                elif(p1.x==(800-vel-p1.width)):
                                                        p1.x += vel
                                                        moved = True
                else:
                    if isJump or falling:
                        rJump = True
                        left = False
                        right = False
                        lJump = False
                    else:
                        left = False
                        right = False
                        lJump = False
                        rJump = False
                    
                    
                if not isJump: 
                        if keys[pygame.K_UP] and not falling:
                            isJump = True
                else:                                               
                        if jumpCount>=-8 and isJump:
                                neg = 1
                                moved = False
                                if jumpCount < 0:
                                        neg = -1
                                for blockCollide in blockList:
                                        if ((p1.y - ((jumpCount)**2)/2 * neg )< blockCollide.y + blockCollide.height)  and xCollide(p1,blockCollide) and isJump and p1.y > blockCollide.y + blockCollide.height:
                                                if blockCollide in lavaList and not blockCD:
                                                        lives-=1
                                                        blockCD = True
                                                if blockCD:
                                                        blockCDTime-=1
                                                if blockCDTime ==0:
                                                        blockCD = False
                                                        blockCDTime = 60
                                                        
                                                p1.y -= p1.y - blockCollide.y
                                                isJump = False
                                                jumpCount = 8
                                if isJump:
                                        p1.y -= (jumpCount**2)/2 * neg
                                        jumpCount-=1
                        else:
                                isJump = False
                                jumpCount = 8

                falling = True
                for blockCollide in blockList:
                        if (p1.height+p1.y) == blockCollide.y and xCollide(p1,blockCollide):
                                falling = False
                if (not isJump):
                        p1.y+=18
                        
                
                for blockCollide in blockList:
                        if isCollide(p1,blockCollide):
                                isJump = False
                                jumpCount = 8
                        if isCollide(p1,blockCollide) and (p1.y+p1.height)>blockCollide.y and p1.y < blockCollide.y and not isJump:
                                if blockCollide in lavaList and not blockCD:
                                        lives-=1
                                        blockCD = True
                                if blockCD:
                                        blockCDTime-=1
                                if blockCDTime ==0:
                                        blockCD = False
                                        blockCDTime = 60
                                p1.y-=((p1.y+p1.height)-blockCollide.y)
                                falling = False

                                
                redrawGameWindow(p1, blockList, left, right, lJump, rJump, enemyList,lives,points,collectibleList)
game_intro()
game_run()
pygame.quit()
