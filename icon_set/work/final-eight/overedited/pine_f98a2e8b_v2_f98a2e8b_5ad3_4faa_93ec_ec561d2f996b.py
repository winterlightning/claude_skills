"""pine-f98a2e8b: Three-tier pine — clear spacing; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f98a2e8b-5ad3-4faa-93ec-ec561d2f996b'
SOURCE_PATH = 'icons-json/symbol/pine_f98a2e8b-5ad3-4faa-93ec-ec561d2f996b.json'
AUTHOR = 'gpt-6'

class PineF98a2e8bVariant2(Solo48):
    icon_id = 'pine-f98a2e8b-v2'
    variant_of = 'pine-f98a2e8b'
    variant_label = 'Three-tier pine — clear spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'pine-f98a2e8b')

    def build(self):
        # Plan: Gave each of the three branch tiers a deeper return while preserving the tree silhouette.
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
        path('tree',(24,4),[('L',(32,14)),('L',(28,14)),('L',(28,20)),('L',(36,26)),('L',(30,26)),('L',(30,31)),('L',(40,38)),('L',(24,38)),('L',(8,38)),('L',(18,31)),('L',(18,26)),('L',(12,26)),('L',(20,20)),('L',(20,14)),('L',(16,14)),('L',(24,4))],True)
        line('trunk',(24,38),(24,44));join('trunk','tree')
