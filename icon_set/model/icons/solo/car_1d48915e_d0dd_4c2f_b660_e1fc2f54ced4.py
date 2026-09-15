"""car: Fuller body and inset wheels; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1d48915e-d0dd-4c2f-b660-e1fc2f54ced4'
SOURCE_PATH = 'icons-json/transportation/car_1d48915e-d0dd-4c2f-b660-e1fc2f54ced4.json'
AUTHOR = 'gpt-6'

class Car(Solo48):
    icon_id = 'car'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('solo-ai-cars-refine', 'solo-ai-next100', 'car')

    def build(self):
        # Plan: Restore full round wheels inside the lower body silhouette and a broader compact cabin. Coherent curved shoulders replace thin projecting bumpers.
        # Reference: Lucide car: original and atomic-debug geometry.

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
        path('body',(6,34),[('C',(4,24),(4,32),(4,28)),('C',(10,18),(4,20),(6,18)),('L',(14,10)),('C',(18,8),(15,8),(16,8)),('L',(26,8)),('L',(32,18)),('C',(44,24),(40,18),(44,20)),('C',(42,34),(44,28),(44,32)),('A',(36,40),6,6,True),('A',(30,34),6,6,True),('L',(18,34)),('A',(12,40),6,6,True),('A',(6,34),6,6,True)],True)
        for x in (12,36):
         path(f'wheel-{x}',(x-6,34),[('A',(x,28),6,6,True),('A',(x+6,34),6,6,True)]);join(f'wheel-{x}','body')
