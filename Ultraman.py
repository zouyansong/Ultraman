from turtle import *

qianlan = (50,160,240)
gold = (255,255,0)
def head(x,y):#头
    pu()
    goto(x,y)
    pd()
    seth(0)
    circle(-70)

    #额头forehead部分
    begin_fill()
    fillcolor(qianlan)
    pu()
    goto(-12,198)
    pd()
    seth(91)
    circle(-3,180)
    seth(280)
    fd(20)
    #seth(0)
    #fd(5)
    circle(3,160)
    seth(80)
    fd(20)
    seth(89)
    circle(-3,180)
    end_fill()

    #眼睛
    pu()
    goto(-30,170)
    begin_fill()
    fillcolor(gold)
    pd()
    seth(0)
    circle(-20)
    end_fill()
    
    pu()
    goto(30,170)
    begin_fill()
    fillcolor(gold)
    pd()
    seth(0)
    circle(-20)
    end_fill()

    #嘴巴
    pu()
    goto(-12,100)
    begin_fill()
    fillcolor(gold)
    pd()
    seth(0)
    fd(24)
    seth(270)
    fd(2)
    circle(-12,180)
    fd(2)
    end_fill()

    #耳朵
    pu()
    goto(-61,165)
    pd()
    seth(175)
    circle(24,175)
    
    begin_fill()
    fillcolor(qianlan)
    pu()
    goto(-61,165)
    pd()
    seth(175)
    circle(24,10)
    #goto(-67,165)
    #pd()
    seth(240)
    circle(75,34)
    end_fill()

    pu()
    goto(61,165)
    pd()
    seth(5)
    circle(-24,175)
    
    begin_fill()
    fillcolor(qianlan)
    pu()
    goto(61,165)
    pd()
    seth(5)
    circle(-24,10)
    #goto(67,165)
    #pd()
    seth(300)
    circle(-75,34)
    end_fill()

def body(x,y):#身体
    #躯干
    pu()
    goto(x,y)
    pd()
    seth(180)
    circle(20,85)
    fd(150)
    circle(15,180)
    seth(70)
    fd(30)
    circle(-20,140)
    fd(30)
    seth(275)
    circle(15,180)
    fd(150)
    circle(20,85)

    #躯干分为三段
    begin_fill()
    fillcolor(qianlan)
    pu()
    goto(x,y)
    pd()
    seth(180)
    circle(20,85)
    fd(70)
    #goto(-45,-30)
    #pd()
    seth(350)
    circle(280,21.2) #还是哪里计算出了问题,小数点可能导致之后无法保存
    seth(95)
    fd(70)
    circle(20,85)
    end_fill()
    #fd(100)

    #腿部分染色
    pu()
    goto(-56,-42)
    pd()
    begin_fill()
    fillcolor(qianlan)
    seth(265)
    fd(60)
    circle(15,180)
    seth(70)
    fd(30)
    circle(-20,140)
    fd(30)
    seth(275)
    circle(15,180)
    fd(60)
    seth(190)
    circle(-300,21)
    end_fill()
    
    #中心红色圆
    pu()
    goto(0,40)
    pd()
    seth(0)
    begin_fill()
    fillcolor('red')
    circle(-18)
    end_fill()

    #左手
    pu()
    goto(-52,25)
    pd()
    seth(170)
    fd(40)
    circle(10,180)
    seth(345)
    fd(42)

    
    pu()
    goto(-52,25)
    pd()
    begin_fill()
    fillcolor(qianlan)
    seth(170)
    fd(16)
    seth(260)
    fd(22)
    seth(345)
    fd(17)
    end_fill()

    
    pu()
    goto(-75,29)
    pd()
    begin_fill()
    seth(170)
    fd(16)
    circle(10,180)
    seth(345)
    fd(15)
    seth(80)
    fd(21)
    end_fill()

    #右手
    pu()
    goto(46,22)
    pd()
    seth(35)
    fd(16)
    circle(-80,25)
    circle(-12,170)
    fd(53)

    begin_fill()
    pu()
    goto(46,22)
    pd()
    seth(35)
    fd(16)
    seth(280)
    fd(24)
    seth(200)
    fd(17)
    end_fill()

    pu()
    goto(76,14)
    begin_fill()
    pd()
    seth(20)
    fd(22)
    circle(12,170)
    circle(80,15)
    seth(280)
    fd(24)
    end_fill()

x = -100
y = -150
def xi():#习
    #横
    x1 = x + 20
    y1 = y - 30
    pu()
    goto(x,y-3)
    pd()
    goto(x1,y-3)
    goto(x1,y1)
    goto(x1-5,y1+5)

    #点
    pu()
    x2 = x + 8
    y2 = y - 8
    goto(x2,y2)
    pd()
    goto(x2+6, y2-6)
    
    #提
    pu()
    y3 = y - 25
    goto(x+1,y3)
    pd()
    goto(x+15,y3+7)
    

def jia():#佳
    #撇
    x1 = x + 45
    pu()
    goto(x1,y)
    pd()
    goto(x1-2,y-4)
    goto(x1-4,y-6)
    goto(x1-12,y-12)
    
    #竖
    pu()
    goto(x1-4,y-6)
    pd()
    goto(x1-4,y-32)

    #横
    pu()
    x2 = x1 + 2
    y2 = y - 10
    goto(x2,y2)
    pd()
    goto(x2+12, y2)

    #竖
    pu()
    goto(x2+6,y2+5)
    pd()
    goto(x2+6,y2-5)
    
    #横
    pu()
    goto(x1,y2-6)
    pd()
    goto(x1+17,y2-6)
    
    #横
    pu()
    goto(x2,y2-13)
    pd()
    goto(x2+12, y2-13)
    
    #竖
    pu()
    goto(x2+6,y2-8)
    pd()
    goto(x2+6,y2-18)

    #横
    pu()
    goto(x1,y2-19)
    pd()
    goto(x1+20,y2-19)
    
def sheng():#生
    x1 = x + 80
    
    #撇
    pu()
    goto(x1+6,y-5)
    pd()
    goto(x1+4,y-10)
    goto(x1,y-16)
    goto(x1-2,y-18)
    
    #横
    pu()
    goto(x1+2,y-13)
    pd()
    goto(x1+20,y-13)

    #横
    pu()
    goto(x1+3,y-22)
    pd()
    goto(x1+18,y-22)
    
    #竖
    pu()
    goto(x1+12,y-3)
    pd()
    goto(x1+12,y-32)

    #横
    pu()
    goto(x1,y-33)
    pd()
    goto(x1+20,y-33)

def ri():#日
    #竖
    pu()
    x1 = x+110
    goto(x1,y-7)
    pd()
    goto(x1,y-32)

    #横折钩
    pu()
    goto(x1+1,y-7)
    pd()
    goto(x1+14,y-7)
    goto(x1+14,y-32)

    #横
    pu()
    goto(x1+1,y-18)
    pd()
    goto(x1+13,y-18)

    #横
    pu()
    goto(x1+1,y-31)
    pd()
    goto(x1+13,y-31)

def kuai():#快
    x1 = x+140
    
    #点
    pu()
    goto(x1-1,y-11)
    pd()
    goto(x1-3,y-14)
    goto(x1-5,y-16)
    
    #点
    pu()
    goto(x1+5,y-9)
    pd()
    goto(x1+8,y-12)
    
    #竖
    pu()
    goto(x1+3,y-2)
    pd()
    goto(x1+3,y-32)
    
    #横折
    pu()
    goto(x1+9,y-7)
    pd()
    goto(x1+21,y-7)
    goto(x1+21,y-16)
    
    #横
    pu()
    goto(x1+7,y-17)
    pd()
    goto(x1+27,y-17)
    
    #撇
    pu()
    goto(x1+15,y-2)
    pd()
    goto(x1+15,y-15)
    goto(x1+12,y-24)
    goto(x1+9,y-32)
    
    #捺
    pu()
    goto(x1+15,y-16)
    pd()
    goto(x1+18,y-22)
    goto(x1+28,y-30)

def le():#乐
    x1 = x + 172
    #撇
    pu()
    goto(x1+18,y-3)
    pd()
    goto(x1+13,y-7)
    goto(x1+3,y-10)
    
    #竖折
    goto(x1+1,y-18)
    goto(x1+20,y-18)
    
    #竖钩
    pu()
    goto(x1+11,y-11)
    pd()
    goto(x1+11,y-33)
    goto(x1+7,y-28)
    
    #点
    pu()
    goto(x1+7,y-23)
    pd()
    goto(x1+2,y-28)
    
    #点
    pu()
    goto(x1+15,y-24)
    pd()
    goto(x1+20,y-29) 

def main():
    pensize(1)
    hideturtle()
    colormode(255)
    setup(400,500)
    speed(5) #设置画画速度

    head(0,200)
    body(-29,65)
    pensize(2)
    xi()
    jia()
    sheng()
    ri()
    kuai()
    le()
    
    

main()

#以下为记录为MP4和gif部分
#具体参考https://github.com/MiracleXYZ/turtle_recorder
#注意路径下不能包含中文，否则会报错
##from turtle_recorder import Recorder
##
##with Recorder(main,fps=30) as rec:
##    rec.to_video('aoteman.mp4')
##    #rec.to_gif('aotoman.gif')
