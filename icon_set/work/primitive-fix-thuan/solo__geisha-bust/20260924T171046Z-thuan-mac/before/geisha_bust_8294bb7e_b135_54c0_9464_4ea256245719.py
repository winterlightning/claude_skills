'Geisha bust.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.\nHuman construction: icon_set/references/human_ref/full_body_ref.png and\nicon_set/references/human_ref/user.svg. Circular head radius 9,\nwith exactly 8 units of centerline head-to-body separation (4 visible units).'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8294bb7e-b135-54c0-9464-4ea256245719'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/geisha_8294bb7e-b135-54c0-9464-4ea256245719.svg'
AUTHOR = 'gpt-6'

class GeishaBust(Solo48):
    icon_id = 'geisha-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture/objects'
    aliases = ()
    keywords = ('geisha', 'japanese', 'kimono', 'hairpin', 'traditional', 'woman', 'culture', 'asian')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_15_21 = (15, 21)
        p_24_12 = (24, 12)
        p_33_21 = (33, 21)
        p_20_8 = (20, 8)
        p_28_8 = (28, 8)
        p_8_4 = (8, 4)
        p_40_4 = (40, 4)
        p_8_44 = (8, 44)
        p_14_38 = (14, 38)
        p_34_38 = (34, 38)
        p_40_44 = (40, 44)
        self.add_arc('head-tl', p_15_21, p_24_12, radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('head-tr', p_24_12, p_33_21, radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('head-bottom', p_33_21, p_15_21, radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('bun-top', p_20_8, p_28_8, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('bun-bottom', p_28_8, p_20_8, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('pin-left', p_8_4, p_24_12)
        self.add_line('pin-right', p_40_4, p_24_12)
        self.add_arc('shoulder-left', p_8_44, p_14_38, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('shoulders', p_14_38, p_34_38)
        self.add_arc('shoulder-right', p_34_38, p_40_44, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('head', 'head-tl', 'head-tr', 'head-bottom', closed=True)
        self.add_contour('bun', 'bun-top', 'bun-bottom', closed=True)
        self.add_contour('garment', 'shoulder-left', 'shoulders', 'shoulder-right', closed=False)
        self.relate('connect', 'head', 'bun')
        self.relate('connect', 'head', 'pin-left')
        self.relate('connect', 'head', 'pin-right')
        self.relate('connect', 'bun', 'pin-left')
        self.relate('connect', 'bun', 'pin-right')
        self.relate('connect', 'pin-left', 'pin-right')
