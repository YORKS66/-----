from algo import Point, intersect

def correct_coord(coord):
    coord = coord.split(',')
    return Point(int(coord[0]), int(coord[1]))


def main():
    print("Проверка двух отрезков а и б на пересечение")
    print("Важно! Координаты вводятся через запятую!")

    line_1_point_start = input('Введите координаты начала отрезка а:')
    line_1_point_end = input('введите координаты конца отрезка а:')

    line_2_point_start = input('Введите координаты начала отрезка б:')
    line_2_point_end = input('введите координаты конца отрезка б:')

    line_1_point_start = correct_coord(line_1_point_start)
    line_1_point_end = correct_coord(line_1_point_end)
    line_2_point_start = correct_coord(line_2_point_start)
    line_2_point_end = correct_coord(line_2_point_end)

    result = intersect(line_1_point_start, line_1_point_end, \
        line_2_point_start, line_2_point_end)
    print(result)