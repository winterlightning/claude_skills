'Floppy disk with label.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb516593-c4bd-55b6-bcd2-eef78189bed3'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/floppy disk_cb516593-c4bd-55b6-bcd2-eef78189bed3.svg'
AUTHOR = 'gpt-6'

class FloppyDiskWithLabel(Solo48):
    icon_id = 'floppy-disk-with-label'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('floppy', 'disk', 'diskette', 'save', 'storage', 'retro', 'label', 'data')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_9_6 = (9, 6)
        p_34_6 = (34, 6)
        p_42_14 = (42, 14)
        p_42_39 = (42, 39)
        p_39_42 = (39, 42)
        p_9_42 = (9, 42)
        p_6_39 = (6, 39)
        p_6_9 = (6, 9)
        p_15_6 = (15, 6)
        p_15_17 = (15, 17)
        p_31_17 = (31, 17)
        p_31_6 = (31, 6)
        p_15_42 = (15, 42)
        p_15_25 = (15, 25)
        p_33_25 = (33, 25)
        p_33_42 = (33, 42)
        self.add_line('disk-1', p_9_6, p_34_6)
        self.add_line('disk-2', p_34_6, p_42_14)
        self.add_line('disk-3', p_42_14, p_42_39)
        self.add_arc('se', p_42_39, p_39_42, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('bottom', p_39_42, p_9_42)
        self.add_arc('sw', p_9_42, p_6_39, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('left', p_6_39, p_6_9)
        self.add_arc('nw', p_6_9, p_9_6, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('shutter-1', p_15_6, p_15_17)
        self.add_line('shutter-2', p_15_17, p_31_17)
        self.add_line('shutter-3', p_31_17, p_31_6)
        self.add_line('label-1', p_15_42, p_15_25)
        self.add_line('label-2', p_15_25, p_33_25)
        self.add_line('label-3', p_33_25, p_33_42)
        self.add_contour('case', 'disk-1', 'disk-2', 'disk-3', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
        self.add_contour('shutter', 'shutter-1', 'shutter-2', 'shutter-3', closed=False)
        self.add_contour('label', 'label-1', 'label-2', 'label-3', closed=False)
        self.relate('connect', 'case', 'shutter')
        self.relate('connect', 'case', 'label')
