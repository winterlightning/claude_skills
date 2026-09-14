'Floppy disk.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48975063-b353-533e-ada8-826f1f506264'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/floppy disk_48975063-b353-533e-ada8-826f1f506264.svg'
AUTHOR = 'gpt-6'

class FloppyDisk(Solo48):
    icon_id = 'floppy-disk'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('floppy', 'disk', 'diskette', 'save', 'storage', 'retro', 'media', 'data')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_6 = (8, 6)
        p_40_6 = (40, 6)
        p_42_8 = (42, 8)
        p_42_40 = (42, 40)
        p_40_42 = (40, 42)
        p_8_42 = (8, 42)
        p_6_40 = (6, 40)
        p_6_8 = (6, 8)
        p_15_6 = (15, 6)
        p_15_16 = (15, 16)
        p_33_16 = (33, 16)
        p_33_6 = (33, 6)
        p_15_42 = (15, 42)
        p_15_34 = (15, 34)
        p_33_34 = (33, 34)
        p_33_42 = (33, 42)
        p_24_25 = (24, 25)
        self.add_line('disk-t', p_8_6, p_40_6)
        self.add_arc('disk-ne', p_40_6, p_42_8, radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_line('disk-r', p_42_8, p_42_40)
        self.add_arc('disk-se', p_42_40, p_40_42, radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_line('disk-b', p_40_42, p_8_42)
        self.add_arc('disk-sw', p_8_42, p_6_40, radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_line('disk-l', p_6_40, p_6_8)
        self.add_arc('disk-nw', p_6_8, p_8_6, radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_line('shutter-1', p_15_6, p_15_16)
        self.add_line('shutter-2', p_15_16, p_33_16)
        self.add_line('shutter-3', p_33_16, p_33_6)
        self.add_line('label-1', p_15_42, p_15_34)
        self.add_line('label-2', p_15_34, p_33_34)
        self.add_line('label-3', p_33_34, p_33_42)
        self.add_line('hub', p_24_25, p_24_25)
        self.add_contour('disk', 'disk-t', 'disk-ne', 'disk-r', 'disk-se', 'disk-b', 'disk-sw', 'disk-l', 'disk-nw', closed=True)
        self.add_contour('shutter', 'shutter-1', 'shutter-2', 'shutter-3', closed=False)
        self.add_contour('label', 'label-1', 'label-2', 'label-3', closed=False)
        self.relate('connect', 'disk', 'shutter')
        self.relate('connect', 'disk', 'label')
