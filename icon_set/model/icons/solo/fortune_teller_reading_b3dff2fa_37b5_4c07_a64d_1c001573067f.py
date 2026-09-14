'Fortune teller reading.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.\nHuman construction: icon_set/references/human_ref/full_body_ref.png and\nicon_set/references/human_ref/user.svg. Circular head radius 5,\nwith exactly 8 units of centerline head-to-body separation (4 visible units).'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3dff2fa-37b5-4c07-a64d-1c001573067f'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/sphere teller_b3dff2fa-37b5-4c07-a64d-1c001573067f.svg'
AUTHOR = 'gpt-6'

class FortuneTellerReading(Solo48):
    icon_id = 'fortune-teller-reading'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture/objects'
    aliases = ()
    keywords = ('fortune teller', 'crystal ball', 'divination', 'psychic', 'reading', 'mystic', 'seance', 'future')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_7_11 = (7, 11)
        p_17_11 = (17, 11)
        p_12_24 = (12, 24)
        p_6_34 = (6, 34)
        p_14_34 = (14, 34)
        p_18_42 = (18, 42)
        p_20_32 = (20, 32)
        p_26_20 = (26, 20)
        p_42_20 = (42, 20)
        p_34_28 = (34, 28)
        p_34_34 = (34, 34)
        p_29_34 = (29, 34)
        p_42_34 = (42, 34)
        p_34_42 = (34, 42)
        self.add_arc('head-top', p_7_11, p_17_11, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('head-bottom', p_17_11, p_7_11, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('seated-body-0', p_12_24, p_6_34)
        self.add_line('seated-body-1', p_6_34, p_14_34)
        self.add_line('seated-body-2', p_14_34, p_18_42)
        self.add_line('reaching-arm', p_12_24, p_20_32)
        self.add_arc('ball-top', p_26_20, p_42_20, radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('ball-br', p_42_20, p_34_28, radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('ball-bl', p_34_28, p_26_20, radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('stand', p_34_28, p_34_34)
        self.add_line('table-0', p_29_34, p_34_34)
        self.add_line('table-1', p_34_34, p_42_34)
        self.add_line('table-leg', p_34_34, p_34_42)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('seated-body', 'seated-body-0', 'seated-body-1', 'seated-body-2', closed=False)
        self.add_contour('ball', 'ball-top', 'ball-br', 'ball-bl', closed=True)
        self.add_contour('table', 'table-0', 'table-1', closed=False)
        self.relate('connect', 'reaching-arm', 'seated-body')
        self.relate('connect', 'ball', 'stand')
        self.relate('connect', 'stand', 'table')
        self.relate('connect', 'table-leg', 'table')
        self.relate('connect', 'table-leg', 'stand')
