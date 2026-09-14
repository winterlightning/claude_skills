"""atom-other: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e1360ae7-7838-4ce4-ab4c-2158d5dcbebb'
SOURCE_PATH = 'icons-json/other/atom_e1360ae7-7838-4ce4-ab4c-2158d5dcbebb.json'
AUTHOR = 'gpt-6'

class AtomOtherVariant2(Solo48):
    icon_id = 'atom-other-v2'
    variant_of = 'atom-other'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('atom', 'other', 'solo-ai-first50')

    def build(self):
        # Plan: Two smooth diagonal orbital loops use cardinal outer extrema and shared crossing nodes. Omitted the nucleus to maintain clear central negative space.
        # Reference: Lucide original/atom.svg and atomic-debug/atom.svg.

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
        path('orbit-one',(4,12), [('C',(8,8),(4,9),(5,8)),('C',(24,16),(13,8),(19,12)),('C',(44,36),(36,24),(44,30)),('C',(40,40),(44,39),(43,40)),('C',(24,32),(35,40),(29,36)),('C',(4,12),(12,24),(4,18))],True)
        path('orbit-two',(4,36), [('C',(24,16),(4,30),(12,24)),('C',(40,8),(29,12),(35,8)),('C',(44,12),(43,8),(44,9)),('C',(24,32),(44,18),(36,24)),('C',(8,40),(19,36),(13,40)),('C',(4,36),(5,40),(4,39))],True)
        join('orbit-one','orbit-two')

