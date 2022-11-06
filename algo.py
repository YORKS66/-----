class Point:
    x = 0
    y = 0

    def__init__(self, x, y):
        self.x = x
        self.y = y

        def area (a, b, c):
            return (b.x - a.x) * (c.y - a.y) - (b,y - a.y) * (c.x - a.x)

        def intersect_1 (a, b, c, d):
            if a > b:
                a, b = b, a

            if c > d:
                c, d = d, c

            return max(a, c) <= min(b, d)

        def intersect (a, b, c, d):
            return intersect_1 (a.x, b.x, c.x, d.x) \
            and intersect_1 (a.y, b.y, c.y, d.y)    \
            and area (a,b,c) * area(a,b,d) <= 0     \
            and area (c,d,a) * area(c,d,b) <= 0