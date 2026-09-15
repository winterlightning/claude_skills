"""bone: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bdd6c205-c49b-4436-8ff7-3c7c0b842d86'
SOURCE_PATH = 'icons-json/symbol/bone_bdd6c205-c49b-4436-8ff7-3c7c0b842d86.json'
AUTHOR = 'gpt-6'

class Bone(Solo48):
    icon_id = 'bone'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bone', 'symbol', 'solo-ai-next50')

    def build(self):
        # Plan: A horizontal bone uses four matching rounded lobes and a broad shaft. Both axes mirror exactly; removed the traced pinched dents.
        # Reference: Lucide bone original and atomic-debug construction.

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
        path('bone',(14,18),[('C',(9,8),(14,11),(13,8)),('C',(4,14),(5,8),(4,10)),('C',(7,24),(4,19),(7,20)),('C',(4,34),(7,28),(4,29)),('C',(9,40),(4,38),(5,40)),('C',(14,30),(13,40),(14,37)),('L',(34,30)),('C',(39,40),(34,37),(35,40)),('C',(44,34),(43,40),(44,38)),('C',(41,24),(44,29),(41,28)),('C',(44,14),(41,20),(44,19)),('C',(39,8),(44,10),(43,8)),('C',(34,18),(35,8),(34,11)),('L',(14,18))],True)
