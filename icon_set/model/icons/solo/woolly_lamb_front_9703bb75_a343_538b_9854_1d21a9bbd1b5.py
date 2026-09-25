'Woolly lamb front.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9703bb75-a343-538b-9854-1d21a9bbd1b5'
SOURCE_PATH = 'pictographic-primitives/animals/lamb_9703bb75-a343-538b-9854-1d21a9bbd1b5.svg'
AUTHOR = 'gpt-6'

class WoollyLambFront(Solo48):
    icon_id = 'woolly-lamb-front'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('lamb', 'sheep', 'wool', 'fluffy', 'face', 'farm', 'livestock', 'front')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_12_12 = (12, 12)
        p_36_12 = (36, 12)
        p_36_36 = (36, 36)
        p_12_36 = (12, 36)
        p_18_22 = (18, 22)
        p_30_22 = (30, 22)
        p_33_26 = (33, 26)
        p_30_26 = (30, 26)
        p_24_33 = (24, 33)
        p_18_26 = (18, 26)
        p_15_26 = (15, 26)
        p_10_40 = (10, 40)
        p_38_40 = (38, 40)
        self.add_arc('fleece-top', p_12_12, p_36_12, radius_x=12, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('fleece-right', p_36_12, p_36_36, radius_x=6, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('fleece-bottom', p_36_36, p_12_36, radius_x=12, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('fleece-left', p_12_36, p_12_12, radius_x=6, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('face-top', p_18_22, p_30_22, radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('ear-right-0', p_30_22, p_33_26, radius_x=4, radius_y=4)
        self.add_arc('ear-right-1', p_33_26, p_30_26, radius_x=4, radius_y=4)
        self.add_arc('jaw-right', p_30_26, p_24_33, radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('jaw-left', p_24_33, p_18_26, radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('ear-left-0', p_18_26, p_15_26, radius_x=4, radius_y=4)
        self.add_arc('ear-left-1', p_15_26, p_18_22, radius_x=4, radius_y=4)
        self.add_line('leg-left', p_12_36, p_10_40)
        self.add_line('leg-right', p_36_36, p_38_40)
        self.add_contour('fleece', 'fleece-top', 'fleece-right', 'fleece-bottom', 'fleece-left', closed=True)
        self.add_contour('face', 'face-top', 'ear-right-0', 'ear-right-1', 'jaw-right', 'jaw-left', 'ear-left-0', 'ear-left-1', closed=True)
        self.relate('connect', 'fleece', 'leg-left')
        self.relate('connect', 'fleece', 'leg-right')
