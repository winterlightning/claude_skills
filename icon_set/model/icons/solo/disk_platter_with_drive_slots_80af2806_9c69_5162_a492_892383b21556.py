"""A magnetic disk platter with a hub and three radial drive slots.

Lucide disc informs concentric circles. The three tapered outlined slots
reduce to short radial strokes so their threefold arrangement stays legible.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80af2806-9c69-5162-a492-892383b21556'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/floppy disk_80af2806-9c69-5162-a492-892383b21556.svg'


class DiskPlatterWithDriveSlots(Solo48):
    icon_id = 'disk-platter-with-drive-slots'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('disk', 'platter', 'floppy', 'hub', 'storage', 'media', 'spindle', 'drive')

    def build(self) -> None:
        self.add_arc('rim-0', (24, 2), (46, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-1', (46, 24), (24, 46), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-2', (24, 46), (2, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-3', (2, 24), (24, 2), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_contour('rim', 'rim-0', 'rim-1', 'rim-2', 'rim-3', closed=True)
        self.add_arc('hub-0', (24, 21), (27, 24), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('hub-1', (27, 24), (24, 27), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('hub-2', (24, 27), (21, 24), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('hub-3', (21, 24), (24, 21), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('hub', 'hub-0', 'hub-1', 'hub-2', 'hub-3', closed=True)
        self.add_line('slot-top', (24, 10), (24, 13))
        self.add_line('slot-left', (12, 31), (15, 29))
        self.add_line('slot-right', (33, 29), (36, 31))
