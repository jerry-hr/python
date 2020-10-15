import turtle
import time
import random

def up():
    jerry.setheading(90)
    jerry.forward(20)

def down():
    jerry.setheading(270)
    jerry.forward(20)

def left():
    jerry.setheading(180)
    jerry.forward(20)

def right():
    jerry.setheading(0)
    jerry.forward(20)

playground = turtle.Screen()
playground.register_shape('tom.gif')
playground.register_shape('jerry.gif')

playground.onkey(up,'Up') #当上键被按下的时候
playground.onkey(down,'Down')
playground.onkey(left,'Left')
playground.onkey(right,'Right')

playground.listen()  #用来监听，当按键按下触发事件



writer = turtle.Turtle()
writer.color('brown')
writer.hideturtle()
writer.penup()
writer.home()
writer.write("TOM & JERRY",align='center',font=("Comic Sans MS",50,'bold'))
writer.goto(0,-50)
writer.write("READY? 3,2,1,GO!",align='center',font=("Comic Sans MS",20,'bold'))
#屏幕沉睡3秒后开始游戏
time.sleep(3)

writer.clear()

tom = turtle.Turtle()
tom.shape('tom.gif')
tom.penup()
tom.goto(random.randint(-200,200),random.randint(-200,200))
tom.pendown()
tom.pensize(3)
tom.color('blue')

jerry = turtle.Turtle()
jerry.shape('jerry.gif')
jerry.speed(0)
jerry.penup()
jerry.goto(random.randint(-200,200),random.randint(-200,200))
jerry.color('brown')


start = time.time() 
while True:
    tom.setheading(tom.towards(jerry))
    tom.forward(5)
    if tom.distance(jerry) < 10:
        end = time.time() 
        playground.clear()
        jerry.goto(0,0) #jerry归位
        jerry.write("GAME OVER",align='center',font=("Comic Sans MS",50,'bold'))
        jerry.goto(0,-50)
        jerry.write("YOU SURVIVED {:.1f} SECONDS".format(end-start),align='center',font=("Comic Sans Ms",20,'bold'))
        tom.pu()
        tom.goto(30,-70)
        tom.stamp() #tom图像印章
        jerry.pu()
        jerry.goto(-80, -70)
        jerry.stamp()  
        break

