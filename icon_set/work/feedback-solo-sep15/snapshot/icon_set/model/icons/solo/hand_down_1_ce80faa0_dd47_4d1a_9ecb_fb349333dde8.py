"""hand-down-1: Flowing pointing hand; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ce80faa0-dd47-4d1a-9ecb-fb349333dde8'
SOURCE_PATH = 'pictographic-primitives/state/hand down 1_ce80faa0-dd47-4d1a-9ecb-fb349333dde8.svg'
AUTHOR = 'gpt-6'

class HandDown1(Solo48):
    icon_id = 'hand-down-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('solo-ai-full-set', 'hand-down-1')

    def build(self):
        # Plan: Human reference: full_body_ref.png. Preserve the downward diagonal finger, tucked thumb and open wrist with smooth, coherent curves.
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
        path('hand',(35,8),[('C',(23,12),(31,11),(27,12)),('C',(4,23),(17,12),(8,18)),('C',(17,22),(4,28),(11,24)),('L',(10,33)),('C',(15,40),(7,38),(10,40)),('L',(22,40)),('C',(28,35),(25,40),(26,37)),('L',(44,16))])
