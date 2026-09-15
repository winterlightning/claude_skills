"""Replace segmented eye curves with coherent mirrored elliptical arcs and exact slash attachment points. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5dce7e9a-2184-434a-9e94-71138d2b612d'
SOURCE_PATH = 'pictographic-primitives/interface-essential/blind_5dce7e9a-2184-434a-9e94-71138d2b612d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Blind(Solo48):
    icon_id = 'blind'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('blind', 'interface-essential')

    def build(self):
        """Symbol plan: Replace segmented eye curves with coherent mirrored elliptical arcs and exact slash attachment points. Reference: Lucide eye: simple mirrored eyelid curves."""

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
        path('eye', (4, 24), [('A', (9, 16), 25, 40, True), ('A', (44, 24), 25, 40, True), ('A', (39, 32), 25, 40, True), ('A', (4, 24), 25, 40, True)], True)
        line('slash', (9, 16), (39, 32))
        join('slash', 'eye')
