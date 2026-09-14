'Baby figure.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.\nHuman construction: icon_set/references/human_ref/full_body_ref.png and\nicon_set/references/human_ref/user.svg. Circular head radius 6,\nwith exactly 8 units of centerline head-to-body separation (4 visible units).'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e4bd3c6-f290-4652-9dfa-4a17d82dca3d'
SOURCE_PATH = 'pictographic-primitives/babies/family baby_8e4bd3c6-f290-4652-9dfa-4a17d82dca3d.svg'
AUTHOR = 'gpt-6'

class BabyFigure(Solo48):
    icon_id = 'baby-figure'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('baby', 'figure', 'infant', 'nursery')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_18_10 = (18, 10)
        p_30_10 = (30, 10)
        p_18_24 = (18, 24)
        p_30_24 = (30, 24)
        p_8_34 = (8, 34)
        p_40_34 = (40, 34)
        p_17_37 = (17, 37)
        p_31_37 = (31, 37)
        p_12_42 = (12, 42)
        p_17_42 = (17, 42)
        p_36_42 = (36, 42)
        p_31_42 = (31, 42)
        self.add_arc('head-top', p_18_10, p_30_10, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('head-bottom', p_30_10, p_18_10, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('shoulders', p_18_24, p_30_24)
        self.add_line('arm-left', p_18_24, p_8_34)
        self.add_line('arm-right', p_30_24, p_40_34)
        self.add_line('waist-left', p_18_24, p_17_37)
        self.add_line('waist-right', p_30_24, p_31_37)
        self.add_line('diaper-band', p_17_37, p_31_37)
        self.add_arc('diaper', p_17_37, p_31_37, radius_x=7, radius_y=7, sweep=False, large_arc=False)
        self.add_line('leg-left-1', p_17_37, p_12_42)
        self.add_line('leg-left-2', p_12_42, p_17_42)
        self.add_line('leg-right-1', p_31_37, p_36_42)
        self.add_line('leg-right-2', p_36_42, p_31_42)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('leg-left', 'leg-left-1', 'leg-left-2', closed=False)
        self.add_contour('leg-right', 'leg-right-1', 'leg-right-2', closed=False)
        self.relate('connect', 'shoulders', 'waist-left')
        self.relate('connect', 'shoulders', 'waist-right')
        self.relate('connect', 'shoulders', 'arm-left')
        self.relate('connect', 'shoulders', 'arm-right')
        self.relate('connect', 'arm-left', 'waist-left')
        self.relate('connect', 'arm-right', 'waist-right')
        self.relate('connect', 'waist-left', 'diaper-band')
        self.relate('connect', 'waist-right', 'diaper-band')
        self.relate('connect', 'diaper-band', 'diaper')
        self.relate('connect', 'waist-left', 'diaper')
        self.relate('connect', 'waist-right', 'diaper')
        self.relate('connect', 'leg-left', 'waist-left')
        self.relate('connect', 'leg-left', 'diaper')
        self.relate('connect', 'leg-left', 'diaper-band')
        self.relate('connect', 'leg-right', 'waist-right')
        self.relate('connect', 'leg-right', 'diaper')
        self.relate('connect', 'leg-right', 'diaper-band')
