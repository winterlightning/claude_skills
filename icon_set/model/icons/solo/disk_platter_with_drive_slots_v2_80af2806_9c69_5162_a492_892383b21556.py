# Variant of disk-platter-with-drive-slots; parent file remains unchanged.
'Solid spindle dot. Independent feedback revision; preserve source subject.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80af2806-9c69-5162-a492-892383b21556'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/floppy disk_80af2806-9c69-5162-a492-892383b21556.svg'
AUTHOR = 'gpt-6'

class DiskPlatterWithDriveSlotsVariant2(Solo48):
    icon_id = 'disk-platter-with-drive-slots-v2'
    variant_of = 'disk-platter-with-drive-slots'
    variant_label = 'Solid spindle dot'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('disk', 'platter', 'floppy', 'hub', 'storage', 'media', 'spindle', 'drive')

    def build(self) -> None:
        self.add_arc('rim-0', (24, 2), (46, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-1', (46, 24), (24, 46), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-2', (24, 46), (2, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-3', (2, 24), (24, 2), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_contour('rim', 'rim-0', 'rim-1', 'rim-2', 'rim-3', closed=True)
        self.add_line('slot-top', (24, 10), (24, 13))
        self.add_line('slot-left', (12, 31), (15, 29))
        self.add_line('slot-right', (33, 29), (36, 31))
        self.add_dot('hub', (24, 24))
