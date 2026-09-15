"""earth-fad4bbe1: Smooth globe and land contours; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fad4bbe1-6331-5672-973b-83becf88fd84'
SOURCE_PATH = 'pictographic-primitives/maps/earth_fad4bbe1-6331-5672-973b-83becf88fd84.svg'
AUTHOR = 'gpt-6'

class EarthFad4bbe1(Solo48):
    icon_id = 'earth-fad4bbe1'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('solo-ai-full-set', 'earth-fad4bbe1')

    def build(self):
        # Plan: Preserve the asymmetric land contours inside a true circle; split the rim at their actual attachment nodes.
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
        path('globe',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
        path('land',(24,4),[('C',(20,15),(22,8),(20,10)),('L',(27,20)),('C',(30,33),(26,29),(26,33)),('C',(38,26),(34,33),(34,27)),('C',(44,24),(40,25),(42,24))]);join('land','globe')
        path('south',(4,24),[('C',(13,30),(9,24),(12,25)),('C',(24,44),(15,40),(18,43))]);join('south','globe')
