"""cake-cherry: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0c27f58f-0b93-5b1c-8a4f-22dd9939aa7b'
SOURCE_PATH = 'pictographic-primitives/food/cake cherry_0c27f58f-0b93-5b1c-8a4f-22dd9939aa7b.svg'
AUTHOR = 'gpt-6'

class CakeCherry(Solo48):
    icon_id = 'cake-cherry'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('cake', 'cherry', 'food', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the wedge of cake and its round cherry; smooth the curved back and preserve a broad lower cake layer. Add a short natural cherry stem.
        # Reference: Lucide cake-slice original and atomic-debug construction.

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
        circle('cherry',25,16,5)
        path('cake',(4,30),[('C',(20,16),(4,20),(12,16)),('A',(25,21),5,5,False),('A',(30,16),5,5,False),('L',(44,30)),('L',(44,40)),('L',(4,40)),('L',(4,30))],True)
        line('layer',(4,30),(44,30));join('layer','cake');join('cake','cherry')
        path('stem',(25,11),[('C',(35,8),(26,8),(31,8))]);join('stem','cherry')
