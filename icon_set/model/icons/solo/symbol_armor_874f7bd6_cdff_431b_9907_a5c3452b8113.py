"""symbol-armor: Smooth armored vehicle; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '874f7bd6-cdff-431b-9907-a5c3452b8113'
SOURCE_PATH = 'pictographic-primitives/war/symbol armor_874f7bd6-cdff-431b-9907-a5c3452b8113.svg'
AUTHOR = 'gpt-6'

class SymbolArmor(Solo48):
    icon_id = 'symbol-armor'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'symbol-armor')

    def build(self):
        # Plan: Preserve the low rounded body and turret; raise the barrel slightly for a clear gap above the hull.
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
        path('body',(13,20),[('L',(33,20)),('L',(35,20)),('C',(44,30),(41,20),(44,24)),('C',(35,40),(44,36),(41,40)),('L',(13,40)),('C',(4,30),(7,40),(4,36)),('C',(13,20),(4,24),(7,20))],True)
        path('turret',(13,20),[('L',(15,8)),('L',(29,8)),('L',(32,12)),('L',(33,20))]);join('turret','body');line('barrel',(32,12),(44,12));join('barrel','turret')
