"""Police Cap with Shield Emblem.

Symbol plan: Peaked police cap mirrored about24, broad crown and curved visor. Extremes4,8,44,40. Emblem remains central; omit second hatband seam.
Construction references: Source police-cap silhouette; geometric centered emblem; mirrored crown and visor.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91bdffd8-cff0-5390-8c5a-a4e9e6f3dfff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/police hat_91bdffd8-cff0-5390-8c5a-a4e9e6f3dfff.svg'
AUTHOR = 'gpt-6'


class PoliceCapWithShieldEmblem(Solo48):
    icon_id = 'police-cap-with-shield-emblem'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('police', 'cap', 'with', 'shield', 'emblem')

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

        self.add_bezier('crown',(4,32),((4,18),(8,8),(24,8)),((40,8),(44,18),(44,32)))
        self.add_arc('visor',(44,32),(4,32),radius_x=20,radius_y=8)
        self.add_line('band',(4,32),(44,32))
        self.add_contour('cap','crown','visor',closed=True)
        self.relate('connect','cap','band')

        path('shield',(20,17),[(28,17),(28,20),((24,24),4,4,True),((20,20),4,4,True),(20,17)],True)
