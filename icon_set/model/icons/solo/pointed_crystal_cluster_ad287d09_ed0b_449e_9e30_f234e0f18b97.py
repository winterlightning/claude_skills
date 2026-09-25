"""Three elongated pointed crystals form an uneven fan with complete lower ends."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad287d09-ed0b-449e-9e30-f234e0f18b97'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/crystals_ad287d09-ed0b-449e-9e30-f234e0f18b97.svg'
AUTHOR = 'gpt-6'


class PointedCrystalCluster(Solo48):
    icon_id = 'pointed-crystal-cluster'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "decoration"
    aliases = ()
    keywords = ('crystal', 'cluster', 'mineral', 'quartz', 'geology', 'points', 'gem')

    def build(self):
        # Plan: One central crystal and a mirrored pair, with broad parallel side facets and exact shared junctions.

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
        poly('central',(16,44),(16,20),(16,12),(24,4),(32,12),(32,20),(32,44),closed=True)
        poly('left',(16,20),(8,12),(8,36),(16,44));poly('right',(32,20),(40,12),(40,36),(32,44))
        join('left','central');join('right','central')
