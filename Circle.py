
def circle(surface, x0, y0, radius, color):
    x, y = radius, 0
    p = 1 - radius
    while x >= y:
        surface.set_at((x0 + x, y0 + y), color)
        surface.set_at((x0 - x, y0 + y), color)
        surface.set_at((x0 + x, y0 - y), color)
        surface.set_at((x0 - x, y0 - y), color)
        surface.set_at((x0 + y, y0 + x), color)
        surface.set_at((x0 - y, y0 + x), color)
        surface.set_at((x0 + y, y0 - x), color)
        surface.set_at((x0 - y, y0 - x), color)
        y += 1
        if p <= 0:
            p += 2 * y + 1
        else:
            x -= 1
            p += 2 * (y - x) + 1

