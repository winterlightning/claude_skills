"""Enlarge the bill and round the breast and tail into a coherent duck outline; place the eye inside the round head. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4cda3eae-34c4-5ab8-a48f-adebd3cb4042'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__duck-silhouette/20260927T060349Z-thuan-mac-1/reference/chick_4cda3eae-34c4-5ab8-a48f-adebd3cb4042.svg'
AUTHOR = 'gpt-6'

class DuckSilhouette(Solo48):
    icon_id = 'duck-silhouette'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
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
        # Smooth back, round head, paired bill strokes and full belly follow the source silhouette.
        path('duck', (6,20), [
            ('C',(18,25),(8,27),(14,27)),
            ('C',(24,21),(22,25),(23,23)),
            ('C',(24,16),(25,19),(23,18)),
            ('C',(34,8),(24,10),(29,8)),
            ('C',(40,17),(39,8),(40,12)),
            ('L',(44,15)), ('L',(41,18)), ('L',(44,21)), ('L',(39,20)),
            ('C',(36,31),(39,24),(37,28)),
            ('C',(24,40),(34,38),(29,40)),
            ('C',(4,31),(13,40),(4,38)),
            ('C',(6,20),(4,27),(4,22)),
        ], True)
