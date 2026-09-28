"""boxing-glove: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dbf91214-8ada-5b30-9a04-1c64d7b7b10a'
SOURCE_PATH = 'pictographic-primitives/sports/boxing glove_dbf91214-8ada-5b30-9a04-1c64d7b7b10a.svg'
AUTHOR = 'gpt-6'

class BoxingGlove(Solo48):
    icon_id = 'boxing-glove'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('boxing', 'glove', 'sports', 'solo-ai-next50')

    def build(self):
        # Plan: A boxing glove has a broad smooth knuckle dome, an inward thumb and a rounded cuff. Preserved the source hand silhouette and removed uneven corners.
        # Reference: No useful exact Lucide match; supplied boxing glove silhouette.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
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
        path('glove',(16,36),[('C',(8,26),(10,34),(8,31)),('L',(8,16)),('A',(20,4),12,12,True),('L',(28,4)),('A',(40,16),12,12,True),('L',(40,26)),('C',(32,36),(40,32),(36,36)),('L',(16,36))],True)
        path('thumb',(40,26),[('L',(33,19)),('C',(28,27),(28,17),(24,22))]);join('thumb','glove')
        path('cuff',(16,36),[('L',(12,36)),('L',(12,40)),('A',(16,44),4,4,False),('L',(32,44)),('A',(36,40),4,4,False),('L',(36,36)),('L',(32,36))]);join('cuff','glove')
