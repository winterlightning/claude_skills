"""affinity-publisher-logo: Regular diagonal publisher bands; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca67be63-3b5a-4b74-800b-f1df0601b64c'
SOURCE_PATH = 'icons-json/_uncategorized_01/affinity publisher logo_ca67be63-3b5a-4b74-800b-f1df0601b64c.json'
AUTHOR = 'gpt-6'

class AffinityPublisherLogo(Solo48):
    icon_id = 'affinity-publisher-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('solo-ai-full-set', 'affinity-publisher-logo')

    def build(self):
        # Plan: Preserve the four diagonal divisions; rebalance their spacing and make shared edge intersections exact.
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
        path('outline',(6,32),[('L',(10,24)),('L',(15,15)),('L',(20,6)),('L',(32,6)),('L',(42,6)),('L',(42,24)),('L',(42,42)),('L',(30,42)),('L',(20,42)),('L',(6,42)),('L',(6,32))],True)
        for j,(a,b) in enumerate([((10,24),(20,42)),((15,15),(30,42)),((20,6),(42,42)),((32,6),(42,24))]):line(f'band-{j}',a,b);join(f'band-{j}','outline')
