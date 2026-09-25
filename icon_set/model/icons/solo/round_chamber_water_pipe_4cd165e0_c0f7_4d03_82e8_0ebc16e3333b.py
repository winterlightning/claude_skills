"""Glass Smoking Water Pipe.

Symbol plan: Tall neck joined to rounded chamber and diagonal open side tube; flat foot. Visible (6,2)-(42,46). Omit lower chamber reflection.
Construction references: No useful direct Lucide subject match; geometric contour construction.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4cd165e0-c0f7-4d03-82e8-0ebc16e3333b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/cannabis bong_4cd165e0-c0f7-4d03-82e8-0ebc16e3333b.svg'
AUTHOR = 'gpt-6'


class RoundChamberWaterPipe(Solo48):
    icon_id = 'round-chamber-water-pipe'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('round', 'chamber', 'water', 'pipe')

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

        path('pipe',(22,4),[(34,4),(34,20),((40,32),6,12,True),((28,44),12,12,True),(20,44),((12,32),12,12,True),(12,28),(8,24),(14,18),(22,24),(22,4)],True)
