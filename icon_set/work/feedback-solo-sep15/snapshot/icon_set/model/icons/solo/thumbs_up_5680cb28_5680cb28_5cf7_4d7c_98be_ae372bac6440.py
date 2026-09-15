"""thumbs-up-5680cb28: Balanced thumbs-up hand; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5680cb28-5cf7-4d7c-98be-ae372bac6440'
SOURCE_PATH = 'pictographic-primitives/symbol/thumbs up_5680cb28-5cf7-4d7c-98be-ae372bac6440.svg'
AUTHOR = 'gpt-6'

class ThumbsUp5680cb28(Solo48):
    icon_id = 'thumbs-up-5680cb28'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'thumbs-up-5680cb28')

    def build(self):
        # Plan: Human reference: icon_set/references/human_ref/full_body_ref.png. Keep the upright thumb, cuff and broad folded-finger silhouette; smooth the cramped finger bumps.
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
        path('hand',(6,23),[('C',(17,17),(13,23),(16,20)),('C',(22,6),(18,12),(18,6)),('C',(31,11),(28,6),(31,7)),('L',(29,22)),('L',(37,22)),('C',(42,27),(41,22),(42,24)),('C',(38,39),(42,31),(40,36)),('C',(32,42),(36,42),(34,42)),('L',(20,42)),('C',(12,39),(16,42),(16,39)),('L',(6,39)),('L',(6,23))],True)
