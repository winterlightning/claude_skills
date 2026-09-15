"""outdoors-machete: Smooth broad machete; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '13df796c-e4d1-4a16-97fa-eb423cf09cba'
SOURCE_PATH = 'icons-json/outdoors/outdoors machete_13df796c-e4d1-4a16-97fa-eb423cf09cba.json'
AUTHOR = 'gpt-6'

class OutdoorsMachete(Solo48):
    icon_id = 'outdoors-machete'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('solo-ai-full-set', 'outdoors-machete')

    def build(self):
        # Plan: Preserve the broad curved blade and short handle; enlarge both bands perpendicular to the blade direction.
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
        path('blade',(18,25),[('L',(42,6)),('C',(35,28),(42,17),(41,23)),('L',(24,36)),('L',(18,25))],True)
        path('handle',(18,25),[('L',(6,35)),('L',(6,42)),('L',(11,42)),('L',(24,36))]);join('handle','blade')
