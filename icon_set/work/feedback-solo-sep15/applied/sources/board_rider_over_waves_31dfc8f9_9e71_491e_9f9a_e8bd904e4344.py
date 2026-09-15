"""Windsurfing alternative: circular head, one horizontal arm, raised arm, triangular sail and upward-curved board. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '31dfc8f9-9e71-491e-9f9a-e8bd904e4344'
SOURCE_PATH = 'pictographic-primitives/sports/skating_31dfc8f9-9e71-491e-9f9a-e8bd904e4344.svg'
AUTHOR = 'gpt-6'

class BoardRiderOverWaves(Solo48):
    icon_id = 'board-rider-over-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('board', 'rider', 'wave', 'water', 'balance', 'sport')

    def build(self):
        """Symbol plan: Windsurfing alternative: circular head, one horizontal arm, raised arm, triangular sail and upward-curved board. Reference: icon_set/references/human_ref/full_body_ref.png: circular head, coherent limbs, exact 4-unit detached head-to-torso gap."""

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
        oval('head', 12, 12, 4, 4)
        self.add_bezier('torso', (12, 24), ((12, 27), (14, 30), (16, 32)))
        line('arm-left', (4, 24), (12, 24))
        join('arm-left', 'torso')
        poly('arm-raised', (12, 24), (20, 24), (28, 16))
        join('arm-raised', 'torso')
        join('arm-left', 'arm-raised')
        poly('legs', (12, 40), (16, 32), (28, 40))
        join('legs', 'torso')
        poly('mast', (28, 8), (28, 16), (28, 20), (28, 32), (28, 40))
        poly('sail', (28, 8), (36, 20), (44, 32), (28, 32))
        join('sail', 'mast')
        join('arm-raised', 'mast')
        join('legs', 'mast')
        path('board', (4, 40), [('L', (12, 40)), ('L', (28, 40)), ('L', (36, 40)), ('A', (44, 32), 8, 8, False)])
        join('board', 'legs')
        join('board', 'mast')
        join('board', 'sail')
        self.mark_human_figure('windsurfer', head='head', torso='torso', torso_junction='start')
