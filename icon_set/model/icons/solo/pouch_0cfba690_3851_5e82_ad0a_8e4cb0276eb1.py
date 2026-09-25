"""pouch: Smooth drawstring pouch; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0cfba690-3851-5e82-ad0a-8e4cb0276eb1'
SOURCE_PATH = 'pictographic-primitives/video-games/pouch_0cfba690-3851-5e82-ad0a-8e4cb0276eb1.svg'
AUTHOR = 'gpt-6'

class Pouch(Solo48):
    icon_id = 'pouch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('solo-ai-full-set', 'pouch')

    def build(self):
        # Plan: Preserve the gathered neck and rounded bag; mirror the shoulders and separate the drawstring ends.
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
        path('bag',(18,14),[('L',(14,4)),('L',(34,4)),('L',(30,14)),('C',(40,34),(36,19),(40,25)),('C',(30,44),(40,41),(37,44)),('L',(18,44)),('C',(8,34),(11,44),(8,41)),('C',(18,14),(8,25),(12,19))],True)
        path('tie',(18,14),[('L',(24,14)),('L',(30,14))]);join('tie','bag')
        line('left-tie',(18,14),(17,22));line('right-tie',(30,14),(31,22));join('left-tie','bag');join('right-tie','bag')
