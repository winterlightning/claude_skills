"""camping-tent: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0b621e1c-a261-5113-bae2-aea7a2add5c6'
SOURCE_PATH = 'pictographic-primitives/outdoors/camping tent_0b621e1c-a261-5113-bae2-aea7a2add5c6.svg'
AUTHOR = 'gpt-6'

class CampingTent(Solo48):
    icon_id = 'camping-tent'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('camping', 'tent', 'outdoors', 'solo-ai-next100')

    def build(self):
        # Plan: A low wide tent with paired poles and a centered doorway. Mirrored coordinates keep the pitch even.
        # Reference: Lucide tent original and atomic-debug construction.

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
        poly('canvas',(4,40),(24,12),(44,40),(4,40))
        poly('poles',(20,8),(24,12),(28,8));join('poles','canvas')
        poly('door',(16,40),(24,26),(32,40));join('door','canvas')
