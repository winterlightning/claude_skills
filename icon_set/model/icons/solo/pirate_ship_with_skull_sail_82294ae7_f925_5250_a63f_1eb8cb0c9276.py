"""Pirate Ship with Skull Sail.

Symbol plan: Asymmetric sail and raised bow over rounded hull; extremes6,6,42,42. Skull retains jaw silhouette; omit tiny face marks and mast above cloth.
Construction references: Lucide sailboat: coherent curved hull and central mast. Lucide skull: rounded cranium and squared jaw.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82294ae7-f925-5250-a63f-1eb8cb0c9276'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/piracy ship_82294ae7-f925-5250-a63f-1eb8cb0c9276.svg'
AUTHOR = 'gpt-6'


class PirateShipWithSkullSail(Solo48):
    icon_id = 'pirate-ship-with-skull-sail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('pirate', 'ship', 'with', 'skull', 'sail')

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

        self.add_bezier('sail-right',(34,6),((38,12),(40,24),(38,30)))
        path('sail-rest',(38,30),[(24,30),(10,30),(12,6),(34,6)])
        self.relate('connect','sail-right','sail-rest')
        path('skull',(24,14),[((24,20),3,3,True),((24,14),3,3,True)],True)
        self.add_line('jaw',(24,20),(24,22))
        self.relate('connect','skull','jaw')
        self.add_line('mast',(24,30),(24,42))
        path('hull',(6,38),[((14,42),8,4,False),(24,42),(34,42),((42,34),8,8,False)])
        self.relate('connect','mast','sail-rest');self.relate('connect','mast','hull')
