import turtle as t

print('hello, python')
# 거북이가 기어다님.
t.forward(100)  #전진 100픽셀
t.left(90)     #왼쪽으로 회전 90도
t.shape('turtle')  #커서모양 '거북이'로 변경
t.forward(50)   #전진 50픽셀
t.left(90)      #왼쪽으로 회전 90도
t.fd(100)       #forward 와 같은 명령어
t.speed('fast')  #속도 조절 '빠르게'
t.fd(100)    
t.speed(1)  # 속도를 숫자로 표시. 0~10까지 숫자.
t.fd(50)
t.color('red')
t.pensize(5)
t.bgcolor('blue')
t.penup()
t.left(90)
t.fd(50)
t.pendown()
t.left(90)
t.fd(50)
t.goto(-50,-50)