"""A light bulb is assembled from interlocking puzzle pieces, with a curved piece lifted away at the upper right. Rounded tabs and sockets divide the glass above a narrow base and terminal.
Lucide puzzle socket and lightbulb shoulder construction. One large socket and lifted curved piece replace four tightly divided pieces. Rounded base retained; tiny terminal omitted. Intentional missing upper-right section.
VRECT_L: centerline extremes (8,6)-(40,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8013a3c2-dcf3-475e-98f6-cb6db629e137'
SOURCE_PATH = 'pictographic-primitives/work/workflow coaching puzzle lightbulb_8013a3c2-dcf3-475e-98f6-cb6db629e137.svg'
AUTHOR = 'gpt-6'


class JigsawLightBulb(Solo48):
    icon_id = 'jigsaw-light-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('bulb', 'puzzle', 'jigsaw', 'idea', 'solution', 'creativity')

    def build(self) -> None:
        self.add_arc('glass-upper-left', (8, 20), (24, 6), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_line('piece-edge', (24, 6), (24, 12))
        self.add_arc('socket', (24, 12), (24, 20), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_line('piece-bottom', (24, 20), (40, 20))
        self.add_arc('shoulder-right', (40, 20), (34, 32), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('neck-right', (34, 32), (32, 36), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('base-right', (32, 36), (32, 40))
        self.add_arc('cap-right', (32, 40), (28, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('cap-bottom', (28, 42), (20, 42))
        self.add_arc('cap-left', (20, 42), (16, 40), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('base-left', (16, 40), (16, 36))
        self.add_arc('neck-left', (16, 36), (14, 32), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_arc('shoulder-left', (14, 32), (8, 20), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_contour('bulb', 'glass-upper-left', 'piece-edge', 'socket', 'piece-bottom', 'shoulder-right', 'neck-right', 'base-right', 'cap-right', 'cap-bottom', 'cap-left', 'base-left', 'neck-left', 'shoulder-left', closed=True)
        self.add_line('base-seam', (16, 36), (32, 36))
        self.relate("connect", 'base-seam', 'bulb')
        self.add_arc('lifted-piece', (33, 6), (40, 11), radius_x=7, radius_y=7, sweep=True, large_arc=False)
