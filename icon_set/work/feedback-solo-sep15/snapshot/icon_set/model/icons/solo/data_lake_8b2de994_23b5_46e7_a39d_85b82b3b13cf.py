"""data-lake: Regular water-storage cylinder; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8b2de994-23b5-46e7-a39d-85b82b3b13cf'
SOURCE_PATH = 'pictographic-primitives/programing/data lake_8b2de994-23b5-46e7-a39d-85b82b3b13cf.svg'
AUTHOR = 'gpt-6'

class DataLake(Solo48):
    icon_id = 'data-lake'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('solo-ai-full-set', 'data-lake')

    def build(self):
        # Plan: Keep the elliptical tank and two ripple bands; center every wave band and share side attachments.
        # Reference: Original subject; preserve the distinctive silhouette and proportions.

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
        self.add_arc('top-a',(8,7),(40,7),radius_x=16,radius_y=3)
        self.add_arc('top-b',(40,7),(8,7),radius_x=16,radius_y=3)
        self.add_contour('top','top-a','top-b',closed=True)
        path('body',(8,7),[('L',(8,22)),('L',(8,32)),('L',(8,40)),('A',(40,40),16,4,False),('L',(40,32)),('L',(40,22)),('L',(40,7))]);join('body','top')
        for y in [22,32]:
         commands=[]
         for j,x in enumerate([8,16,24,32]):commands.append(('C',(x+8,y),(x+2,y+(-1 if j%2 else 1)),(x+6,y+(-1 if j%2 else 1))))
         path(f'ripple-{y}',(8,y),commands);join(f'ripple-{y}','body')
