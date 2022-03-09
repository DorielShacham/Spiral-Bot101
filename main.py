import turtle as t
t.screensize(400,400,"black")
t.pensize(1)
t.speed(30)
for index in range(400):
    if index % 4 in [1]:
        t.pencolor("red")
    elif index % 4 in [2]:
        t.pencolor("orange")
    elif index % 4 in [3]:
        t.pencolor("purple")
    else:
        t.pencolor("blue")
    t.fd(5+index*2)
    t.left(91)

