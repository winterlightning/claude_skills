"""bag-shopping: Folded grocery sack; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '12a6aa6e-010c-419c-b6a1-fd8f3a38bd08'
SOURCE_PATH = 'pictographic-primitives/shopping/bag_12a6aa6e-010c-419c-b6a1-fd8f3a38bd08.svg'
AUTHOR = 'gpt-6'

class BagShopping(Solo48):
    icon_id = 'bag-shopping'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'bag-shopping')

    def build(self):
        # Plan: A folded paper grocery sack uses a rolled upper flap and a side gusset instead of an external loop handle. Intentional perspective distinguishes this bag variant.
        # Reference: Lucide paper-bag: original and atomic-debug geometry.

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
        poly('flap',(12,4),(34,4),(40,12),(20,12),(12,4))
        path('body',(12,4),[('L',(8,20)),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,24)),('L',(36,12))])
        poly('gusset',(12,4),(16,20),(16,44))
        join('flap','body');join('gusset','flap');join('gusset','body')
