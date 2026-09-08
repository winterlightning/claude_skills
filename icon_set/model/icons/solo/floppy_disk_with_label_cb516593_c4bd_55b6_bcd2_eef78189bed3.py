"""Clipped corner disk with shutter and label. Extremes (2,2)-(46,46). Lucide save; one label line replaces two and shutter aperture becomes a slot."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb516593-c4bd-55b6-bcd2-eef78189bed3'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/floppy disk_cb516593-c4bd-55b6-bcd2-eef78189bed3.svg'
AUTHOR = 'astra-chatgpt'

class FloppyDiskWithLabel(Solo48):
    icon_id = 'floppy-disk-with-label'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('floppy', 'disk', 'diskette', 'save', 'storage', 'retro', 'label', 'data')

    def build(self) -> None:
        self.add_line('disk-1', (6, 2), (36, 2))
        self.add_line('disk-2', (36, 2), (46, 12))
        self.add_line('disk-3', (46, 12), (46, 42))
        self.add_arc('se', (46, 42), (42, 46), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom', (42, 46), (6, 46))
        self.add_arc('sw', (6, 46), (2, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left', (2, 42), (2, 6))
        self.add_arc('nw', (2, 6), (6, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('case', 'disk-1', 'disk-2', 'disk-3', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
        self.add_polyline('shutter', (11, 2), (11, 16), (33, 16), (33, 2), closed=False)
        self.relate('connect', 'case', 'shutter')
        self.add_line('slot', (25, 2), (25, 9))
        self.relate('connect', 'case', 'slot')
        self.relate('connect', 'shutter', 'slot')
        self.add_polyline('label', (11, 46), (11, 25), (37, 25), (37, 46), closed=False)
        self.relate('connect', 'case', 'label')
        self.add_line('writing', (19, 35), (29, 35))
