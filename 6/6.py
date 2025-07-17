from turtle import *
'''dv2'''
screensize(3000,3000)
k = 60
left(90)
speed(3000)
for _ in range(2):
    forward(14*k)
    right(90)
    forward(18*k)
    right(90)
pu()
forward(3*k)
right(90)
forward(7*k)
left(90)
pd()
for _ in range(2):
    forward(74*k)
    right(90)
    forward(92*k)
    right(90)
done()











'''ege2023_3'''
# left(90)
# k = 60
# speed(3000)
# screensize(3000,3000)
# right(90)
# begin_fill()
# for _ in range(3):
#     right(45)
#     forward(10*k)
#     right(45)
# right(315)
# forward(10*k)
# for _ in range(2):
#     right(90)
#     forward(10*k)
# end_fill()
# cnt = 0
# canvas = getcanvas()
# for x in range(-200,200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k,y*k,x*k,y*k) == (5,):
#             cnt += 1
# print(cnt)
# pu()
# for x in range(-20,10):
#     for y in range(-20,10):
#         goto(x*k,y*k)
#         dot(3, 'red')
# done()

'''ege2024_2'''
# left(90)
# k = 100
# speed(3000)
# screensize(3000,3000)
# begin_fill()
# for _ in range(2):
#     forward(7*k)
#     right(90)
#     forward(12*k)
#     right(90)
# end_fill()
# # из верхней итерации вынесли лишнюю
# pu()
# for _ in range(1):
#     forward(7*k)
#     right(90)
#     forward(12*k)
#     right(90)
# pd()
# #
# pu()
# forward(4*k)
# right(90)
# forward(6*k)
# left(90)
# pd()
# begin_fill()
# for _ in range(2):
#     forward(83*k)
#     right(90)
#     forward(77*k)
#     right(90)
# end_fill()
# cnt = 0
# canvas = getcanvas()
# for x in range(-200,200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k,y*k,x*k,y*k) != ():
#             cnt += 1
# print(cnt)
# done()


'''var14'''
# left(90)
# tracer(0)
# k = 60
# screensize(3000,3000)
#
# begin_fill()
# for _ in range(3):
#     forward(7*k)
#     right(120)
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-10,10):
#     for y in range(-10,10):
#         if canvas.find_overlapping(x*k,y*k,x*k,y*k) == (5,):
#             cnt += 1
# print(cnt)
# pu()
# for x in range(-10,10):
#     for y in range(-10,10):
#         goto(x*k,y*k)
#         dot(3, 'red')
# done()



'''var1'''
# screensize(3000,3000)
# left(90)
# tracer(0)
# k = 15
# for _ in range(5):
#     forward(30*k)
#     right(90)
#     forward(40*k)
#     right(90)
# pu()
# forward(20*k)
# right(90)
# forward(5*k)
# right(90)
# pd()
# for _ in range(7):
#     forward(10*k)
#     right(90)
# pu()
# for x in range(-100,100):
#     for y in range(-100,100):
#         goto(x*k,y*k)
#         dot(3)
# done()

'''var2'''
# from turtle import *
# screensize(3000,3000)
# k = 30
# tracer(0)
# left(90)
# for _ in range(5):
#     forward(30*k)
#     right(90)
#     forward(40*k)
#     right(90)
# pu()
# forward(20*k)
# right(90)
# forward(15*k)
# right(90)
# pd()
# for _ in range(7):
#     forward(10*k)
#     right(90)
#
# pu()
# for x in range(-100,100):
#     for y in range(-100,100):
#         goto(x*k,y*k)
#         dot(3,'red')
# done()

'''var3'''
# screensize(3000,3000)
# left(90)
# tracer(0)
# k = 15
# for _ in range(3):
#     forward(2*k)
#     right(90)
#     forward(3*k)
#     left(90)
# right(180)
# forward(6*k)
# right(90)
# forward(9*k)
# pu()
# backward(4*k)
# right(90)
# pd()
# for _ in range(3):
#     forward(1*k)
#     right(90)
#     forward(2*k)
#     left(90)
# right(180)
# forward(4*k)
# right(90)
# forward(6*k)
# right(90)
# forward(1*k)
# penup()
# for x in range(-100,100):
#     for y in range(-100,100):
#         goto(x*k,y*k)
#         dot(3, 'red')
# done()

'''var5'''
# from turtle import *
# left(90)
# k = 60
# screensize(3000,3000)
# speed(3000)
# begin_fill()
# for _ in range(2):
#     forward(17*k)
#     left(90)
#     forward(10*k)
#     left(90)
# end_fill()
# pu()
# back(4*k)
# right(90)
# back(3*k)
# left(90)
# pd()
# begin_fill()
# for _ in range(2):
#     forward(40*k)
#     right(90)
#     forward(10*k)
#     right(90)
# end_fill()
#
# canvas = getcanvas()
# cnt = 0
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) != ():
#             cnt += 1
# print(cnt)
# # pu()
# # for x in range(-100,100):
# #     for y in range(-100,100):
# #         goto(x*k,y*k)
# #         dot(3,'red')
# done()

'''var7'''
# from turtle import *
# k = 25
# screensize(3000,3000)
# tracer(0)
# for _ in range(3):
#     pd()
#     for _ in range(2):
#         forward(10*k)
#         right(90)
#         forward(10*k)
#         right(90)
#     pu()
#     forward(5*k)
#     right(90)
#     forward(5*k)
#     left(90)
#
# pu()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*k,y*k)
#         dot(3,'red')
# done()

'''var9'''
# from turtle import *
# k = 10
# screensize(3000,3000)
# tracer(0)
#
# pu()
# forward(10*k)
# right(90)
# forward(10*k)
# right(30)
# pd()
# begin_fill()
# for _ in range(4):
#     forward(25*k)
#     right(90)
# end_fill()
#
# canvas = getcanvas()
# count = 0
# # for x in range(0,1000):
# #     for y in range(-500, 500):
# #         if canvas.find_overlapping(x*k,y*k,x*k,y*k) == (5,):
# #             count += 1
# pu()
# for x in range(-100,100):
#     for y in range(-100,100):
#         goto(x*k,y*k)
#         dot(3, 'red')
# print(count)
# done()

'''var20'''
# screensize(3000,3000)
# speed(3000)
# k = 30 # 60+ для заливки
# begin_fill()
# right(90)
# forward(4*k)
# right(90)
# forward(48*k)
# right(90)
# forward(4*k)
# right(30)
# for _ in range(8):
#     forward(6*k)
#     right(120)
#     forward(6*k)
#     right(240)
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
#             cnt += 1
# print(cnt)
# penup()
# for x in range(-100,10):
#     for y in range(-10,15):
#         goto(x*k,y*k)
#         dot(3, 'red')
# done()

'''dosrok'''
# screensize(3000,3000)
# left(90)
# k = 60
# speed(3000) # для заливки, tracer(0) - чтоб быстро нарисовались точки
#
# right(30)
# begin_fill()
# for _ in range(2):
#     right(150)
#     forward(6*k)
#     right(30)
#     forward(12*k)
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
#             cnt += 1
# print(cnt)
# penup()
# for x in range(-10,10):
#     for y in range(-20,10):
#         goto(x*k,y*k)
#         dot(3, 'red')
# done()

''' Пробник 15 '''
# tracer(0)
# screensize(3000,3000)
# pendown()
# left(90)
# k = 10
# begin_fill()
# for _ in range(6):
#     forward(31*k)
#     right(60)
# end_fill()
#
# penup()
#
# canvas = getcanvas() # k > 60
# cnt = 0
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
#             cnt += 1
# print(cnt)
#
# dots = 0
# for x in range(-20,60):
#     for y in range(-20,60):
#         if  y < 1/3**0.5*x + 31 and y < -1/3**0.5*x + 62 and y > 31:
#             dots += 2
# for x in range(-20,60):
#     for y in range(-20,60):
#         if x > 0 and x < 54 and y >= 0 and y <= 31:
#             dots += 1
# print(dots)
# for x in range(-20,60):
#     for y in range(-20,60):
#         goto(x*k,y*k)
#         dot(2, 'red')
# done()

''' B99881 '''
# left(90)
# speed(3000) # Вместо tracer
# screensize(3000,3000)
# k = 100 # Побольше
# begin_fill() # Начало заливки 1-ой фигуры
# for _ in range(2): # Уменьшаем до замыкания фигуры
#     forward(27*k)
#     right(90)
#     forward(12*k)
#     right(90)
# end_fill() # Конец заливки
# pu()
# forward(4*k)
# right(90)
# forward(6*k)
# left(90)
# down()
# begin_fill() # Начало заливки 2-ой фигуры
# for _ in range(2): # Уменьшаем до замыкания фигуры
#     forward(83*k)
#     right(90)
#     forward(77*k)
#     right(90)
# end_fill() # Конец заливки
# canvas = getcanvas() ###
# cnt = 0 # Счётчик точек
# for x in range(-300, 300): # Следим, чтобы вся фигура входила
#     for y in range(-300, 300): # Следим, чтобы вся фигура входила
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) != (): # Линии включ.
#             cnt += 1 ###
# print(cnt) ###
# done()

'''A7F8FA'''
# tracer(0)
# screensize(3000,3000)
# k = 10
# pendown()
# left(90)
# for i in range(9):
#     forward(27*k)
#     right(90)
#     forward(30*k)
#     right(90)
# penup()
# forward(3*k)
# right(90)
# forward(6*k)
# left(90)
# pendown()
# for i in range(9):
#     forward(77*k)
#     right(90)
#     forward(66*k)
#     right(90)
# pu()
# for x in range(-60,40):
#     for y in range(-60,30):
#         goto(x*k, y*k)
#         dot(3)
# done()

''' 19080A '''
# left(90)
# tracer(0)
# k = 20
# screensize(3000,3000)
# pendown()
# right(315)
# for i in range(7):
#     forward(16 * k)
#     right(45)
#     forward(8 * k)
#     right(135)
#
# pu()
# for x in range(-30,30):
#     for y in range(-30,30):
#         goto(x * k, y * k)
#         dot(5)
# done()

''' ДЗ 1 '''
# pen()
# left(90)
# k = 70
# screensize(6000,6000)
# tracer(0)
# penup()
# for _ in range(10):
#     right(120)
#     forward(12*k)
# pendown()
# for _ in range(7):
#     forward(7*k)
#     right(90)
# for _ in range(5):
#     right(60)
#     forward(20*k)
#     forward(30*k)
# penup()
# for x in range(-20,20):
#     for y in range(-20, 10):
#         setpos(x*k,y*k)
#         dot(3)
# done()

''' ДЗ 2 '''
# left(90)
# k = 100
# screensize(6000,6000)
# speed(3000)
#
# for _ in range(4):
#     right(45)
#     forward(10*k)
#     right(45)
# for _ in range(4):
#     forward(20*k)
#     right(90)
#
# pu()
# for x in range(-10,40):
#     for y in range(-20, 10):
#         setpos(x*k,y*k)
#         dot(3,'red')
# done()

''' ДЗ 3 '''
# left(90)
# k = 50
# screensize(6000,6000)
# tracer(0)
#
# for _ in range(5):
#     right(45)
#     forward(10*k)
#     right(45)
# for _ in range(6):
#     forward(20*k)
#     right(90)
#
# pu()
# for x in range(-10,40):
#     for y in range(-20, 10):
#         setpos(x*k,y*k)
#         dot(3,'red')
# done()

''' ДЗ 4 '''
# left(90)
# k = 25
# screensize(6000,6000)
# tracer(0)
#
# for _ in range(5):
#     forward(10*k)
#     right(90)
#     forward(16*k)
#     right(90)
# for _ in range(6):
#     left(45)
#     forward(5*2**0.5*k)
#     right(135)
# for _ in range(3):
#     forward(14*k)
#     left(120)
#
# pu()
# for x in range(-10,40):
#     for y in range(-10, 30):
#         setpos(x*k,y*k)
#         dot(3,'red')
# done()

''' ДЗ 5 '''
# left(90)
# k = 45
# screensize(6000,6000)
# speed(3000)
#
# for _ in range(4):
#     forward(12*k)
#     right(90)
# for _ in range(5):
#     forward(4*k)
#     right(45)
#
# canvas = getcanvas()
# cnt = 0
# for x in range(-100,200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) != ():
#             cnt += 1
# print(cnt)
#
# pu()
# for x in range(-10,40):
#     for y in range(-10, 30):
#         setpos(x*k,y*k)
#         dot(3,'red')
# done()

''' ДЗ 6 '''
# left(90)
# k = 45
# screensize(6000,6000)
# tracer(0)
#
# left(255)
# for _ in range(3):
#     left(30)
#     for _ in range(4):
#         forward(10*k)
#         left(90)
#
# pu()
# for x in range(-10,40):
#     for y in range(-10, 30):
#         setpos(x*k,y*k)
#         dot(3,'red')
# done()

''' №15 '''
# k = 5
# left(90)
# speed(300)
# screensize(3000,3000)
# begin_fill()
# for _ in range(3):
#     forward(111*k)
#     right(120)
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-100,200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
#             cnt += 1
# print(cnt)
# done()

''' №14 '''
# from math import *
# k = 100
# left(90)
# speed(300)
# screensize(3000,3000)
# begin_fill()
# for _ in range(3):
#     forward(137*k)
#     right(120)
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-100,200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
#             cnt += 1
# print(cnt)
# cnt = 0
# for y in range(-200, 200):
#     for x in range(-10,200):
#         if y < tan(radians(150))*x + 137 and y > tan(radians(30))*x and x > 0:
#             cnt += 1
# print(cnt)
# done()

''' №11 '''
# k = 30
# tracer(0)
# screensize(3000,3000)
# right(40)
# begin_fill()
# for _ in range(6):
#     right(120)
#     forward(3*k)
#     left(60)
#     back(3*k)
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-100,200):
#     for y in range(-100, 100):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
#             cnt += 1
# print(cnt)
# penup()
# for x in range(-30,30):
#     for y in range(-30,30):
#         setpos(x*k,y*k)
#         dot(3)
# done()

''' №8 '''
# left(90)
# k = 100
# speed(3000)
# screensize(3000,3000)
# begin_fill()
# for _ in range(2):
#     right(90)
#     forward(120*k)
#     right(90)
#     forward(14*k)
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-100,200):
#     for y in range(-100, 100):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) != ():
#             cnt += 1
# print(cnt)
# done()

''' №7 '''
# left(90)
# k = 24
# tracer(0)
# screensize(3000,3000)
#
# right(90)
# for _ in range(3):
#     right(45)
#     forward(12*k)
#     right(45)
# right(315)
# forward(12*k)
# for _ in range(2):
#     right(90)
#     forward(12*k)
# pu()
# for x in range(-20,10):
#     for y in range(-20,10):
#         goto(x*k,y*k)
#         dot(3)
# cnt = 0
# for x in range(-20,10):
#     for y in range(-20,10):
#         if y < -x and y > x - 12 * 2 ** 0.5 and y > -x - 12 * 2 ** 0.5 and y < x + 12 * 2 **0.5:
#             cnt +=1
# print(cnt)
# done()

''' №2 '''
# screensize(2500, 2500)
# k = 100
# tracer(0)
# down()
# begin_fill()
# for i in range(6):
#     forward(6*k)
#     right(300)
# end_fill()
# up()
# forward(3*k)
# right(270)
# forward(5*k)
# right(90)
# down()
# begin_fill()
# for i in range(2):
#     forward(7*k)
#     right(270)
#     forward(9*k)
#     right(270)
# end_fill()
# up()
# canvas = getcanvas()
# cnt = 0
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) != ():
#             cnt += 1
# print(cnt)
# penup()
# for x in range(-10,20):
#     for y in range(-10, 20):
#         setpos(x*k,y*k)
#         dot(3,'red')
# done()

''' №1 '''
# pen()
# k = 50
# screensize(3000,3000)
# left(90)
# speed(100000) # при tracer заливка нерпавильно считает
#
#
# right(45)
# forward(4*k)
# begin_fill()
# for _ in range(2):
#     right(45)
#     forward(7*k)
#     right(135)
#     forward(4*k)
# end_fill()
#
# canvas = getcanvas()
# cnt = 0
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
#             cnt += 1
# print(cnt)
#
# penup()
# for x in range(0,20):
#     for y in range(0, 20):
#         setpos(x*k,y*k)
#         dot(5)
#
# done()

''' demo-variant '''
# k = 10
# screensize(3000,3000)
# tracer(0)
# left(90)
#
# for i in range(9):
#     forward(22*k)
#     right(90)
#     forward(6*k)
#     right(90)
# penup()
# forward(1*k)
# right(90)
# forward(5*k)
# left(90)
# pendown()
# for i in range(9):
#     forward(53*k)
#     right(90)
#     forward(75*k)
#     right(90)
# canvas = getcanvas()
# cnt = 0
# for x in range(-200, 200):
#     for y in range(-200, 200):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
#             cnt += 1
# print(cnt)
# # оси координат:
# penup()
# for x in range(-60, 100):
#     for y in range(-60, 60):
#         goto(x*k,y*k)
#         dot(3)
# done()