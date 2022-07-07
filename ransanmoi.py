import pygame
import random
pygame.init()
#color
bl = (0, 0, 0)
wh = (255, 255, 255)
gr = (0, 255, 0)
re = (213, 50, 80)
#display
dis_width = 900
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('game rác')
clock = pygame.time.Clock()
#snake_1 (speed & size)
ran_block = 10 
ran_tocdo = 20 #speedsnake
#font in game 
diem_font = pygame.font.SysFont("time new roman", 100)
font_style = pygame.font.SysFont("bahnschrift", 45)
#score in game
def Diem(diem):
    value = diem_font.render(" " + str(diem), True, gr)
    dis.blit(value, [0, 0])
#snake_2 (setting)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
def our_ran(ran_block, ran_list):
    for x in ran_list:
        pygame.draw.rect(dis, wh, [x[0], x[1], ran_block, ran_block])
#loopbyq
def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    ran_List = []
    Length_of_ran = 1
    moix = round(random.randrange(0, dis_width - ran_block) / 10) * 10
    moiy = round(random.randrange(0, dis_height - ran_block) / 10) * 10
    while not game_over:
        while game_close == True:
            dis.fill(bl)
            message("R - chơi lại hoặc Q - thoát!!!!", wh)
            Diem(Length_of_ran - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: #press q 
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r: #press r
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #press LEFT key
                    x1_change = -ran_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: #press RIGHT key
                    x1_change = ran_block
                    y1_change = 0
                elif event.key == pygame.K_UP: #press UP key
                    y1_change = -ran_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN: #press DOWN key
                    y1_change = ran_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(bl)
        pygame.draw.rect(dis, re, [moix, moiy, ran_block, ran_block])
        ran_Head = []
        ran_Head.append(x1)
        ran_Head.append(y1)
        ran_List.append(ran_Head)
        if len(ran_List) > Length_of_ran:
            del ran_List[0]
        for x in ran_List[:-1]:
            if x == ran_Head:
                game_close = True
        our_ran(ran_block, ran_List)
        Diem(Length_of_ran - 1)
        pygame.display.update()
        if x1 == moix and y1 == moiy:
            moix = round(random.randrange(0, dis_width - ran_block) / 10) * 10
            moiy = round(random.randrange(0, dis_height - ran_block) / 10) * 10
            Length_of_ran += 1 #eat moi
        clock.tick(ran_tocdo)
    pygame.quit()
    quit()
    #out game
 #loog game
gameLoop()
