'''demo'''
# # 0 открытие файла
# f = open('demo_2025_27_Б.txt')
# data = []
# for s in f:
#     s = s.replace(',', '.')
#     x, y = map(float, s.split())
#     data.append([x,y])
# print(len(data))
# # 1 разбиение на кластеры
# # 1.1. аналитика
# clusters = [[],[],[]]
# for point in data:
#     if point[0] > 5:
#         clusters[2].append(point)
#     else:
#         if point[1] > 6:
#             clusters[1].append(point)
#         else:
#             clusters[0].append(point)
# print([len(x) for x in clusters])
# # 1.1.1* проверочка на разделение
# # from turtle import *
# # from random import *
# # pu()
# # tracer(0)
# # screensize(3000,3000)
# # for cluster in clusters:
# #     color = random(), random(), random()
# #     for point in cluster:
# #         goto(point[0] * 50, point[1] * 50)
# #         dot(4, color)
# # done()
# # 2 нахождение центров
# from math import dist
# def centroid(cluster):
#     points_with_distances = []
#     for point in cluster:
#         distances = [dist(point, point2) for point2 in cluster]
#         points_with_distances.append([sum(distances), point])
#     return min(points_with_distances)[1]
# centroids = [centroid(cluster) for cluster in clusters]
# print([c for c in centroids])
# # # 3 находим ответ
# mid_x = sum([x for x,y in centroids]) / len(clusters) * 10_000
# mid_y = sum([y for x,y in centroids]) / len(clusters) * 10_000
# print(int(mid_x), int(mid_y))

'''var1'''
# # DBscan (Wrong)
# data = []
# for i in open('var1A.txt'):
#     x,y = map(float, i.split())
#     data.append([x,y])
# from math import dist
# # def dist(p1,p2):
# #     x1,y1 = p1
# #     x2,y2 = p2
# #     return ((x1-x2)**2 + (y1-y2)**2) ** 0.5
# clusters = []
# while data:
#     cl = [data.pop()]
#     for p in cl:
#         sosed = [p1 for p1 in data if dist(p,p1) < 2]
#         for p1 in sosed:
#             cl.append(p1)
#             data.remove(p1)
#     clusters.append(cl)
# def centroid(cluster):
#     m = []
#     for p in cluster:
#         s = sum(dist(p,p1) for p1 in cl)
#         m.append([s,p])
#     return min(m)[1]
# centroids = [centroid(cl) for cl in clusters]
# print(centroids)
# px = sum(x for x,y in centroids)/len(centroids)
# py = sum(y for x,y in centroids)/len(centroids)
# print(int(px*10000), int(py*10000))
# from turtle import *
# from random import *
# up()
# tracer(0)
# for cl in clusters:
#     color = random(), random(), random()
#     for x,y in cl:
#         goto(x*10, y*10)
#         dot(3,color)
# from math import dist
# def centroid(c):
#     res = []
#     for p1 in c:
#         res.append((sum(dist(p1,p2) for p2 in c), p1))
#     return min(res)[1]
# c = [[],[]]
# for i in open('var1A.txt'):
#     x,y = map(float, i.split())
#     if y > 20:
#         c[0].append([x,y])
#     else:
#         c[1].append([x,y])
# cs = [centroid(cl) for cl in c]
# print(cs, [len(c) for c in c])
# print(int(10_000 * sum(x for x,y in cs) / 2), int(10_000 * sum(y for x,y in cs) / 2))
# up()
# tracer(0)
# for cl in clusters:
#     color = random(), random(), random()
#     for x,y in cl:
#         goto(200-x*10, y*10)
#         dot(3,color)
# done()

'''var2'''
# # 0 открытие файла
# f = open('var2B.txt')
# data = []
# for s in f:
#     s = s.replace(',', '.')
#     x, y = map(float, s.split())
#     data.append([x,y])
# print(len(data))
# # 1 разбиение на кластеры
# # 1.1. аналитика
# #FOR A
# # clusters = [[],[]]
# #FOR B
# clusters = [[],[],[]]
# for point in data:
#     #FOR A
#     # if point[1] > 15:
#     #     clusters[1].append(point)
#     # else:
#     #     clusters[0].append(point)
#
#     #FOR B
#     if point[1] < 0:
#         clusters[0].append(point)
#     else:
#         if point[0] < 0:
#             clusters[1].append(point)
#         else:
#             clusters[2].append(point)
# print([len(x) for x in clusters])
# # 1.1.1* проверочка на разделение
# from turtle import *
# from random import *
# pu()
# tracer(0)
# k = 15
# screensize(3000,3000)
# for cluster in clusters:
#     color = random(), random(), random()
#     for point in cluster:
#         goto(point[0] * k, point[1] * k)
#         dot(4, color)
# done()
# # 2 нахождение центров
# from math import dist
# def centroid(cluster):
#     points_with_distances = []
#     for point in cluster:
#         distances = [dist(point, point2) for point2 in cluster]
#         points_with_distances.append([sum(distances), point])
#     return min(points_with_distances)[1]
# centroids = [centroid(cluster) for cluster in clusters]
# print([c for c in centroids])
# # # 3 находим ответ
# mid_x = sum([x for x,y in centroids]) / len(clusters) * 10_000
# mid_y = sum([y for x,y in centroids]) / len(clusters) * 10_000
# print(int(mid_x), int(mid_y))

'''var6'''
# 0 открытие файла
# from math import dist
# f = open('var6B.txt')
# data = []
# for s in f:
#     s = s.replace(',', '.')
#     x, y = map(float, s.split())
#     data.append([x,y])
# print(len(data))
# # 1 разбиение на кластеры
# # 1.1. аналитика
# #FOR A
# # clusters = [[],[]]
#
# # for point in data:
#     # FOR A
#     # if point[1] > 15:
#     #     clusters[1].append(point)
#     # else:
#     #     clusters[0].append(point)
# #FOR B
# clusters = [[],[],[]]
# for point in data:
#     if point[0] < -5:
#         clusters[0].append(point)
#     else:
#         if point[1] < 0:
#             clusters[1].append(point)
#         else:
#             clusters[2].append(point)
# # 1.2 DBscan
# # clusters = []
# # while data:
# #     cl = [data.pop()]
# #     for p in cl:
# #         sosed = [p1 for p1 in data if dist(p,p1) < 2]
# #         cl = cl + sosed
# #         for p1 in sosed: data.remove(p1)
# #     clusters.append(cl)
#
# print([len(x) for x in clusters])
# # 1.1.1* проверочка на разделение
# from turtle import *
# from random import *
# pu()
# tracer(0)
# k = 15
# screensize(3000,3000)
# for cluster in clusters:
#     color = random(), random(), random()
#     for point in cluster:
#         goto(point[0] * k, point[1] * k)
#         dot(4, color)
# done()
# # 2 нахождение центров
# def centroid(cluster):
#     points_with_distances = []
#     for point in cluster:
#         distances = [dist(point, point2) for point2 in cluster]
#         points_with_distances.append([sum(distances), point])
#     return min(points_with_distances)[1]
# centroids = [centroid(cluster) for cluster in clusters]
# print([c for c in centroids])
# # # 3 находим ответ
# mid_x = sum([x for x,y in centroids]) / len(clusters) * 10_000
# mid_y = sum([y for x,y in centroids]) / len(clusters) * 10_000
# print(abs(int(mid_x)), abs(int(mid_y)))

'''dv'''
# 0 открытие файла
from math import dist
f = open('dv27B.txt')
data = []
for s in f:
    s = s.replace(',', '.')
    x, y = map(float, s.split())
    data.append([x,y])
print(len(data))
# 1 разбиение на кластеры
# 1.1. аналитика
#FOR A
# clusters = [[],[]]
# for point in data:
    # FOR A
    # if point[1] > 15:
    #     clusters[1].append(point)
    # else:
    #     clusters[0].append(point)
#FOR B
# clusters = [[],[],[]]
# for point in data:
#     if point[0] < -5:
#         if point[1] > -5:
#             clusters[0].append(point)
#     else:
#         if point[1] < 5:
#             clusters[1].append(point)
#         elif point[1] > 5 > point[0]:
#             clusters[2].append(point)
# 1.2 DBscan
clusters = []
while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p,p1) < 2]
        cl = cl + sosed
        for p1 in sosed: data.remove(p1)
    clusters.append(cl)

print([len(x) for x in clusters])
clusters = [cl for cl in clusters if len(cl) > 5]
# 1.1.1* проверочка на разделение
from turtle import *
from random import *
pu()
tracer(0)
k = 15
screensize(3000,3000)
for cluster in clusters:
    color = random(), random(), random()
    for point in cluster:
        goto(point[0] * k, point[1] * k)
        dot(4, color)
done()
# 2 нахождение центров
def centroid(cluster):
    points_with_distances = []
    for point in cluster:
        distances = [dist(point, point2) for point2 in cluster]
        points_with_distances.append([sum(distances), point])
    return min(points_with_distances)[1]
centroids = [centroid(cluster) for cluster in clusters]
print([c for c in centroids])
# # 3 находим ответ
mid_x = sum([x for x,y in centroids]) / len(clusters) * 10_000
mid_y = sum([y for x,y in centroids]) / len(clusters) * 10_000
print(abs(int(mid_x)), abs(int(mid_y)))