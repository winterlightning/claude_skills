"""Enlarge the lion head into a rounded mane with a projecting side muzzle; simplify the wing and remove its crowded inner seam. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '913ea823-995f-439f-bf00-7e196c2b8d57'
SOURCE_PATH = 'pictographic-primitives/animals/leopard_913ea823-995f-439f-bf00-7e196c2b8d57.svg'
AUTHOR = 'gpt-6'

class WingedLion(Solo48):
    icon_id = 'winged-lion'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('winged', 'lion', 'animal')

    def build(self):
        """Symbol plan: Enlarge the lion head into a rounded mane with a projecting side muzzle; simplify the wing and remove its crowded inner seam. Reference: Lucide cat and dog: a projecting muzzle and rounded head; deliberate side profile."""

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
        path('lion', (12, 18), [('L', (12, 10)), ('L', (12, 6)), ('L', (18, 10)), ('C', (24, 24), (26, 8), (26, 18)), ('L', (30, 10)), ('L', (42, 6)), ('C', (36, 28), (42, 16), (40, 24)), ('C', (42, 34), (40, 28), (42, 30)), ('L', (42, 42)), ('L', (34, 42)), ('L', (30, 34)), ('L', (24, 34)), ('L', (20, 42)), ('L', (10, 42)), ('L', (14, 34)), ('L', (12, 30)), ('A', (6, 24), 6, 6, True), ('A', (12, 18), 6, 6, True)], True)
