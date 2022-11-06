from algo import Point, intersect
def test_all():
    all_test_check = True
    line_1_point_start = Point(0, 0)
    line_1_point_end = Point(100, 100)
    
    line_2_point_start = Point(0, 100)
    line_2_point_end = Point(100, 0)

    result = intersect(line_1_point_start, line_1_point_end, \
        line_2_point_start, line_2_point_end)
    if all_test_check:
        all_test_check = result == True

        line_1_point_start = Point(0, 0)
        line_1_point_end = Point(100, 0)

        line_2_point_start = Point(0, 100)
        line_1_point_end = Point(100, 100)

        result = intersect(line_1_point_start, line_1_point_end, \
            line_2_point_start, line_2_point_end)
        if all_test_check:
            all_test_check = result == False

        print('Check All:', all_test_check)

        def test():
            line_1_point_start = Point(0, 0)
            line_1_point_end = Point(100, 100)

            line_2_point_start = Point(0, 100)
            line_2_point_end = Point(100, 0)

            result = intersect(line_1_point_start, line_1_point_end, line_2_point_start, line_2_point_end)
            print('Check:', result == True)

            test()
            test_all()