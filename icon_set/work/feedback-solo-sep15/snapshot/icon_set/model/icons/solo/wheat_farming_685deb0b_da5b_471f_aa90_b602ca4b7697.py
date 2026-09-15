"""wheat-farming: Balanced wheat sprig; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '685deb0b-da5b-471f-aa90-b602ca4b7697'
SOURCE_PATH = 'pictographic-primitives/farming/wheat_685deb0b-da5b-471f-aa90-b602ca4b7697.svg'
AUTHOR = 'gpt-6'

class WheatFarming(Solo48):
    icon_id = 'wheat-farming'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'farming'
    aliases = ()
    keywords = ('solo-ai-full-set', 'wheat-farming')

    def build(self):
        # Plan: Preserve the single grain head and two broad leaves; share the central stem and mirror the leaf shapes.
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
        path('grain',(24,4),[('C',(32,12),(28,7),(32,7)),('C',(24,20),(32,17),(28,19)),('C',(16,12),(20,19),(16,17)),('C',(24,4),(16,7),(20,7))],True)
        path('stem',(24,20),[('L',(24,34)),('L',(24,44))]);join('stem','grain')
        path('left',(24,34),[('C',(8,27),(22,29),(14,27)),('C',(24,34),(8,34),(16,36))],True)
        path('right',(24,34),[('C',(40,27),(26,29),(34,27)),('C',(24,34),(40,34),(32,36))],True)
        join('left','stem');join('right','stem');join('left','right')
