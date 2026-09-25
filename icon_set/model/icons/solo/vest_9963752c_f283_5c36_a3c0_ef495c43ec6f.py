"""vest: Balanced vest panels; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9963752c-f283-5c36-a3c0-ef495c43ec6f'
SOURCE_PATH = 'pictographic-primitives/clothes/vest_9963752c-f283-5c36-a3c0-ef495c43ec6f.svg'
AUTHOR = 'gpt-6'

class Vest(Solo48):
    icon_id = 'vest'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('solo-ai-full-set', 'vest')

    def build(self):
        # Plan: Preserve the open vest front and neckline; paired straps and smooth armholes share exact nodes.
        # Reference: Lucide shirt: original and atomic-debug geometry.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
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
        commands=[('L',(20,4))]
        if True:commands += [('L',(24,18)),('L',(28,4))]
        else:commands += [('C',(24,14),(20,10),(21,14)),('C',(28,4),(27,14),(28,10))]
        commands += [('L',(36,4)),('C',(40,20),(36,14),(36,17)),('L',(40,42)),('L',(28,44)),('L',(24,40)),('L',(20,44)),('L',(8,42)),('L',(8,20)),('C',(12,4),(12,17),(12,14))]
        path('vest',(12,4),commands,True)
        line('seam',(24,18),(24,40));join('seam','vest')
