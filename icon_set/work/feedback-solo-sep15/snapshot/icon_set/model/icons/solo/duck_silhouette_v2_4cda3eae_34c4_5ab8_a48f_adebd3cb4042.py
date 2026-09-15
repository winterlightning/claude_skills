"""Enlarge the bill and round the breast and tail into a coherent duck outline; place the eye inside the round head. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4cda3eae-34c4-5ab8-a48f-adebd3cb4042'
SOURCE_PATH = 'pictographic-primitives/animals/chick_4cda3eae-34c4-5ab8-a48f-adebd3cb4042.svg'
AUTHOR = 'gpt-6'

class DuckSilhouetteVariant2(Solo48):
    icon_id = 'duck-silhouette-v2'
    variant_of = 'duck-silhouette'
    variant_label = 'Enlarge the bill and round the breast and tail into a coherent duck outline; place the eye inside the round head.'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('duck', 'bird', 'rubber duck', 'toy', 'bath', 'silhouette', 'poultry', 'minimal')

    def build(self):
        """Symbol plan: Enlarge the bill and round the breast and tail into a coherent duck outline; place the eye inside the round head. Reference: Lucide bird: round head, dot eye, and one coherent silhouette."""

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
        path('duck', (20, 18), [('A', (30, 8), 10, 10, True), ('A', (38, 16), 8, 8, True), ('L', (44, 16)), ('L', (44, 24)), ('L', (38, 24)), ('C', (24, 40), (38, 34), (32, 40)), ('C', (4, 24), (12, 40), (4, 34)), ('L',(4,16)),('C',(14,24),(8,22),(10,24)),('C',(20,20),(18,24),(20,24)), ('L', (20, 18))], True)
        dot('eye', (30, 18))
