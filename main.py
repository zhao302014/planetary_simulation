# 导入模块
import pygame
import sys
import math
from pygame.locals import *

# 初始化
pygame.init()

# 定义窗口大小、标题名称、字体设置、创建时钟(可以控制游戏循环频率)等
size = width, height = 1206, 780
screen = pygame.display.set_mode(size)
pygame.display.set_caption("太阳系行星运转示意图")
myfont = pygame.font.Font(None, 60)
clock = pygame.time.Clock()

# 定义三个空列表
pos_e = pos_mm = []
# 地球和月球等其他行星的公转过的角度
roll_e = roll_m = 0
roll_2 = roll_3 = roll_4 = roll_5 = roll_6 = roll_7 = roll_8 = 0

# 添加背景音乐
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1, 40)
pygame.mixer.music.set_volume(0.5)

# 循环，达到万事万物永不停息的目的
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # 宇宙
    background = pygame.image.load("image/starry_sky_bg.jpg")
    screen.blit(background, (0, 0))

    # 显示文字及星球
    textImage = myfont.render("Solar System", True, (255, 255, 0))  # 太阳系
    screen.blit(textImage, (100, 100))
    my_font = pygame.font.SysFont("arial", 15)
    text_surface = my_font.render("Sun", True, (255, 0, 0), (0, 0, 0))  # 太阳
    screen.blit(text_surface, (1020, 30))
    sun = pygame.image.load("image/sun_bg.png")
    screen.blit(pygame.transform.scale(sun, (27, 27)), (1090, 25))
    my_font = pygame.font.SysFont("arial", 15)
    text_surface = my_font.render("Mercury", True, (255, 0, 0), (0, 0, 0))  # 水星
    screen.blit(text_surface, (1020, 70))
    my_font = pygame.font.SysFont("arial", 15)
    Mercury = pygame.image.load("image/mercury_bg.png")
    screen.blit(pygame.transform.scale(Mercury, (27, 27)), (1090, 65))
    text_surface = my_font.render("Venus", True, (255, 0, 0), (0, 0, 0))  # 金星
    screen.blit(text_surface, (1020, 110))
    my_font = pygame.font.SysFont("arial", 15)
    spark = pygame.image.load("image/spark_bg.png")
    screen.blit(pygame.transform.scale(spark, (27, 27)), (1090, 105))
    text_surface = my_font.render("Earth", True, (255, 0, 0), (0, 0, 0))  # 地球
    screen.blit(text_surface, (1020, 150))
    my_font = pygame.font.SysFont("arial", 15)
    earth = pygame.image.load("image/earth_min_bg.png")
    screen.blit(pygame.transform.scale(earth, (27, 27)), (1090, 145))
    text_surface = my_font.render("Moon", True, (255, 0, 0), (0, 0, 0))  # 月球
    screen.blit(text_surface, (1020, 190))
    my_font = pygame.font.SysFont("arial", 15)
    moon = pygame.image.load("image/mercury_bg.png")
    screen.blit(pygame.transform.scale(moon, (27, 27)), (1090, 185))
    text_surface = my_font.render("Mars", True, (255, 0, 0), (0, 0, 0))  # 火星
    screen.blit(text_surface, (1020, 230))
    Mars = pygame.image.load("image/venus_bg.png")
    screen.blit(pygame.transform.scale(Mars, (27, 27)), (1090, 225))
    my_font = pygame.font.SysFont("arial", 15)
    text_surface = my_font.render("Jupiter", True, (255, 0, 0), (0, 0, 0))  # 木星
    screen.blit(text_surface, (1020, 270))
    Jupiter = pygame.image.load("image/jupiter_min_bg.png")
    screen.blit(pygame.transform.scale(Jupiter, (27, 27)), (1090, 265))
    my_font = pygame.font.SysFont("arial", 15)
    text_surface = my_font.render("Saturn", True, (255, 0, 0), (0, 0, 0))  # 土星
    screen.blit(text_surface, (1020, 300))
    Saturn = pygame.image.load("image/saturn_bg.png")
    screen.blit(pygame.transform.scale(Saturn, (30, 30)), (1090, 305))
    my_font = pygame.font.SysFont("arial", 15)
    text_surface = my_font.render("Uranus", True, (255, 0, 0), (0, 0, 0))  # 天王星
    screen.blit(text_surface, (1020, 340))
    Uranus = pygame.image.load("image/uranus_bg.png")
    screen.blit(pygame.transform.scale(Uranus, (27, 27)), (1090, 345))
    my_font = pygame.font.SysFont("arial", 15)
    text_surface = my_font.render("Neptune", True, (255, 0, 0), (0, 0, 0))  # 海王星
    screen.blit(text_surface, (1020, 380))
    Neptune = pygame.image.load("image/neptune_bg.png")
    screen.blit(pygame.transform.scale(Neptune, (27, 27)), (1090, 385))

    # 太阳
    sun = pygame.image.load("image/sun_bg.png")
    screen.blit(pygame.transform.scale(sun, (170, 170)), (527, 307))

    # 水星
    roll_3 += 0.077  # 每帧公转pi
    pos_3_x = int(size[0] // 2 + size[1] // 8 * math.sin(roll_3))
    pos_3_y = int(size[1] // 2 + size[1] // 8 * math.cos(roll_3))
    mercury = pygame.image.load("image/mercury_bg.png")
    screen.blit(pygame.transform.scale(mercury, (8, 8)), (pos_3_x, pos_3_y))

    # 金星
    roll_2 += 0.069  # 每帧公转pi
    pos_2_x = int(size[0] // 2 + size[1] // 7 * math.sin(roll_2))
    pos_2_y = int(size[1] // 2 + size[1] // 7 * math.cos(roll_2))
    venus = pygame.image.load("image/venus_bg.png")
    screen.blit(pygame.transform.scale(venus, (10, 10)), (pos_2_x, pos_2_y))

    # 地球
    roll_e += 0.060  # 每帧公转pi
    pos_e_x = int(size[0] // 2 + size[1] // 6 * math.sin(roll_e))
    pos_e_y = int(size[1] // 2 + size[1] // 6 * math.cos(roll_e))
    earth = pygame.image.load("image/earth_min_bg.png")
    screen.blit(pygame.transform.scale(earth, (15, 15)), (pos_e_x, pos_e_y))

    # 月球
    roll_m += 0.2  # 每帧公转pi
    pos_m_x = int(pos_e_x + size[1] // 50 * math.sin(roll_m))
    pos_m_y = int(pos_e_y + size[1] // 50 * math.cos(roll_m))
    mouth = pygame.image.load("image/mercury_bg.png")
    screen.blit(pygame.transform.scale(mouth, (6, 6)), (pos_m_x, pos_m_y))

    # 火星
    roll_4 += 0.053  # 每帧公转pi
    pos_4_x = int(size[0] // 2 + size[1] // 5 * math.sin(roll_4))
    pos_4_y = int(size[1] // 2 + size[1] // 5 * math.cos(roll_4))
    venus = pygame.image.load("image/venus_bg.png")
    screen.blit(pygame.transform.scale(venus, (13, 13)), (pos_4_x, pos_4_y))

    # 木星
    roll_5 += 0.045  # 每帧公转pi
    pos_5_x = int(size[0] // 2 + size[1] // 4 * math.sin(roll_5))
    pos_5_y = int(size[1] // 2 + size[1] // 4 * math.cos(roll_5))
    mouth = pygame.image.load("image/jupiter_bg.png")
    screen.blit(pygame.transform.scale(mouth, (70, 70)), (pos_5_x, pos_5_y))

    # 土星
    roll_6 += 0.037  # 每帧公转pi
    pos_6_x = int(size[0] // 2 + size[1] // 3.5 * math.sin(roll_6))
    pos_6_y = int(size[1] // 2 + size[1] // 3.5 * math.cos(roll_6))
    saturn = pygame.image.load("image/saturn_bg.png")
    screen.blit(pygame.transform.scale(saturn, (50, 50)), (pos_6_x, pos_6_y))

    # 天王星
    roll_7 += 0.031  # 每帧公转pi
    pos_7_x = int(size[0] // 2 + size[1] // 2.7 * math.sin(roll_7))
    pos_7_y = int(size[1] // 2 + size[1] // 2.7 * math.cos(roll_7))
    uranus = pygame.image.load("image/uranus_bg.png")
    screen.blit(pygame.transform.scale(uranus, (45, 45)), (pos_7_x, pos_7_y))

    # 海王星
    roll_8 += 0.025  # 每帧公转pi
    pos_8_x = int(size[0] // 2 + size[1] // 2 * math.sin(roll_8))
    pos_8_y = int(size[1] // 2 + size[1] // 2 * math.cos(roll_8))
    neptune = pygame.image.load("image/neptune_bg.png")
    screen.blit(pygame.transform.scale(neptune, (37, 37)), (pos_8_x, pos_8_y))

    # 刷新
    pygame.display.flip()
    # 数值越大刷新越快，小球运动越快
    clock.tick(50)