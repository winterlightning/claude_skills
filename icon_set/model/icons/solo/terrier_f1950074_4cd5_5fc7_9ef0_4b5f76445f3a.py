"""terrier: Smooth alert terrier; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f1950074-4cd5-5fc7-9ef0-4b5f76445f3a'
SOURCE_PATH = 'pictographic-primitives/pets/terrier_f1950074-4cd5-5fc7-9ef0-4b5f76445f3a.svg'
AUTHOR = 'gpt-6'

class Terrier(Solo48):
    icon_id = 'terrier'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'terrier')

    def build(self):
        # Plan: Preserve pointed ears, broad cheeks and narrow muzzle. Mirror the face but keep the ears tall and open.
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
        path('face',(8,4),[('L',(18,14)),('C',(30,14),(22,12),(26,12)),('L',(40,4)),('C',(36,24),(40,13),(39,19)),('C',(24,44),(34,37),(31,42)),('C',(12,24),(17,42),(14,37)),('C',(8,4),(9,19),(8,13))],True)
        self.add_dot('left-eye',(20,22));self.add_dot('right-eye',(28,22));line('muzzle',(24,36),(24,44));join('muzzle','face')
