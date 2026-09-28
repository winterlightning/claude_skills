"""airchair: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2e130f83-d8c1-50d3-98ae-5ea5bac53dab'
SOURCE_PATH = 'pictographic-primitives/symbol/airchair_2e130f83-d8c1-50d3-98ae-5ea5bac53dab.svg'
AUTHOR = 'gpt-6'

class Airchair(Solo48):
    icon_id = 'airchair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('airchair', 'symbol', 'solo-ai-first50')

    def build(self):
        # Plan: Lucide armchair: shared arched back and two rounded arms; broad eight-unit seat band and aligned legs.

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
        path('seat',(8,20), [('A',(12,16),4,4,True),('A',(16,20),4,4,True),('L',(16,28)),('L',(32,28)),('L',(32,20)),('A',(36,16),4,4,True),('A',(40,20),4,4,True),('L',(40,32)),('A',(36,36),4,4,True),('L',(12,36)),('A',(8,32),4,4,True),('L',(8,20))],True)
        path('back',(12,16), [('A',(36,16),12,12,True)])
        join('back','seat')
        for x in (12,36):
         line(f'leg-{x}',(x,36),(x,44));join(f'leg-{x}','seat')
