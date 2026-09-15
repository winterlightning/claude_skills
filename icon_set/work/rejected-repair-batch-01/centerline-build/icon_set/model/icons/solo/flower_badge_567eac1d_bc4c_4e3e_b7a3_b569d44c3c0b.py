"""flower-badge: Smooth six-lobed outline; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '567eac1d-bc4c-4e3e-b7a3-b569d44c3c0b'
SOURCE_PATH = 'pictographic-primitives/state/flower badge_567eac1d-bc4c-4e3e-b7a3-b569d44c3c0b.svg'
AUTHOR = 'gpt-6'

class FlowerBadge(Solo48):
    icon_id = 'flower-badge'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('solo-ai-full-set', 'flower-badge')

    def build(self):
        # Plan: Six rounded lobes with mirrored valleys; preserve the six-petal badge identity.
        # Reference: Lucide flower: original and atomic-debug geometry.

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
        left=[('C',(17,11),(20,6),(18,8)),('C',(6,18),(11,9),(6,12)),('C',(8,24),(6,21),(8,22)),('C',(6,30),(8,26),(6,27)),('C',(17,37),(6,36),(11,39)),('C',(24,42),(18,40),(20,42))]
        commands=list(left);starts=[(24,6)]+[c[1] for c in left[:-1]]
        for c,start in reversed(list(zip(left,starts))):
         _,end,c1,c2=c
         commands.append(('C',(48-start[0],start[1]),(48-c2[0],c2[1]),(48-c1[0],c1[1])))
        path('outline',(24,6),commands,True)
