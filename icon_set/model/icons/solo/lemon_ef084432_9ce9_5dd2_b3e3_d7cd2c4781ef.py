"""lemon: Flowing lemon silhouette; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ef084432-9ce9-5dd2-b3e3-d7cd2c4781ef'
SOURCE_PATH = 'icons-json/food/lemon_ef084432-9ce9-5dd2-b3e3-d7cd2c4781ef.json'
AUTHOR = 'gpt-6'

class Lemon(Solo48):
    icon_id = 'lemon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('solo-ai-full-set', 'lemon')

    def build(self):
        # Plan: Preserve the lemon tips and fuller middle; mirror the opposing shoulders without changing the upright silhouette.
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
        path('fruit',(24,4),[('C',(30,8),(27,4),(27,6)),('C',(40,24),(37,13),(40,18)),('C',(30,40),(40,31),(36,36)),('C',(24,44),(27,42),(27,44)),('C',(18,40),(21,44),(21,42)),('C',(8,24),(12,36),(8,31)),('C',(18,8),(8,18),(11,13)),('C',(24,4),(21,6),(21,4))],True)
