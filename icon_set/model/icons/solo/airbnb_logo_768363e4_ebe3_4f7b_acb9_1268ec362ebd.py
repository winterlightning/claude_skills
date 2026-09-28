"""airbnb-logo: Smooth looped travel mark; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '768363e4-ebe3-4f7b-acb9-1268ec362ebd'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/airbnb logo_768363e4-ebe3-4f7b-acb9-1268ec362ebd.svg'
AUTHOR = 'gpt-6'

class AirbnbLogo(Solo48):
    icon_id = 'airbnb-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-full-set', 'airbnb-logo')

    def build(self):
        # Plan: Preserve the tall rounded triangular loop and central crossing oval, with mirrored lower lobes.
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
        path('outer',(24,4),[('C',(30,9),(27,4),(28,5)),('L',(40,33)),('C',(33,44),(40,40),(37,44)),('C',(24,39),(30,44),(27,42)),('C',(15,44),(21,42),(18,44)),('C',(8,33),(11,44),(8,40)),('L',(18,9)),('C',(24,4),(20,5),(21,4))],True)
        path('loop',(24,39),[('C',(19,29),(20,35),(19,32)),('A',(29,29),5,5,True),('C',(24,39),(29,32),(28,35))],True);join('loop','outer')
