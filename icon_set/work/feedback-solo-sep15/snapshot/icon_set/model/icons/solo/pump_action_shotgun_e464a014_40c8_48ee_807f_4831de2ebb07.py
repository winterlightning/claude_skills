"""Pump-Action Shotgun. Long barrel, angled grip and separate pump fore-end; small trigger guard omitted.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e464a014-40c8-48ee-807f-4831de2ebb07'
SOURCE_PATH = 'pictographic-primitives/war/shotgun_e464a014-40c8-48ee-807f-4831de2ebb07.svg'
AUTHOR = 'gpt-6'

class PumpActionShotgun(Solo48):
    icon_id = 'pump-action-shotgun'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('shotgun', 'pump', 'barrel', 'grip', 'trigger', 'weapon')

    def build(self):
        # Plan: Broaden the pump assembly and expose its two exact attachment nodes on the barrel; preserve the diagonal stock and long muzzle.

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
        poly('gun',(10,42),(6,30),(10,22),(36,6),(42,12),(36,16),(20,27),(16,30),(18,38),closed=True)
        poly('pump',(20,27),(28,34),(38,27),(36,16));join('pump','gun')
