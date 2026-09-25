# Review revision; previous candidates preserved.
"""Curled silhouette, muzzle and two stripes in a broad tail. No useful local raccoon match; circular construction re-authored from the supplied image. Four stripes reduced to two."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dcf6e72c-8224-5fad-bb7d-737e07df48dd'
SOURCE_PATH = 'pictographic-primitives/animals/raccoon_dcf6e72c-8224-5fad-bb7d-737e07df48dd.svg'
AUTHOR = 'gpt-6'

class CurledRaccoon(Solo48):
    icon_id = 'curled-raccoon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('raccoon', 'curled', 'tail', 'stripes', 'mask', 'animal', 'wildlife', 'nocturnal')

    def build(self):
        # Plan: Open the face-to-tail gap, retain a clear eye and coherent circular back, and put two stripes on the broadest parts of the curl.

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
        path('outline',(6,14), [('L',(10,14)),('A',(24,6),14,8,True),('A',(42,24),18,18,True),('A',(24,42),18,18,True),('L',(14,42)),('A',(6,34),8,8,True),('L',(6,32)),('L',(10,32)),('L',(16,34)),('L',(24,34)),('A',(34,24),10,10,False)])
        path('face',(6,14), [('L',(6,19)),('A',(12,24),6,5,False),('L',(22,24))]);join('face','outline')
        line('ear',(24,6),(24,8));join('ear','outline')
        line('stripe-lower',(24,42),(24,34));line('stripe-side',(42,24),(34,24));join('stripe-lower','outline');join('stripe-side','outline')
        self.add_dot('eye',(20,15))
