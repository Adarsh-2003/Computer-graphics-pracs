import turtle as t
r = 10
for i in range(10):
    t.speed(20)
    t.circle(r * i)
    t.up()
    t.sety((r * i)*(-1))
    t.down()
