"""Recompose the antenna phone horizontally with a landscape body and clear screen division. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '77811bbb-bdab-5163-82d0-2aa453a8554b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__antenna-mobile-phone/20260926T064521Z-thuan-mac/reference/mobile phone blackberry_77811bbb-bdab-5163-82d0-2aa453a8554b.svg'
AUTHOR = "claude-opus-5-5"

class AntennaMobilePhone(Solo48):
    icon_id = 'antenna-mobile-phone'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('phone', 'mobile', 'antenna', 'handset', 'screen', 'device')

    def build(self):
        """Symbol plan: a portrait antenna phone (revision per review) - taller, narrower body with two horizontal dividers."""

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for i, c in enumerate(commands):
                kind, end, *args = c
                name = f'{n}-{i}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                members.append(name)
                here = end
            self.add_contour(n, *members, closed=closed)

        def oval(n, x, y, rx, ry):
            path(n, (x - rx, y), [('A', (x + rx, y), rx, ry, True), ('A', (x - rx, y), rx, ry, True)], True)

        def box(n, l, t, r, b, rad=4):
            path(n, (l + rad, t), [('L', (r - rad, t)), ('A', (r, t + rad), rad, rad, True), ('L', (r, b - rad)), ('A', (r - rad, b), rad, rad, True), ('L', (l + rad, b)), ('A', (l, b - rad), rad, rad, True), ('L', (l, t + rad)), ('A', (l + rad, t), rad, rad, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        # Revision per review: the body is taller and narrower (portrait, x 10..38, y 12..44 with r4
        # corners) and two horizontal dividers cross it at y 20 and 32 (keypad above, screen band,
        # lower panel as in the reference); the antenna rises from the top-left corner (14, 12)
        # to (14, 4). Divider-to-divider and divider-to-edge gaps are 8 or more.
        l, t, r, b = 10, 12, 38, 44
        path('body', (14, t), [('L', (r - 4, t)), ('A', (r, t + 4), 4, 4, True), ('L', (r, 20)), ('L', (r, 32)),
                               ('L', (r, b - 4)), ('A', (r - 4, b), 4, 4, True), ('L', (l + 4, b)),
                               ('A', (l, b - 4), 4, 4, True), ('L', (l, 32)), ('L', (l, 20)), ('L', (l, t + 4)),
                               ('A', (14, t), 4, 4, True)], True)
        line('antenna', (14, 4), (14, t))
        join('antenna', 'body')
        for y in (20, 32):
            line(f'divider-{y}', (l, y), (r, y))
            join(f'divider-{y}', 'body')
