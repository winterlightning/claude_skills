"""Dog Carrying Ball.

Plan: Left-facing carrying dog head at upper-right, large ball at left and bent front leg below. Ball held at an exact mouth attachment.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08cdc871-2ff7-4c1a-9e75-3415928459cf'
SOURCE_PATH = 'pictographic-primitives/pets/dog carrying bring play ball_08cdc871-2ff7-4c1a-9e75-3415928459cf.svg'
AUTHOR = 'gpt-6'

class DogCarryingBall(Solo48):
    icon_id = 'dog-carrying-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'ball', 'fetch', 'play', 'carrying', 'training', 'pet')

    def build(self):
        # Plan: Trace the rounded muzzle and flowing open jaw instead of the angular zigzag; retain the pointed ear and ball at the mouth.

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
        path('head',(42,18), [('C',(40,6),(42,12),(40,8)),('L',(34,14)),('L',(28,14)),('C',(22,24),(24,14),(22,18))])
        circle('ball',14,24,8)
        path('jaw',(22,24), [('L',(30,24)),('L',(30,30)),('C',(24,38),(30,34),(24,34)),('C',(34,38),(24,42),(30,42)),('L',(42,42))])
        join('ball','head');join('ball','jaw');join('head','jaw')
