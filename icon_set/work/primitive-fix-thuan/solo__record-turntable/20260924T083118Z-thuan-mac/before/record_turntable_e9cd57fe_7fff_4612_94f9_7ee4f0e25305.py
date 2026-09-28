'Record turntable.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9cd57fe-7fff-4612-94f9-7ee4f0e25305'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/turntable 1_e9cd57fe-7fff-4612-94f9-7ee4f0e25305.svg'
AUTHOR = 'gpt-6'

class RecordTurntable(Solo48):
    icon_id = 'record-turntable'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('turntable', 'record player', 'vinyl', 'dj', 'music', 'audio', 'platter', 'deck')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_11_6 = (11, 6)
        p_37_6 = (37, 6)
        p_42_8 = (42, 8)
        p_42_40 = (42, 40)
        p_37_42 = (37, 42)
        p_11_42 = (11, 42)
        p_6_40 = (6, 40)
        p_6_8 = (6, 8)
        p_33_24 = (33, 24)
        p_24_33 = (24, 33)
        p_15_24 = (15, 24)
        p_24_15 = (24, 15)
        p_24_24 = (24, 24)
        p_15_33 = (15, 33)
        self.add_line('deck-top0', p_11_6, p_37_6)
        self.add_arc('deck-ne', p_37_6, p_42_8, radius_x=5, radius_y=2, sweep=True, large_arc=False)
        self.add_line('deck-right', p_42_8, p_42_40)
        self.add_arc('deck-se', p_42_40, p_37_42, radius_x=5, radius_y=2, sweep=True, large_arc=False)
        self.add_line('deck-bottom0', p_37_42, p_11_42)
        self.add_arc('deck-sw', p_11_42, p_6_40, radius_x=5, radius_y=2, sweep=True, large_arc=False)
        self.add_line('deck-left', p_6_40, p_6_8)
        self.add_arc('deck-nw', p_6_8, p_11_6, radius_x=5, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('platter0', p_33_24, p_24_33, radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('platter1', p_24_33, p_15_24, radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('platter2', p_15_24, p_24_15, radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('platter3', p_24_15, p_33_24, radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_line('spindle', p_24_24, p_24_24)
        self.add_line('tonearm', p_24_24, p_15_33)
        self.add_contour('deck', 'deck-top0', 'deck-ne', 'deck-right', 'deck-se', 'deck-bottom0', 'deck-sw', 'deck-left', 'deck-nw', closed=True)
        self.add_contour('platter', 'platter0', 'platter1', 'platter2', 'platter3', closed=True)
        self.relate('connect', 'spindle', 'tonearm')
        self.relate('connect', 'platter', 'tonearm')
