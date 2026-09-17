"""Classic Sailing Pirate Ship.

Symbol plan: Tiered sail curves on central mast, wide hull. Visible (6,2)-(42,46). Omit rigging and flag.
Construction references: Lucide sailboat: rounded hull and central mast; source retains tiered square sails.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '879727ea-a627-5f5b-89c1-619981348dfe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/piracy ship_879727ea-a627-5f5b-89c1-619981348dfe.svg'
AUTHOR = 'gpt-6'


class SailingShipWithTieredSails(Solo48):
    icon_id = 'sailing-ship-with-tiered-sails'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('sailing', 'ship', 'with', 'tiered', 'sails')

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

        path('hull',(8,36),[(24,36),(40,36),((32,44),8,8,True),(16,44),((8,36),8,8,True)],True)
        self.add_line('mast-upper',(24,12),(24,20))
        self.add_line('mast-lower',(24,20),(24,36))
        path('upper-sail',(14,4),[(34,4),((24,12),10,8,True),((14,4),10,8,True)],True)
        path('lower-sail',(8,20),[(24,20),(40,20),((24,20),8,8,True),((8,20),8,8,True)],True)
        for a,b in [('mast-upper','upper-sail'),('mast-upper','lower-sail'),('mast-upper','mast-lower'),('mast-lower','lower-sail'),('mast-lower','hull')]:self.relate('connect',a,b)
