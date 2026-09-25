"""A front-facing spacecraft has a rounded upper cabin above a boxy body and two side pods. A circular upper window and square central panel sit above three evenly spaced flared engine nozzles.

HRECT_XL visible bounds (2,6)-(46,42); rounded cabin, side pods and three equally spaced engines. Central square panel omitted to preserve the window and engines. Lucide rocket informed engine hierarchy; bilateral symmetry and shared nozzle dimensions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd00911d-64ad-4cc3-8476-5c6417280480'
SOURCE_PATH = 'pictographic-primitives/science/fiction ship_fd00911d-64ad-4cc3-8476-5c6417280480.svg'
AUTHOR = 'gpt-6'

class ThreeEngineSpacecraft(Solo48):
    icon_id = 'three-engine-spacecraft'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('spacecraft', 'engine', 'cabin', 'rocket', 'nozzle', 'space')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        # Plan: Symmetric arched cabin, circular window and three equal eight-unit engine openings; replace narrow flared nozzle necks.

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
        path('hull',(12,20), [('A',(36,20),12,12,True),('L',(44,24)),('L',(44,32)),('L',(36,32)),('L',(28,32)),('L',(20,32)),('L',(12,32)),('L',(4,32)),('L',(4,24)),('L',(12,20))],True)
        circle('window',24,20,3)
        for j,x in enumerate((8,24,40)):
         poly(f'engine-{j}',(x-4,32),(x-4,40),(x+4,40),(x+4,32));join(f'engine-{j}','hull')
