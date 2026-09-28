"""feather: Smooth notched feather; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ab28f10-44ce-40c6-b0df-2578356c15de'
SOURCE_PATH = 'pictographic-primitives/symbol/feather_8ab28f10-44ce-40c6-b0df-2578356c15de.svg'
AUTHOR = 'gpt-6'

class Feather(Solo48):
    icon_id = 'feather'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('solo-ai-full-set', 'feather')

    def build(self):
        # Plan: Preserve the broad vane, diagonal shaft and one intentional notch; the notch ends at a shared vane node.
        # Reference: Lucide leaf: original and atomic-debug geometry.

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
        path('vane',(13,35),[('C',(8,25),(9,33),(8,29)),('C',(38,4),(8,15),(27,7)),('C',(40,13),(40,7),(40,10)),('C',(29,27),(40,20),(34,24)),('C',(13,35),(29,35),(20,39))],True)
        path('quill',(8,44),[('L',(13,35)),('L',(25,20))]);join('quill','vane')
