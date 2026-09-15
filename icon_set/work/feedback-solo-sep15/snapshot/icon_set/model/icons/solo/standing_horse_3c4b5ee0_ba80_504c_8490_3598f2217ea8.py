"""Corrected keyshape selection to match the existing square proportions.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3c4b5ee0-ba80-504c-8490-3598f2217ea8'
SOURCE_PATH = 'pictographic-primitives/animals/animal horse_3c4b5ee0-ba80-504c-8490-3598f2217ea8.svg'
AUTHOR = 'gpt-6'

class StandingHorse(Solo48):
    icon_id = 'standing-horse'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('horse', 'pony', 'stallion', 'equine', 'animal', 'farm', 'riding', 'profile')

    def build(self):
        # Plan: Horse silhouette retains pointed ear, muzzle, two clear legs and curved tail. Paired leg widths share eight-unit spacing; directional stance remains asymmetric.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        poly('horse',(4,18),(12,14),(16,8),(20,20),(36,20),(36,40),(28,40),(28,28),(20,28),(20,40),(12,40),(12,28),(4,24),closed=True)
        path('tail',(36,20), [('C',(44,32),(44,20),(44,24))]);join('tail','horse')
