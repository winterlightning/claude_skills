"""virtual-coin-crypto-tron: Clean triangular Tron facets; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '02129ee0-b664-4e6d-ab7f-1e3b7ee2f16c'
SOURCE_PATH = 'pictographic-primitives/money/virtual coin crypto tron_02129ee0-b664-4e6d-ab7f-1e3b7ee2f16c.svg'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoTron(Solo48):
    icon_id = 'virtual-coin-crypto-tron'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('solo-ai-full-set', 'virtual-coin-crypto-tron')

    def build(self):
        # Plan: Preserve all three facets and the skewed outer triangle; use one uninterrupted outer diagonal and shared hub.
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
        poly('outline',(8,4),(35,10),(40,17),(21,44),closed=True)
        for j,end in enumerate([(8,4),(40,17),(21,44)]):line(f'facet-{j}',(21,20),end);join(f'facet-{j}','outline')
        for j in range(3):
         for k in range(j+1,3):join(f'facet-{j}',f'facet-{k}')
