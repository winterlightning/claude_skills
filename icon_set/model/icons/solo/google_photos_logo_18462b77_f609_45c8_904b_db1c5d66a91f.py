"""google-photos-logo: Regular four-blade pinwheel; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18462b77-f609-45c8-904b-db1c5d66a91f'
SOURCE_PATH = 'pictographic-primitives/logos/google photos logo_18462b77-f609-45c8-904b-db1c5d66a91f.svg'
AUTHOR = 'gpt-6'

class GooglePhotosLogo(Solo48):
    icon_id = 'google-photos-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('solo-ai-full-set', 'google-photos-logo')

    def build(self):
        # Plan: Preserve the four rotating blades using equal radii and exact central attachment nodes.
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
        for j in range(4):
         def p(x,y):
          for _ in range(j):x,y=48-y,x
          return x,y
         path(f'blade-{j}',p(24,24),[('L',p(24,6)),('A',p(24,24),9,9,True)],True)
        for j in range(4):
         for k in range(j+1,4):join(f'blade-{j}',f'blade-{k}')
