"""Rate stretch tool (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7be4363f-746d-5909-9b6e-3dba795301f6'
SOURCE_PATH = 'pictographic-primitives/arrows/rate stretch tool_7be4363f-746d-5909-9b6e-3dba795301f6.svg'
AUTHOR = 'gpt-6'

class RateStretchTool(Solo48):
    icon_id = 'rate-stretch-tool'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('rate', 'stretch', 'tool', 'arrows')

    def build(self):
        # Plan: Two mirrored rounded turns with open arrowheads replace folded duplicate segments; separate their inner endpoints by ten units.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        path('upper',(6,12), [('L',(18,12)),('A',(24,18),6,6,True),('L',(24,19))])
        poly('upper-arrow',(12,6),(6,12),(12,18));join('upper','upper-arrow')
        path('lower',(42,36), [('L',(30,36)),('A',(24,30),6,6,True),('L',(24,29))])
        poly('lower-arrow',(36,42),(42,36),(36,30));join('lower','lower-arrow')
