"""Rebalance the feather into a broader, smoother eye-shaped vane, move the solid dot along its diagonal axis, and join the quill tangentially. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f40b6248-c81f-53b7-82f1-64f0cd1d0e22'
SOURCE_PATH = 'pictographic-primitives/animals/peacock feather_f40b6248-c81f-53b7-82f1-64f0cd1d0e22.svg'
AUTHOR = 'gpt-6'

class PeacockFeather(Solo48):
    icon_id = 'peacock-feather'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('peacock', 'feather')

    def build(self):
        """Symbol plan: Rebalance the feather into a broader, smoother eye-shaped vane, move the solid dot along its diagonal axis, and join the quill tangentially. Reference: Lucide feather: one dominant vane and aligned quill."""

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
        path('vane', (40, 4), [('C', (12, 38), (18, 4), (12, 17)), ('C', (40, 4), (34, 38), (40, 23))], True)
        line('quill', (12, 38), (8, 44))
        join('quill', 'vane')
        dot('eye', (25, 22))
