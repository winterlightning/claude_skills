"""A detonator with a larger empty box and open cable loop.

SQUARE: ink (0,0)-(64,64). Box centerlines (2,16)-(40,62),
up from (2,24)-(38,62): clear straight interior grows from 32x34 to 34x42.
Cable-to-box centerline spacing grows from 8 to 10; loop width remains 12.
Lucide monitor original and atomic-debug informed the rounded box and centered
post. The source supplies the T handle and asymmetric cable. The final cable
foot is omitted, leaving a simple round-ended descent and more room for the box.
Symbol plan: box owns the centered plunger and wire attachment; wire turns
share endpoints and tangents. Parent remains unchanged.
Hosting (compose.py): plus valid; heart valid; check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (tnt-detonator-plunger SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '2ba32171-2b1e-4619-ac1e-b8b912b7fa13'
SOURCE_PATH = 'container_icons/svg/tnt-detonator-plunger-2ba32171-2b1e-4619-ac1e-b8b912b7fa13.svg'
AUTHOR = 'claude-opus-5-5'


class TntDetonatorPlunger(Container64):
    icon_id = 'tnt-detonator-plunger'
    keyshape = Keyshape.SQUARE
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('tnt', 'detonator', 'plunger', 'explosive')

    def build(self) -> None:
        self.add_line('box-top', (11, 17), (34, 17))
        self.add_arc('box-ne', (34, 17), (39, 22), radius_x=5)
        self.add_line('box-right', (39, 22), (39, 53))
        self.add_arc('box-se', (39, 53), (34, 58), radius_x=5)
        self.add_line('box-bottom', (34, 58), (11, 58))
        self.add_arc('box-sw', (11, 58), (6, 53), radius_x=5)
        self.add_line('box-left', (6, 53), (6, 22))
        self.add_arc('box-nw', (6, 22), (11, 17), radius_x=5)
        self.add_line('plunger', (22, 6), (22, 17))
        self.add_line('handle', (12, 6), (33, 6))
        self.add_arc('wire-out', (39, 47), (48, 38), radius_x=9, sweep=False)
        self.add_line('wire-rise', (48, 38), (48, 34))
        self.add_arc('wire-crest', (48, 34), (58, 34), radius_x=5, radius_y=6)
        self.add_line('wire-fall', (58, 34), (58, 58))
        self.add_contour('box', 'box-top', 'box-ne', 'box-right', 'box-se', 'box-bottom', 'box-sw', 'box-left', 'box-nw', closed=True)
        self.add_contour('wire', 'wire-out', 'wire-rise', 'wire-crest', 'wire-fall')
        self.relate('connect', 'handle', 'plunger')
        self.relate('connect', 'plunger', 'box')
        self.relate('connect', 'wire', 'box')
