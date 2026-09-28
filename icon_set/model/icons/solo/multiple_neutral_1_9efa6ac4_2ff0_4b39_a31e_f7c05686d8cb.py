"""multiple-neutral-1: Balanced two-person group; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9efa6ac4-2ff0-4b39-a31e-f7c05686d8cb'
SOURCE_PATH = 'pictographic-primitives/users/multiple neutral 1_9efa6ac4-2ff0-4b39-a31e-f7c05686d8cb.svg'
AUTHOR = 'gpt-6'

class MultipleNeutral1(Solo48):
    icon_id = 'multiple-neutral-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'multiple-neutral-1')

    def build(self):
        # Plan: Human references: user.svg and full_body_ref.png. Two circular heads and open shoulders preserve the group; each detached head has exactly four units of visible clearance to its own shoulder.
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
        circle('front-head',14,15,7);circle('back-head',36,15,6)
        path('front-body',(4,40),[('L',(4,36)),('C',(14,30),(4,32),(10,30)),('C',(26,36),(20,30),(26,32)),('L',(26,40))])
        path('back-body',(36,29),[('C',(44,35),(40,29),(44,32)),('L',(44,40)),('L',(36,40))])
