"""imessage-logo: Smooth speech bubble; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '57877e05-412a-4ab7-81af-b1b8f5355989'
SOURCE_PATH = 'pictographic-primitives/logos/imessage logo_57877e05-412a-4ab7-81af-b1b8f5355989.svg'
AUTHOR = 'gpt-6'

class ImessageLogo(Solo48):
    icon_id = 'imessage-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'imessage-logo')

    def build(self):
        # Plan: Preserve the broad oval bubble and lower-left tail; use coherent arcs and a clear tail join.
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
        path('bubble',(12,33),[('C',(4,23),(7,30),(4,28)),('C',(24,8),(4,13),(14,8)),('C',(44,23),(34,8),(44,13)),('C',(24,36),(44,32),(34,36)),('L',(18,35)),('C',(8,40),(15,38),(11,40)),('L',(12,33))],True)
