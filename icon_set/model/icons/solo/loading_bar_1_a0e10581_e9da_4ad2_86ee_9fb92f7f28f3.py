"""loading-bar-1: Regular curved loading bar; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a0e10581-e9da-4ad2-86ee-9fb92f7f28f3'
SOURCE_PATH = 'icons-json/interface-essential/loading bar 1_a0e10581-e9da-4ad2-86ee-9fb92f7f28f3.json'
AUTHOR = 'gpt-6'

class LoadingBar1(Solo48):
    icon_id = 'loading-bar-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('solo-ai-full-set', 'loading-bar-1')

    def build(self):
        # Plan: Matching rounded ends and shared parallel stripe spacing; retain the source stripe count and slant.
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
        tops=[25, 39]
        bottoms=[x-14 for x in tops]
        commands=[('L',(x,8)) for x in tops]+[('L',(38,8)),('C',(44,24),(42,8),(44,14)),('C',(38,40),(44,34),(42,40))]+[('L',(x,40)) for x in reversed(bottoms)]+[('L',(10,40)),('C',(4,24),(6,40),(4,34)),('C',(10,8),(4,14),(6,8))]
        path('body',(10,8),commands,True)
        for j,(a,b) in enumerate(zip(tops,bottoms)):
         line(f'stripe-{j}',(a,8),(b,40));join(f'stripe-{j}','body')
