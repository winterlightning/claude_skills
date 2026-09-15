"""text-strike-through: Smooth strikethrough S; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a8a2022f-6ae0-41e6-966f-a2ea1e79a09b'
SOURCE_PATH = 'pictographic-primitives/interface-essential/text strike through_a8a2022f-6ae0-41e6-966f-a2ea1e79a09b.svg'
AUTHOR = 'gpt-6'

class TextStrikeThrough(Solo48):
    icon_id = 'text-strike-through'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('solo-ai-full-set', 'text-strike-through')

    def build(self):
        # Plan: Preserve the S and central strike; a coherent letter curve crosses the shared line at a defined midpoint.
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
        path('letter',(33,14),[('C',(23,6),(33,8),(29,6)),('C',(15,15),(17,6),(15,9)),('C',(24,24),(15,20),(19,23)),('C',(33,33),(30,26),(33,28)),('C',(23,42),(33,39),(29,42)),('C',(14,34),(17,42),(14,39))])
        path('strike',(6,24),[('L',(24,24)),('L',(42,24))]);join('strike','letter')
