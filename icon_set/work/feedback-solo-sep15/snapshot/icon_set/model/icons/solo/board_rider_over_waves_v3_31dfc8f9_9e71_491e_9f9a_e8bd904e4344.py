"""Rebuild the board rider with an aligned head and continuous alternating wave curves. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '31dfc8f9-9e71-491e-9f9a-e8bd904e4344'
SOURCE_PATH = 'pictographic-primitives/sports/skating_31dfc8f9-9e71-491e-9f9a-e8bd904e4344.svg'
AUTHOR = 'gpt-6'

class BoardRiderOverWavesVariant3(Solo48):
    icon_id = 'board-rider-over-waves-v3'
    variant_of = 'board-rider-over-waves'
    variant_label = 'Rebuild the board rider with an aligned head and continuous alternating wave curves.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('board', 'rider', 'wave', 'water', 'balance', 'sport')

    def build(self):
        """Symbol plan: Rebuild the board rider with an aligned head and continuous alternating wave curves. Reference: icon_set/references/human_ref/full_body_ref.png: circular head, coherent limbs, exact 4-unit detached head-to-torso gap."""

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
        oval('head', 18, 9, 3, 3)
        line('torso', (18, 20), (18, 24))
        line('arm', (6, 20), (18, 20))
        join('arm', 'torso')
        poly('legs', (18, 24), (30, 24), (34, 32))
        join('legs', 'torso')
        line('rear-leg', (18, 24), (14, 32))
        join('rear-leg', 'torso')
        join('rear-leg', 'legs')
        poly('board', (8, 32), (14, 32), (34, 32), (42, 24))
        join('board', 'rear-leg')
        join('board', 'legs')
        path('water',(6,42),[('C',(15,40),(9,42),(12,40)),('C',(24,42),(18,40),(21,42)),('C',(33,40),(27,42),(30,40)),('C',(42,42),(36,40),(39,42))])
        self.mark_human_figure('rider', head='head', torso='torso', torso_junction='start')

