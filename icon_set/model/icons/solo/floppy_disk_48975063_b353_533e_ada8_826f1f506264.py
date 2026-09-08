"""Square disk with shutter, circular hub and bottom label. Extremes (2,2)-(46,46); Lucide save attached panels."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48975063-b353-533e-ada8-826f1f506264'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/floppy disk_48975063-b353-533e-ada8-826f1f506264.svg'
AUTHOR = 'astra-chatgpt'

class FloppyDisk(Solo48):
    icon_id = 'floppy-disk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('floppy', 'disk', 'diskette', 'save', 'storage', 'retro', 'media', 'data')

    def build(self) -> None:
        self.add_line('disk-t', (5, 2), (43, 2))
        self.add_arc('disk-ne', (43, 2), (46, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_line('disk-r', (46, 5), (46, 43))
        self.add_arc('disk-se', (46, 43), (43, 46), radius_x=3, radius_y=3, sweep=True)
        self.add_line('disk-b', (43, 46), (5, 46))
        self.add_arc('disk-sw', (5, 46), (2, 43), radius_x=3, radius_y=3, sweep=True)
        self.add_line('disk-l', (2, 43), (2, 5))
        self.add_arc('disk-nw', (2, 5), (5, 2), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('disk', 'disk-t', 'disk-ne', 'disk-r', 'disk-se', 'disk-b', 'disk-sw', 'disk-l', 'disk-nw', closed=True)
        self.add_polyline('shutter', (11, 2), (11, 14), (37, 14), (37, 2), closed=False)
        self.relate('connect', 'disk', 'shutter')
        self.add_arc('hub-top', (20, 26), (28, 26), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('hub-bottom', (28, 26), (20, 26), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('hub', 'hub-top', 'hub-bottom', closed=True)
        self.add_polyline('label', (11, 46), (11, 38), (37, 38), (37, 46), closed=False)
        self.relate('connect', 'disk', 'label')
