"""Swimming Dog.

Plan: Left-facing floppy head and level back above a repeated wave line; no submerged legs.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2579e93c-54a1-5e07-b122-57efb336f1ff'
SOURCE_PATH = 'pictographic-primitives/pets/dog swimming_2579e93c-54a1-5e07-b122-57efb336f1ff.svg'
AUTHOR = 'gpt-6'

class SwimmingDog(Solo48):
    icon_id = 'swimming-dog'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'swimming', 'water', 'waves', 'pet', 'summer', 'paddle')

    def build(self):
        # Plan: A domed head and smooth rump rise above four equal waves. Deepen the muzzle to provide a full eight-unit opening.

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
        path('head',(12,20), [('A',(28,20),8,12,True)])
        poly('muzzle',(12,20),(4,20),(4,28),(14,28));join('muzzle','head')
        path('back',(28,20), [('L',(38,20)),('A',(44,26),6,6,True)]);join('back','head')
        path('water',(4,37), [('A',(14,37),5,3,False),('A',(24,37),5,3,False),('A',(34,37),5,3,False),('A',(44,37),5,3,False)])
