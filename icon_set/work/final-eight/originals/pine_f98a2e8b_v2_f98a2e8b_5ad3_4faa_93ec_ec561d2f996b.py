"""pine-f98a2e8b: Three-tier pine — spacing review; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f98a2e8b-5ad3-4faa-93ec-ec561d2f996b'
SOURCE_PATH = 'icons-json/symbol/pine_f98a2e8b-5ad3-4faa-93ec-ec561d2f996b.json'
AUTHOR = 'gpt-6'

class PineF98a2e8bVariant2(Solo48):
    icon_id = 'pine-f98a2e8b-v2'
    variant_of = 'pine-f98a2e8b'
    variant_label = 'Three-tier pine — spacing review'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'pine-f98a2e8b')

    def build(self):
        # Plan: Attempted wider branch gaps and shorter tier overhangs. Keep three tiers and the trunk; the tight branch returns remain flagged for manual exception review.
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
        path('tree',(24,4),[('L',(32,14)),('L',(27,14)),('C',(36,26),(27,20),(32,24)),('L',(29,26)),('C',(40,38),(29,32),(35,35)),('L',(24,38)),('L',(8,38)),('C',(19,26),(13,35),(19,32)),('L',(12,26)),('C',(21,14),(16,24),(21,20)),('L',(16,14)),('L',(24,4))],True)
        line('trunk',(24,38),(24,44));join('trunk','tree')
