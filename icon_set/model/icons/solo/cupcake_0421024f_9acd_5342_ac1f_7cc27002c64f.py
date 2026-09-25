"""cupcake: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0421024f-9acd-5342-ac1f-7cc27002c64f'
SOURCE_PATH = 'pictographic-primitives/food/cupcake_0421024f-9acd-5342-ac1f-7cc27002c64f.svg'
AUTHOR = 'gpt-6'

class Cupcake(Solo48):
    icon_id = 'cupcake'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('cupcake', 'food', 'solo-ai-next100')

    def build(self):
        # Plan: Retain the cherry-topped cupcake, scalloped frosting and tapered wrapper; reduce tiny creases to one central wrapper fold.
        # Reference: Lucide cake original and atomic-debug construction.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L":
                    self.add_line(ident, here, end)
                elif kind == "A":
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == "C":
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [("A",(cx+r,cy),r,r,True), ("A",(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ("L",(x1-r,y0)), ("A",(x1,y0+r),r,r,True),
                ("L",(x1,y1-r)), ("A",(x1-r,y1),r,r,True),
                ("L",(x0+r,y1)), ("A",(x0,y1-r),r,r,True),
                ("L",(x0,y0+r)), ("A",(x0+r,y0),r,r,True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate("connect",a,b)
        circle('cherry',24,12,4)
        path('stem',(24,8),[('C',(32,4),(24,4),(28,4))]);join('stem','cherry')
        path('frosting',(8,28),[('C',(20,12),(8,21),(14,14)),('A',(28,12),4,4,False),('C',(40,28),(34,14),(40,21)),('C',(36,31),(39,30),(38,31)),('C',(30,28),(33,31),(32,30)),('C',(24,31),(28,30),(26,31)),('C',(18,28),(22,31),(20,30)),('C',(12,31),(16,30),(15,31)),('C',(8,28),(10,31),(9,30))],True);join('frosting','cherry')
        poly('wrapper',(12,31),(16,44),(32,44),(36,31));join('wrapper','frosting')
        line('fold',(24,31),(24,44));join('fold','wrapper');join('fold','frosting')
