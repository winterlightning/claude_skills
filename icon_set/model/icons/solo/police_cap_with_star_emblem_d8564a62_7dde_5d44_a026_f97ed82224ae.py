"""Police Hat with Star.

Symbol plan: Peaked police cap mirrored about24, broad crown and curved visor. Extremes4,8,44,40. Emblem remains central; omit second hatband seam.
Construction references: Source police-cap silhouette; geometric centered emblem; mirrored crown and visor.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8564a62-7dde-5d44-a026-f97ed82224ae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/police hat_d8564a62-7dde-5d44-a026-f97ed82224ae.svg'
AUTHOR = 'gpt-6'


class PoliceCapWithStarEmblem(Solo48):
    icon_id = 'police-cap-with-star-emblem'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('police', 'cap', 'with', 'star', 'emblem')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x-r,y), [((x+r,y),r,r,True), ((x-r,y),r,r,True)], True)

        self.add_bezier('crown',(4,34),((4,18),(8,8),(24,8)),((40,8),(44,18),(44,34)))
        self.add_arc('visor',(44,34),(4,34),radius_x=20,radius_y=6)
        self.add_line('band',(4,34),(44,34))
        self.add_contour('cap','crown','visor',closed=True)
        self.relate('connect','cap','band')

        for j,end in enumerate(((24,17),(29,20),(27,26),(21,26),(19,20))):
         self.add_line(f'ray-{j}',(24,21),end)
         for k in range(j):self.relate('connect',f'ray-{j}',f'ray-{k}')
