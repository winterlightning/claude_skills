"""Burning Crashed Aircraft. Crashed aircraft, rising flame and one smoke stroke; second smoke trail removed.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81f5c526-61a1-4426-afae-2fec80a31cb2'
SOURCE_PATH = 'pictographic-primitives/war/plane crashed_81f5c526-61a1-4426-afae-2fec80a31cb2.svg'
AUTHOR = 'gpt-6'

class BurningCrashedAircraft(Solo48):
    icon_id = 'burning-crashed-aircraft'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('aircraft', 'crash', 'fire', 'smoke', 'flame', 'wreck')

    def build(self):
        # Plan: Broaden the broken aircraft wing and trace one flowing flame rising from two exact attachment nodes; retain the smoke trail.

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
        poly('plane',(8,25),(18,30),(17,18),(27,23),(28,34),(38,34),(40,34),(40,44),(25,44),(8,36),closed=True)
        path('fire',(27,23), [('C',(30,12),(26,20),(26,16)),('C',(30,4),(32,8),(30,6)),('C',(40,22),(40,12),(40,16)),('C',(38,34),(40,26),(38,31))]);join('fire','plane')
        line('smoke',(12,4),(10,14))
