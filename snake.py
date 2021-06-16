 #计科203 江智昆 202010405307 贪吃蛇
import pygame as  pg
import random

#窗口网格化
class gezi:
    def __init__(self,row=0,col=0):
        self.row=row
        self.col=col
        self.width=int(w/Col)
        self.height=int(h/Row)
    def copy(self):
        return gezi(self.row,self.col)

#初始化
pg.init()
pg.mixer.init()
fps=8#设置刷新率

#文字部分
restart='重新游戏'
over='gameover'
font=pg.font.SysFont('‪simHei',30)
end=pg.font.SysFont('‪simHei',90)
start='开始游戏'
font_color1=(125,125,125)
font_color2=(255,125,125)
score=0
text_start=font.render(start,True,font_color1)
text_restart=font.render(restart,True,font_color1)
text_stop=end.render('游戏暂停',True,font_color2)
text_over=end.render(over,True,font_color2)
text_quit=font.render("结束游戏",True,font_color1)
text_exit=font.render("退出游戏",True,font_color1)
text_continue=font.render("继续游戏",True,font_color1)
#文字坐标、长度
x1,y1=450,150
x2,y2=450,200
start_w,start_h=text_start.get_size()
quit_w,quit_h=text_quit.get_size()
stop_w,stop_h=text_stop.get_size()
restart_w,restart_h=text_restart.get_size()
#设置背景音乐
pg.mixer.music.load("./bgm/bgm.mp3")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(loops=-1)
eatsound=pg.mixer.Sound("./bgm/eat.mp3")
eatsound.set_volume(0.2)

#导入图片:
#食物
apple=pg.image.load("./image/food.png")
#菜单背景
bg=pg.image.load("./image/bg.png")
#蛇头朝向
rhead=pg.image.load("./image/right.png")
lhead=pg.image.load("./image/left.png")
uhead=pg.image.load("./image/up.png")
dhead=pg.image.load("./image/down.png")
#蛇身图像
body_image=pg.image.load("./image/body.png")

#窗口的初始数值
size=w,h=1024,1024
window=pg.display.set_mode(size)
pg.display.set_caption("jzk贪吃蛇")
Quit=True
Row=40
Col=40
clock=pg.time.Clock()

#定义蛇头、蛇身、食物的位置：
head=gezi(row=int(Row/2),col=int(Col/2))
body=[]

#按钮
def anniu(text1,text2,wenzi1,wenzi2,w1,h1,w2,h2):
    quit=True
    window.blit(text1,(x1,y1))
    window.blit(text2,(x2,y2))
    pg.display.update()
    while quit:
        events=pg.event.get()
        for event in events:
            if event.type==pg.QUIT :
                 exit(0)
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    exit(0)
            #鼠标移动到文字上文字变色
            if event.type==pg.MOUSEMOTION:
               x,y= pg.mouse.get_pos()
               if x<=x1+w1 and x>=x1 and y>=y1 and y<=y1+h1:
                   text1_2=font.render(wenzi1,True,font_color2)
                   window.blit(text1_2,(x1,y1))
                   pg.display.update()
               else :
                   window.blit(text1,(x1,y1))
                   pg.display.update()
               if x<=x2+w2 and x>=x2 and y>=y2 and y<=y2+h2:
                   text2_2=font.render(wenzi2,True,font_color2)
                   window.blit(text2_2,(x1,y2))
                   pg.display.update()
               else:
                   window.blit(text2,(x1,y2))
                   pg.display.update()
             #点击按钮的效果
            if event.type==pg.MOUSEBUTTONDOWN:
                x,y= pg.mouse.get_pos()
                if x<=x1+w1 and x>=x1 and y>=y1 and y<=y1+h1:
                       quit=False
                if x<=x2+w2 and x>=x2 and y>=y2 and y<=y2+h2:
                       exit(0)
#给出食物的位置
def pos_food():
    while 1:
        legal=True
        pos=gezi(row=random.randint(3,Row-3),col=random.randint(3,Col-3))#避免食物产生在边角
        if head.col==pos.col and head.row==pos.col:
            legal=False
        for meat in body:
             if meat.col==pos.col and meat.row==pos.row:
                legal=False
        if legal:
            return pos
food=pos_food()
dir='left'
def blit(image,pos):
    left=pos.col*pos.width
    top=pos.row*pos.height
    window.blit(image,(left,top))

#创造初始界面
colck=pg.time.Clock()
window.blit(bg,(0,0))
anniu(text_start,text_quit,start,"结束游戏",start_w,start_h,quit_w,quit_h)

#游戏循环
while Quit:   
   #0游戏背景
    screen=pg.draw.rect(window,(225,225,225),(0,0,w,h))
    #得分
    text_score=font.render('得分:{}'.format(score),True,(100,100,100))
    window.blit(text_score,(5,5))

    #进食
    eat=(head.col==food.col and head.row==food.row)
    if eat:
        food=pos_food()#刷新食物
        eatsound.play(loops=0)
        score+=1
        #每拿三分增加一次移动速度
        if score%3==0:
            fps+=1

    #蛇的身体
    body.insert(0,head.copy())
    if len(body)>=30:#如果蛇太长则扩大窗口以免影响游戏体验
        w+=100
        h+=100
    if not eat:
        body.pop()

   #蛇头
    if dir=='left':
        head.col-=1
        blit(lhead,head)
    elif dir=='right':
        head.col+=1
        blit(rhead,head)
    if dir=='up':
        head.row-=1
        blit(uhead,head)
    elif dir=='down':
        head.row+=1
        blit(dhead,head)
    
    #画蛇身
    for meat in body:
        blit(body_image,meat)    
    blit(apple,food)
    pg.display.update()

    #判断蛇是否死亡
    dead=False
    if head.col<0 or head.col>Col or head.row<0 or head.row>Row:
        dead=True#撞墙
    for meat in body:
        if head.col==meat.col and head.row==meat.row:
            dead=True#吃到自己
    while dead:
        window.blit(text_over,(350,300))
        window.blit(text_restart,(x1,y1))
        window.blit(text_quit,(x2,y2))
        pg.display.update()
        events2=pg.event.get()
        for event2 in events2:
                    anniu(text_restart,text_quit,"重新游戏","结束游戏",restart_w,restart_h,quit_w,quit_h)
                    head=gezi(row=int(Row/2),col=int(Col/2))
                    #初始化数据
                    body=[]
                    score=0
                    dead=False
                    fps=8

    #处理事件
    for event in pg.event.get():
        if event.type==pg.QUIT:
            Quit=False
        elif event.type==pg.KEYDOWN:
            if event.key==273 or event.key==119:
                if dir =='right'or dir=='left':
                    dir='up'
            elif event.key==274 or event.key==115:
                 if dir =='right'or dir=='left':
                    dir='down'
            elif event.key==276 or event.key==97:
                 if dir =='up'or dir=='down':
                    dir='left'
            elif event.key==275 or event.key==100:
               if dir =='up'or dir=='down':
                    dir='right'
            elif event.key==pg.K_ESCAPE:
                exit(0)
            elif event.key==pg.K_SPACE:
                 quit=True
                 window.blit(text_stop,(350,350))
                 window.blit(text_continue,(x1,y1))
                 window.blit(text_quit,(x2,y2))
                 pg.display.update()
                 while quit:
                    events=pg.event.get()
                    for event in events:
                        if event.type==pg.QUIT :
                            exit(0)
                        if event.type==pg.KEYDOWN:
                            if event.key==pg.K_ESCAPE:
                                exit(0)
                        #鼠标移动到文字上文字变色
                        if event.type==pg.MOUSEMOTION:
                            x,y= pg.mouse.get_pos()
                            if x<=x1+restart_w and x>=x1 and y>=y1 and y<=y1+restart_h:
                                text1_2=font.render("继续游戏",True,font_color2)
                                window.blit(text1_2,(x1,y1))
                                pg.display.update()
                            else :
                                window.blit(text_continue,(x1,y1))
                                pg.display.update()
                                if x<=x2+quit_w and x>=x2 and y>=y2 and y<=y2+quit_h:
                                    text2_2=font.render("结束游戏",True,font_color2)
                                    window.blit(text2_2,(x1,y2))
                                    pg.display.update()
                                else:
                                    window.blit(text_quit,(x1,y2))
                                    pg.display.update()
                            #点击按钮的效果
                        if event.type==pg.MOUSEBUTTONDOWN:
                            x,y= pg.mouse.get_pos()
                            if x<=x1+restart_w and x>=x1 and y>=y1 and y<=y1+restart_h:
                                quit=False
                            if x<=x2+quit_w and x>=x2 and y>=y2 and y<=y2+quit_h:
                                exit(0)
    #设置帧数
    clock.tick(fps)   