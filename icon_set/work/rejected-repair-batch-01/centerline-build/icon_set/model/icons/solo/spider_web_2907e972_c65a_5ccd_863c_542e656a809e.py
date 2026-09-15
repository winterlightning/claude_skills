from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2907e972-c65a-5ccd-863c-542e656a809e'
SOURCE_PATH = 'pictographic-primitives/animals/spider web_2907e972-c65a-5ccd-863c-542e656a809e.svg'
AUTHOR = 'gpt-6'


class SpiderWeb(Solo48):
    icon_id = 'spider-web'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('spider', 'web', 'cobweb', 'hexagon', 'net', 'halloween', 'geometric', 'trap')

    def build(self):
        # Plan: Six radiating threads meet bowed silk spans; remove the crowded second ring so each web sector retains an open counter.

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
        from itertools import combinations
        points=[(24,6),(42,13),(42,35),(24,42),(6,35),(6,13)]
        controls=[((28,12),(34,14)),((36,18),(36,30)),((34,34),(28,36)),((20,36),(14,34)),((12,30),(12,18)),((14,14),(20,12))]
        nodes=[]
        for j,(a,b) in enumerate(zip(points,points[1:]+points[:1])):
         c,d=controls[j];path(f'web-{j}',a,[('C',b,c,d)]);line(f'ray-{j}',a,(24,24));nodes.extend([(f'web-{j}',{a,b}),(f'ray-{j}',{a,(24,24)})])
        for (a,p),(b,q) in combinations(nodes,2):
         if p&q:join(a,b)
