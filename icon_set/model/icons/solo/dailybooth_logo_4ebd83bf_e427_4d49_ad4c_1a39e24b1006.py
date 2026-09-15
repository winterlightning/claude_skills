"""Speech-bubble roundel enclosing a reduced camera and lens; rounded camera shoulder owns the lens spacing; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ebd83bf-e427-4d49-ad4c-1a39e24b1006'
SOURCE_PATH = 'pictographic-primitives/logos/dailybooth logo_4ebd83bf-e427-4d49-ad4c-1a39e24b1006.svg'
AUTHOR = 'gpt-6'

class DailyboothLogo(Solo48):
    icon_id = 'dailybooth-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('dailybooth', 'camera', 'photo', 'logo', 'brand', 'social', 'speech-bubble')

    def build(self):
        # Plan: Retain the camera inside its speech bubble. Round the camera body and simplify the tiny lens to a filled mark so the nested counters fit.

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
        path('bubble',(24,6), [('A',(42,24),18,18,True),('C',(40,32),(42,28),(41,30)),('L',(42,42)),('L',(32,40)),('C',(24,42),(30,41),(28,42)),('A',(6,24),18,18,True),('A',(24,6),18,18,True)],True)
        box('camera',15,15,33,33,7);self.add_dot('lens',(24,24))
