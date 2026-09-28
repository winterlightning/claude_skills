'Hyena profile: preserve the angular ears, lowered muzzle and shaggy open neck; move the eye into the broad cheek.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '753d11ca-ec60-486c-857b-55d44895af07'
SOURCE_PATH = 'pictographic-primitives/animals/hyena head side_753d11ca-ec60-486c-857b-55d44895af07.svg'
AUTHOR = 'gpt-6'


class HyenaHeadProfile(Solo48):
    icon_id = 'hyena-head-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('hyena', 'head', 'profile', 'side', 'snout', 'ear', 'animal', 'wildlife')

    def build(self):
        # Plan: Trace a broad rounded upright ear and a smooth muzzle-to-jaw flow, replacing the narrow angular lower-jaw fold; keep the natural profile asymmetry.

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
        path('head',(4,8), [('L',(19,13)),('C',(26,8),(20,10),(24,8)),('C',(29,17),(32,8),(29,13)),('C',(35,25),(32,18),(33,22)),('L',(44,29)),('C',(40,36),(44,32),(43,34)),('C',(22,34),(34,40),(28,32)),('C',(10,40),(18,35),(13,36))])
        self.add_dot('eye',(21,24))
