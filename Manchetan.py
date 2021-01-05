import random
import math

### ПРОГРАММА ВЫЧИСЛЯЕТ РАСТОЯНИЕ ОТ ВЫХОДА ИЗ ДОМА УЧЕНИКА ДО ВХОДА БЛИЖАЙШЕЙ ШКОЛЫ

def nearest_school(schools_exits_and_blocks, body_exits_and_block):
    body_exits = body_exits_and_block[0]
    body_block = body_exits_and_block[1]
    all_schools_exits = []
    all_schools_blocks = []
    for schools in schools_exits_and_blocks:
        all_schools_exits.append(schools[0])
        all_schools_blocks.append(schools[1])
    min_block_dist = [float('inf'), float('inf')]
    block_dists = []
    # Необходимо рассмотреть школы в определенном радиусе от человека, чтобы сократить выборку
    for school_block in all_schools_blocks:
        block_dist = [int(math.fabs(body_block[0] - school_block[0])), int(math.fabs(body_block[1] - school_block[1]))]
        block_dists.append(block_dist)
        if block_dist[0] < min_block_dist[0]:
            min_block_dist[0] = block_dist[0]
        if block_dist[1] < min_block_dist[1]:
            min_block_dist[1] = block_dist[1]
    schools_exits = []
    while schools_exits == []:
        i = 0
        for block_dist in block_dists:
            if(block_dist[0] <= min_block_dist[0]+1 and block_dist[1] <= min_block_dist[1]+1):
                schools_exits.append(all_schools_exits[i])
            i += 1
        min_block_dist[0] += 1
        min_block_dist[1] += 1
    nearest_school = []
    min_dist = float('inf')
    dists = []
    # Ищем ближайшие школы
    for enters in schools_exits:
        ex_min = float('inf')
        for exit in body_exits:
            loc_min = float('inf')
            for enter in enters:
                dist = math.fabs(exit[0] - enter[0]) + math.fabs(exit[1] - enter[1])
                if dist < loc_min:
                    loc_min = dist
            if loc_min < ex_min:
                ex_min = loc_min
        if ex_min < min_dist:
            min_dist = ex_min
        dists.append(ex_min)
    i = 0
    for dist in dists:
        if dist == min_dist:
            # Подходящие школы записываем в массив
            nearest_school.append([schools_exits[i], min_dist])
        i += 1
    return nearest_school


def find_exits_and_block(place, side):
    exits = []
    # Находим выходы на улицу из точек внутри райнов
    bl = place[0]//side
    bw = place[1]//side
    points = [[side*bl, place[1]], [place[0], side*bw], [side*(bl+1), place[1]], [place[0], side*(bw+1)]]
    min_dist = float('inf')
    dists = []
    for point in points:
        dist = int(math.sqrt(((place[0] - point[0])**2) + ((place[1] - point[1])**2)))
        dists.append(dist)
        if (dist < min_dist):
            min_dist = dist
    i = 0
    for dist in dists:
        if min_dist == dist:
            exits.append(points[i])
        i += 1
    bl_bw = [bl+1,bw+1]
    for i in range(2):
        if bl_bw[i] > int(math.sqrt(N_STREATS)):
            bl_bw[i] = bl_bw[i] - 1
    exits_and_block = [exits, bl_bw]
    return exits_and_block


N_STREATS = 25 # Обязательно квадрат целого числа
side = 3
n_schools = 4
schools = []
for i in range(n_schools):
    schools.append([random.randint(0, int(math.sqrt(N_STREATS))*side), random.randint(0, int(math.sqrt(N_STREATS))*side)])
body = [random.randint(0, int(math.sqrt(N_STREATS))*side), random.randint(0, int(math.sqrt(N_STREATS))*side)]
#body = [11,3]
#schools = [[9,12], [7,9], [5,3]]
body_exits_and_block = find_exits_and_block(body, side)
schools_exits_and_blocks = []
for school in schools:
    schools_exits_and_blocks.append(find_exits_and_block(school, side))
right_schools = nearest_school(schools_exits_and_blocks, body_exits_and_block)
print('Наш житель', body_exits_and_block)
print('Школы:')
for school in schools_exits_and_blocks:
    print(school)
for school in right_schools:
    print("Подходит школа", school)