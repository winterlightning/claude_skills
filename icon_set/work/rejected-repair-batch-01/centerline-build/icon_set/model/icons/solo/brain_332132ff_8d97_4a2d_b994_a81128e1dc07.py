"""brain: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '332132ff-8d97-4a2d-b994-a81128e1dc07'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain_332132ff-8d97-4a2d-b994-a81128e1dc07.svg'
AUTHOR = 'gpt-6'

class Brain(Solo48):
    icon_id = 'brain'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('brain', 'artificial-intelligence', 'solo-ai-next50')

    def build(self):
        # Plan: A frontal brain has matching rounded hemispheres and two shallow folds branching from the central fissure. The folds open toward the lobes rather than forming ear-like loops.
        # Reference: Lucide brain original and atomic-debug construction.

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
        left=[('C',(18,6),(24,8),(22,6)),('C',(12,14),(12,6),(10,10)),('C',(6,24),(8,14),(6,19)),('C',(10,32),(6,28),(6,31)),('C',(18,42),(8,38),(12,42)),('C',(24,36),(22,42),(24,40))]
        path('left',(24,12),left+[('L',(24,18)),('L',(24,12))],True)
        mirror=lambda p:(48-p[0],p[1])
        right=[(k,mirror(e),mirror(a),mirror(b)) for k,e,a,b in left]
        path('right',(24,12),right+[('L',(24,18)),('L',(24,12))],True);join('left','right')
        for side in (-1,1):
         x=lambda d:24+side*d
         path(f'fold-{side}',(24,18),[('C',(x(8),26),(24,23),(x(4),26))])
         join(f'fold-{side}','left');join(f'fold-{side}','right')
