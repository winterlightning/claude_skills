"""modern-tv-curvy-edge: Even television frame; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '069bf6b4-e362-4e8f-b335-eb005c8c4865'
SOURCE_PATH = 'pictographic-primitives/tv/modern tv curvy edge_069bf6b4-e362-4e8f-b335-eb005c8c4865.svg'
AUTHOR = 'gpt-6'

class ModernTvCurvyEdge(Solo48):
    icon_id = 'modern-tv-curvy-edge'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    aliases = ()
    keywords = ('solo-ai-full-set', 'modern-tv-curvy-edge')

    def build(self):
        # Plan: Preserve the rounded screen and center stand; match frame corners and keep clear space above the foot.
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
        path('screen',(4+4,8),[('L',(44-4,8)),('A',(44,8+4),4,4,True),('L',(44,32-4)),('A',(44-4,32),4,4,True),('L',(24,32)),('L',(4+4,32)),('A',(4,32-4),4,4,True),('L',(4,8+4)),('A',(4+4,8),4,4,True)],True)
        line('stand',(24,32),(24,40));path('foot',(24-8,40),[('L',(24,40)),('L',(24+8,40))]);join('stand','screen');join('stand','foot')
