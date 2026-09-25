"""curtains-open: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4f732af1-71a8-516e-aec3-32b7c620ce19'
SOURCE_PATH = 'pictographic-primitives/building/curtains open_4f732af1-71a8-516e-aec3-32b7c620ce19.svg'
AUTHOR = 'gpt-6'

class CurtainsOpen(Solo48):
    icon_id = 'curtains-open'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('curtains', 'open', 'building', 'solo-ai-next100')

    def build(self):
        # Plan: Two tied-back curtain panels mirror about a clear center opening. Shared tie nodes and generous lower folds preserve the drape.
        # Reference: No useful exact Lucide match; supplied original silhouette.

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
        poly('rod',(6,6),(18,6),(30,6),(42,6))
        for side in (-1,1):
         x=lambda d:24+side*d
         path(f'panel-{side}',(x(6),6),[('L',(x(18),6)),('L',(x(18),25)),('L',(x(18),42)),('L',(x(8),42)),('C',(x(9),25),(x(8),34),(x(8),29)),('C',(x(6),6),(x(6),20),(x(6),13))],True)
         line(f'tie-{side}',(x(18),25),(x(9),25));join(f'tie-{side}',f'panel-{side}');join(f'panel-{side}','rod')
