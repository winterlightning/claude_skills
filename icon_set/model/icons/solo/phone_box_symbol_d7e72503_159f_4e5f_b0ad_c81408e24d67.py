"""phone-box-symbol: Balanced telephone kiosk; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd7e72503-159f-4e5f-b0ad-c81408e24d67'
SOURCE_PATH = 'pictographic-primitives/symbol/phone box_d7e72503-159f-4e5f-b0ad-c81408e24d67.svg'
AUTHOR = 'gpt-6'

class PhoneBoxSymbol(Solo48):
    icon_id = 'phone-box-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('solo-ai-full-set', 'phone-box-symbol')

    def build(self):
        # Plan: A smooth domed roof and level window sill share exact side-wall nodes, with clear room inside the dome.
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
        path('roof',(8,16),[('A',(40,16),16,12,True),('L',(38,16)),('L',(10,16)),('L',(8,16))],True)
        for x in [10,38]:path(f'wall-{x}',(x,16),[('L',(x,29)),('L',(x,44))]);join(f'wall-{x}','roof')
        path('base',(8,44),[('L',(10,44)),('L',(38,44)),('L',(40,44))]);line('sill',(10,29),(38,29))
        for x in [10,38]:join(f'wall-{x}','sill');join(f'wall-{x}','base')
