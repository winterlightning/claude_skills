"""flame: Flowing flame silhouette; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '949214a5-cd3d-46da-8416-617e71942aa0'
SOURCE_PATH = 'pictographic-primitives/fire/flame_949214a5-cd3d-46da-8416-617e71942aa0.svg'
AUTHOR = 'gpt-6'

class Flame(Solo48):
    icon_id = 'flame'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    categories = ('fire', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'flame')

    def build(self):
        # Plan: Keep the flame curl and lifted right tip; coherent curves preserve the original asymmetric fire shape.
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
        path('flame',(24,4),[('C',(31,26),(34,9),(35,18)),('C',(38,22),(29,34),(36,29)),('C',(40,30),(39,25),(40,27)),('C',(24,44),(40,40),(33,44)),('C',(8,31),(14,44),(8,38)),('C',(24,4),(8,17),(29,15))],True)
