"""Rebuild the sword around one exact 45-degree centerline; straighten and lengthen the grip, use a perpendicular guard, and broaden the symmetrical blade. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2d6ea938-e0f7-53d4-8ee7-1a3662ed24d3'
SOURCE_PATH = 'pictographic-primitives/war/antique sword_2d6ea938-e0f7-53d4-8ee7-1a3662ed24d3.svg'
AUTHOR = 'gpt-6'

class BroadBladedSword(Solo48):
    icon_id = 'broad-bladed-sword'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('broad', 'bladed', 'sword')

    def build(self):
        """Symbol plan: Rebuild the sword around one exact 45-degree centerline; straighten and lengthen the grip, use a perpendicular guard, and broaden the symmetrical blade. Reference: Lucide sword: shared blade/handle axis and perpendicular guard."""

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
        poly('blade', (16, 24), (34, 6), (42, 6), (42, 14), (24, 32))
        poly('guard', (12, 20), (16, 24), (20, 28), (24, 32), (28, 36))
        join('guard', 'blade')
        line('grip', (20, 28), (9, 39))
        join('grip', 'guard')
        poly('pommel', (6, 36), (9, 39), (12, 42))
        join('pommel', 'grip')
