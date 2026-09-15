"""thumb-symbol: Smooth thumbs-up silhouette; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c5652a88-5c11-499a-8e2e-486a9b3a75d1'
SOURCE_PATH = 'icons-json/symbol/thumb_c5652a88-5c11-499a-8e2e-486a9b3a75d1.json'
AUTHOR = 'gpt-6'

class ThumbSymbol(Solo48):
    icon_id = 'thumb-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'thumb-symbol')

    def build(self):
        # Plan: Human reference: icon_set/references/human_ref/full_body_ref.png. Preserve the raised thumb and broad hand with a rounded, clearly separated thumb.
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
        path('hand',(8,23),[('C',(17,18),(12,23),(16,21)),('C',(22,4),(18,14),(18,4)),('C',(31,9),(28,4),(31,5)),('L',(29,21)),('L',(36,22)),('C',(40,26),(40,22),(40,24)),('L',(36,40)),('C',(30,44),(35,43),(33,44)),('L',(19,44)),('C',(13,40),(16,44),(16,40)),('L',(8,40)),('L',(8,23))],True)
