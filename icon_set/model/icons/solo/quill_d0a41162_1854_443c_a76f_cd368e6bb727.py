"""quill: Smooth broad quill; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd0a41162-1854-443c-a76f-cd368e6bb727'
SOURCE_PATH = 'pictographic-primitives/design/quill_d0a41162-1854-443c-a76f-cd368e6bb727.svg'
AUTHOR = 'gpt-6'

class Quill(Solo48):
    icon_id = 'quill'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'state')
    aliases = ()
    keywords = ('solo-ai-full-set', 'quill')

    def build(self):
        # Plan: Preserve the diagonal tapering leaf and short quill stroke. Use two coherent vane curves and a central partial shaft.
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
        path('vane',(13,35),[('C',(42,6),(8,20),(27,9)),('C',(13,35),(39,27),(26,41))],True)
        path('shaft',(6,42),[('L',(13,35)),('L',(26,22))]);join('shaft','vane')
