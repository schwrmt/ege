'''color_box'''
# f = open('color_box.txt')
# boxes = []
# for s in f:
#     b = list(map(int, s.split()))
#     if len(b) == 2:
#         boxes.append((b[0], 'R'))
#         boxes.append((b[1], 'B'))
#     else:
#         boxes.append((b[0], 'R'))
# boxes = sorted(boxes, reverse=True)
# added_boxes = [boxes[0]]
# for b in boxes:
#     last_added_box = added_boxes[-1]
#     if last_added_box[0] - b[0] >= 5 and last_added_box[1] != b[1]:
#         added_boxes.append(b)
# print(len(added_boxes), added_boxes[-1][0])

'''ege2023_1'''
# f = open('ege2023_1.txt')
# n = int(f.readline())
# events = [list(map(int,x.split())) for x in f]
# for i in range(n):
#     events[i] = [events[i][1], events[i][0]] #меняем конец с началом, чтобы отсортировать по концам
# events = sorted(events)
# approved_event = [events[0]]
# for event in events:
#     last_approved_event = approved_event[-1]
#     if event[1] >= last_approved_event[0]:
#         approved_event.append(event)
# min_start_time_for_last_approved_event = approved_event[-2][0]
# for i in range(n-1,-1,-1):
#     event = events[i]
#     if min_start_time_for_last_approved_event <= event[1] and approved_event[-1][0] < event[0]:
#         approved_event = approved_event[:-1] + [event]
#         break
# print(len(approved_event), approved_event[-1][0])

'''3B2A3F'''
# f = open('3B2A3F.txt')
# n = int(f.readline())
# events = [list(map(int,x.split())) for x in f]
# for i in range(n):
#     events[i] = [events[i][1], events[i][0]] #меняем конец с началом, чтобы отсортировать по концам
# events = sorted(events)
# approved_event = [events[0]]
# for event in events:
#     last_approved_event = approved_event[-1]
#     if event[1] >= last_approved_event[0]:
#         approved_event.append(event)
# min_start_time_for_last_approved_event = approved_event[-2][0]
# for i in range(n):
#     event = events[i]
#     if min_start_time_for_last_approved_event <= event[1] and approved_event[-1][1] < event[1]:
#         approved_event = approved_event[:-1] + [event]
# max_timeout_for_last_2_event = approved_event[-1][1] - approved_event[-2][0]
# print(len(approved_event), max_timeout_for_last_2_event)

'''var1'''
# f = open('var1.txt')
# n, m, k = map(int, f.readline().split())
# vert_rows = [] # вертикальные ячейки
# for i in range(k):
#     vert_rows.append([0]*m) #добавляем горизонт. ячейки
# free_cells = [-1] * k
# for cell_ship in f:
#     h, v = map(int, cell_ship.split())
#     vert_rows[v-1][h-1] = 1
# for j in range(k):
#     vert_row = vert_rows[j]
#     for i in range(m):
#         if vert_row[i] == 1:
#             free_cells[j] = i - 1
#             break
# max_hor_cell_for_ship = 0
# for i in range(k-1):
#     if min(free_cells[i], free_cells[i+1]) + 1 > max_hor_cell_for_ship:
#         max_hor_cell_for_ship = min(free_cells[i], free_cells[i+1]) + 1
#         min_vert_cell_for_ship = i + 1
# print(max_hor_cell_for_ship, min_vert_cell_for_ship)
# BEST
# f = open('var1.txt')
# n, m, k = map(int, f.readline().split())
# cells_with_ships = [list(map(int, x.split())) for x in f]
# cells_with_ships = sorted(cells_with_ships)
# free_vert_cell = [m] * (k + 1)
# for cell in cells_with_ships:
#     if free_vert_cell[cell[1]] == m:
#         free_vert_cell[cell[1]] = cell[0]
# max_hor_cell_for_2_ship = 0
# for i in range(1, len(free_vert_cell) - 2):
#     if min(free_vert_cell[i], free_vert_cell[i+1]) - 1 > max_hor_cell_for_2_ship:
#             max_hor_cell_for_2_ship = min(free_vert_cell[i], free_vert_cell[i+1]) - 1
#             min_vert_cell_for_ship = i
# print(max_hor_cell_for_2_ship, min_vert_cell_for_ship)

'''var2'''
# f = open('var1.txt')
# n, m, k = map(int, f.readline().split())
# cells_with_ships = [list(map(int, x.split())) for x in f]
# cells_with_ships = sorted(cells_with_ships)
# free_vert_cell = [m] * (k + 1)
# for cell in cells_with_ships:
#     if free_vert_cell[cell[1]] == m:
#         free_vert_cell[cell[1]] = cell[0]
# max_hor_cell_for_2_ship = 0
# for i in range(1, len(free_vert_cell) - 2):
#     if min(free_vert_cell[i], free_vert_cell[i+1], free_vert_cell[i+2]) - 1 > max_hor_cell_for_2_ship:
#             max_hor_cell_for_2_ship = min(free_vert_cell[i], free_vert_cell[i+1], free_vert_cell[i+2]) - 1
#             max_vert_cell_for_ship = i + 2
# print(max_hor_cell_for_2_ship, max_vert_cell_for_ship)

'''var3'''
# f = open('var3.txt')
# n, m, k = map(int, f.readline().split())
# cells_with_ships = [list(map(int,x.split())) for x in f]
# cells_with_ships = [[vert,hor] for hor,vert in cells_with_ships] # меняем верт. и гор. номера местами
# cells_with_ships = sorted(cells_with_ships) # сортируем по вертикальным номерам
# dist_hor_vert = [(cells_with_ships[0][1] - 2, cells_with_ships[0][1] - 1, cells_with_ships[0][0])]
# for i in range(n-1):
#     cell = cells_with_ships[i]
#     cell_next = cells_with_ships[i+1]
#     if cell[0] == cell_next[0]:
#         dist_hor_vert.append((cell_next[1] - cell[1] - 2, cell_next[1] - 1, cell[0]))
#     else:
#         dist_hor_vert.append((cell_next[1]-2, cell_next[1]-1,cell_next[0])) # до верха
#         dist_hor_vert.append((m - cell[1] - 1, m, cell[0])) #от низа
# # Надо бы ещё сделать проверку на то, что вертикальный ряд вообще не содержит кораблей и тогда у него максимальная дистанция от низа до верха
# print(sorted(dist_hor_vert, reverse=True)[:5])

'''var4'''
# f = open('var4.txt')
# n, m, k = map(int, f.readline().split())
# cells_with_ships = [list(map(int,x.split())) for x in f]
# cells_with_ships = [[vert,hor] for hor,vert in cells_with_ships] # меняем верт. и гор. номера местами
# cells_with_ships = sorted(cells_with_ships) # сортируем по вертикальным номерам
# max_distance = cells_with_ships[0][1]
# max_hor = -1
# max_vert = -1
# for i in range(n-1):
#     cell = cells_with_ships[i]
#     cell_next = cells_with_ships[i+1]
#     if cell[0] == cell_next[0] and max_distance < cell_next[1] - cell[1] - 2:
#         max_distance = cell_next[1] - cell[1] - 2
#         max_hor = cell_next[1] - 1
#         max_vert = cell[0]
#     elif cell[0] != cell_next[0] and max_distance < m - cell[1] - 1: # от нижней ячейки
#         max_distance = m - cell[1]  - 1
#         max_hor = m
#         max_vert = cell[0]
#     elif cell[0] != cell_next[0] and max_distance < cell_next[1] - 2: # от кораблика до самой верхней
#         max_distance = cell_next[1]  - 2
#         max_hor = cell_next[1] - 1
#         max_vert = cell_next[0]
# # Надо бы ещё сделать проверку на то, что вертикальный ряд вообще не содержит кораблей и тогда у него максимальная дистанция от низа до верха
# print(max_hor, max_distance, max_vert)

'''var5'''
# f = open('var5.txt')
# n = int(f.readline())
# events = [list(map(int,x.split())) for x in f]
# for i in range(n):
#     events[i] = [events[i][0] + events[i][1], events[i][0]] #вместо начало+длительность делаем конец+начало
# events = sorted(events)
# approved_event = [events[0]]
# for event in events:
#     last_approved_event = approved_event[-1]
#     if event[1] >= last_approved_event[0]:
#         approved_event.append(event)
# min_start_time_for_last_approved_event = approved_event[-2][0]
# for i in range(n):
#     event = events[i]
#     if min_start_time_for_last_approved_event <= event[1] and approved_event[-1][1] < event[1]:
#         approved_event = approved_event[:-1] + [event]
# max_timeout_for_last_2_event = approved_event[-1][1] - approved_event[-2][0]
# print(len(approved_event), max_timeout_for_last_2_event)

'''var6'''
# f = open('var6.txt')
# n = int(f.readline())
# events = [list(map(int,x.split())) for x in f]
# for i in range(n):
#     events[i] = [events[i][0] + events[i][1], events[i][0]] #вместо начало+длительность делаем конец+начало
# events = sorted(events)
# approved_event = [events[0]]
# for event in events:
#     last_approved_event = approved_event[-1]
#     if event[1] >= last_approved_event[0]:
#         approved_event.append(event)
# min_start_time_for_last_approved_event = approved_event[-2][0]
# for i in range(n):
#     event = events[i]
#     if min_start_time_for_last_approved_event <= event[1] and approved_event[-1][1] < event[1]:
#         approved_event = approved_event[:-1] + [event]
# max_timeout_for_last_2_event = approved_event[-1][1] - approved_event[-2][0]
# print(len(approved_event), max_timeout_for_last_2_event)

'''var7'''
# f = open('var7.txt')
# n = int(f.readline())
# squares = [list(map(int, x.split())) for x in f]
# squares = sorted(squares, reverse=True)
# added_squares = [squares[0]]
# for square in squares:
#     if square[0] + square[1] <= added_squares[-1][0]:
#         added_squares.append(square)
# added_squares_with_distances = []
# for square in added_squares:
#     if square[0] < 0:
#         added_squares_with_distances.append((abs(square[0] + square[1]), square[0]))
#     else:
#         added_squares_with_distances.append((square[0], square[0]))
# added_squares_with_distances = sorted(added_squares, key=lambda x: x[0])
# for square in squares:
#     sq_dist = 0
#     if square[0] > 0:
#         sq_dist = square[0]
#     else:
#         sq_dist = abs(square[0]) + square[1]
#     if sq_dist > added_squares_with_distances[-1][0] and square[0] + square[1] > added_squares_with_distances[-2][1]:
#         del added_squares_with_distances[-1]
#         added_squares_with_distances.append((sq_dist, square[0]))
# print(len(added_squares), abs(added_squares_with_distances[-1][1] - added_squares_with_distances[-2][1]))

# f = open('var7.txt')
# n = int(f.readline())
# squares = [list(map(int, x.split())) for x in f]
# squares = [[left_end, left_end+side_len] for left_end, side_len in squares] #добавляем правый край
# squares = sorted(squares, key=lambda x: (x[1])) #сортируем по правому верхнему краю
# added_squares = [squares[0]]
# for square in squares:
#     if square[0] > added_squares[-1][1]:
#         added_squares.append(square)
# added_squares = sorted(added_squares, key=lambda x: abs(x[0]))
# for square in squares:
#     if square[0] > added_squares[-1][0] and square[0] > added_squares[-2][1]:
#         del added_squares[-1]
#         added_squares.append(square)
# print(len(added_squares), added_squares[-1][0] - added_squares[-2][0])

'''B3C563'''
# f = open('B3C563.txt')
# k = int(f.readline()) #кол-во ячеек
# n = int(f.readline()) #кол-во туристов
# data = sorted([list(map(int,x.split())) for x in f])
# cells = [-1] * k
# cnt = 0
# last_cell = -1
# for start, end in data:
#    for i in range(k):
#        if start > cells[i]:
#            cells[i] = end
#            cnt += 1
#            last_cell = i + 1
#            break
# print(cnt,last_cell)

'''dosrok2023'''
# f = open('dosrok2023.txt')
# count_cells = int(f.readline())
# n = int(f.readline())
# appeals = sorted([list(map(int,x.split())) for x in f])
# cells = [-1] * count_cells #время до скольки заняли i-ую ячейку
# cnt = 0
# for start, end in appeals:
#     for i in range(count_cells):
#         if start > cells[i]:
#             cells[i] = end
#             cnt += 1
#             break
# print(cnt,i+1)

'''dosrok2022'''
# f = open('dosrok2022.txt')
# f.readline()
# seats = [list(map(int,x.split())) for x in f]
# seats = sorted(seats, reverse=True)
# max_row = -1
# min_seat = 0
# for i in range(len(seats)-1):
#     seat1, seat2 = seats[i], seats[i+1]
#     if seat1[0] == seat2[0] and seat1[1] - seat2[1] == 12:
#         max_row = seat1[0]
#         min_seat = seat2[1] + 1
#     if max_row > seat2[0]:
#         break
# print(max_row,min_seat)

'''EGE2021'''
# f = open('EGE2021.txt')
# f.readline()
# seats = [list(map(int,x.split())) for x in f]
# seats = sorted(seats, reverse=True)
# max_row = -1
# min_seat = 0
# for i in range(len(seats)-1):
#     seat1, seat2 = seats[i], seats[i+1]
#     if seat1[0] == seat2[0] and seat1[1] - seat2[1] == 3:
#         max_row = seat1[0]
#         min_seat = seat2[1] + 1
#     if max_row > seat2[0]:
#         break
# print(max_row,min_seat)

'''ege2023_2'''
# f = open('ege2023_2.txt')
# n = int(f.readline())
# data = [list(map(int, x.split())) for x in f]
# grid = []
# paint = []
# for i in range(len(data)):
#     detail = data[i]
#     if detail[0] < detail[1]:
#         grid.append((detail[0],i+1))
#     else:
#         paint.append((detail[1], i+1))
# grid = sorted(grid)
# paint = sorted(paint, reverse=True)
# if grid[-1] > paint[0]:
#     last_detail = grid[-1][1]
#     cnt = len(grid[:-1])
# else:
#     last_detail = paint[0][1]
#     cnt = len(grid)
# print(last_detail, cnt)

'''ege2023_3'''
# f = open('ege2023_3.txt')
# n = int(f.readline())
# data = [list(map(int, x.split())) for x in f]
# cnt_for_time = {}
# for start, end in data:
#     cnt_for_time[start] = 1 if start not in cnt_for_time else cnt_for_time[start] + 1
#     cnt_for_time[end] = -1 if end not in cnt_for_time else cnt_for_time[end] - 1
# cnt_for_time = dict(sorted(cnt_for_time.items()))
# inside = [0]
# for t in cnt_for_time:
#     if cnt_for_time[t] != 0:
#         inside.append(inside[-1] + cnt_for_time[t])
# print(inside.count(max(inside)),max(inside))
#
# f = open('ege2023_3.txt')
# n = int(f.readline())
# visits = [list(map(int,s.split())) for s in f]
# visits = sorted(visits)
# cnt_in_timeline = [0] * 1441
# for visit in visits:
#     for i in range(visit[0],visit[1]):
#         cnt_in_timeline[i] += 1
# peak = max(cnt_in_timeline)
# peak_cnt = 0
# for i in range(len(cnt_in_timeline)):
#     cnt_people = cnt_in_timeline[i]
#     if cnt_people == peak and cnt_in_timeline[i-1] != peak:
#         peak_cnt += 1
# print(peak_cnt, peak)

'''dosrok2023'''
# f = open('dosrok2023.txt')
# k = int(f.readline()) #кол-во ячеек
# n = int(f.readline()) #кол-во туристов
# data = sorted([list(map(int,x.split())) for x in f])
# cells = [-1] * k
# cnt = 0
# last_cell = -1
# for start, end in data:
#     for i in range(k):
#         if start > cells[i]:
#             cells[i] = end
#             cnt += 1
#             last_cell = i + 1
#             break
# print(cnt,last_cell)

'''EGKR240424'''
# f = open('EGKR270424.txt')
# max_weight, n = map(int,f.readline().split())
# f = [int(x) for x in f]
# f = sorted(f)
# current_weight = 0
# cnt = 0
# last_pack = 0
# for pack in f:
#     if current_weight + pack < max_weight:
#         current_weight += pack
#         cnt += 1
#         last_pack = pack
#     else:
#         break
# free_space = max_weight - (current_weight - last_pack)
# for i in range(len(f)-1, cnt, -1):
#     pack = f[i]
#     if f[i] <= free_space:
#         # current_weight -= last_pack + f[i]
#         last_pack = f[i]
#         break
# print(cnt,last_pack)

'''EGKR161223'''
# f = open('EGKR161223.txt')
# max_weight, n = map(int,f.readline().split())
# f = [int(x) for x in f]
# f = sorted(f)
# storage = []
# for pack in f:
#     if sum(storage) + pack <= max_weight:
#         storage.append(pack)
#     elif sum(storage[:-1]) + pack <= max_weight:
#         del storage[-1]
#         storage.append(pack)
#     else:
#         break
# print(len(storage), max(storage))

'''Dosrok2025'''
# f = open('dosrok2025.txt')
# f.readline()
# f = [int(s) for s in f]
# f = sorted(f, reverse=True)
# cnt = 1
# current_box = f[0]
# for b in f:
#     if current_box - b >= 9:
#         current_box = b
#         cnt += 1
# print(cnt, current_box)

'''Dosrok2024'''
# f = open('dosrok2024.txt')
# f.readline()
# f = [int(s) for s in f]
# f = sorted(f, reverse=True)
# cnt = 1
# current_box = f[0]
# for b in f:
#     if current_box - b >= 8:
#         current_box = b
#         cnt += 1
# print(cnt, current_box)

'''EGE2022Box'''
# f = open('EGE2022Box.txt')
# f.readline()
# f = list(map(int,f.read().split()))
# f = sorted(f, reverse=True)
# current_box = f[0]
# cnt = 1
# for s in f:
#     if current_box - 3 >= s:
#         current_box = s
#         cnt += 1
# print(cnt, current_box)

'''1important'''
# f = open('1Important.txt').read().strip()
# f = list(map(int,f.split()))
# f = sorted(f[1:], reverse=True)
# print(sum(f) - sum(f[:len(f)//3]))
# print(sum(f) - sum([f[i] for i in range(2, len(f), 3)]))

'''2022Rezerv'''
# f = open('2022Rezerv.txt').read().strip()
# f = list(map(int,f.split()))
# f = sorted(f[1:], reverse=True)
# print(sum(f) - sum([f[i] for i in range(5, len(f), 6)]) // 2)
# print(sum(f) - sum(f[-len(f)//6+1:]) // 2)

'''demo2025'''
# f = open('demo_2025_26.txt')
# n = int(f.readline())
# data = [list(map(int, x.split())) for x in f]
# new_data = []
# for d in data:
#     new_data.append((d[1:].count(2), sum(d[1:]) / 4, d[0]))
# new_data = sorted(new_data, key=lambda x: (x[0], -x[1], x[2]))
# first_id_with_3_dvoek = -1
# for i in range(len(new_data)):
#     if new_data[i][0] == 3:
#         first_id_with_3_dvoek = new_data[i][2]
#         break
# print(new_data[n//4-1][2], first_id_with_3_dvoek)

'''ege2024_2'''
# f = open('ege2024_2.txt')
# n, s = map(int, f.readline().split())
# data = [list(map(int,x.split())) for x in f]
# students = [[_id, grade1 + grade2 + grade3, sobes] for _id, grade1, grade2, grade3, sobes in data]
# students = sorted(students, key=lambda x: (-x[1], -x[2], x[0]))
# polyprohod_ball = students[s-1][1]
# last_id_with_prohod_ball = -1
# cnt_stud_with_polyprohod = 0
# for stud in students:
#     if stud[1] > polyprohod_ball:
#         last_id_with_prohod_ball = stud[0]
#     elif stud[1] == polyprohod_ball:
#         cnt_stud_with_polyprohod += 1
#     else:
#         break
# print(last_id_with_prohod_ball, cnt_stud_with_polyprohod)