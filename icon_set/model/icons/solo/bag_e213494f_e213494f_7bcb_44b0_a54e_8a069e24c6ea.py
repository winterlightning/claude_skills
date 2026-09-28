"""bag-e213494f: Rounded bucket bag; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e213494f-7bcb-44b0-a54e-8a069e24c6ea'
SOURCE_PATH = 'pictographic-primitives/shopping/bag_e213494f-7bcb-44b0-a54e-8a069e24c6ea.svg'
AUTHOR = 'gpt-6'

class BagE213494f(Solo48):
    icon_id = 'bag-e213494f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'bag-e213494f')

    def build(self):
        # Plan: A bucket-shaped bag has a broad rounded bottom and a low circular handle. The continuous bowl-shaped base contrasts with the straight-bottom totes.
        # Reference: Lucide handbag: original and atomic-debug geometry.

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
        path('handle',(16,16),[('L',(16,12)),('A',(32,12),8,8,True),('L',(32,16))])
        path('body',(8,16),[('L',(16,16)),('L',(32,16)),('L',(40,16)),('L',(38,32)),('C',(24,44),(37,40),(30,44)),('C',(10,32),(18,44),(11,40)),('L',(8,16))],True)
        join('handle','body')
