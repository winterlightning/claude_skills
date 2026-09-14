'Plumed battle helmet.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8214f96f-5065-5adb-8225-f44c3d1738eb'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/spartan mask_8214f96f-5065-5adb-8225-f44c3d1738eb.svg'
AUTHOR = 'gpt-6'

class PlumedBattleHelmet(Solo48):
    icon_id = 'plumed-battle-helmet'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('helmet', 'plume', 'spartan', 'greek', 'warrior', 'armour', 'battle', 'crest')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_15_25 = (15, 25)
        p_26_13 = (26, 13)
        p_37_25 = (37, 25)
        p_40_32 = (40, 32)
        p_34_32 = (34, 32)
        p_37_44 = (37, 44)
        p_27_37 = (27, 37)
        p_24_28 = (24, 28)
        p_22_36 = (22, 36)
        p_18_36 = (18, 36)
        p_13_36 = (13, 36)
        p_33_4 = (33, 4)
        p_8_28 = (8, 28)
        p_8_37 = (8, 37)
        p_11_44 = (11, 44)
        p_23_41 = (23, 41)
        p_30_44 = (30, 44)
        self.add_arc('dome-left', p_15_25, p_26_13, radius_x=11, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('dome-right', p_26_13, p_37_25, radius_x=11, radius_y=12, sweep=True, large_arc=False)
        self.add_line('face-1', p_37_25, p_40_32)
        self.add_line('face-2', p_40_32, p_34_32)
        self.add_line('face-3', p_34_32, p_37_44)
        self.add_line('face-4', p_37_44, p_27_37)
        self.add_line('face-5', p_27_37, p_24_28)
        self.add_line('face-6', p_24_28, p_22_36)
        self.add_line('face-7', p_22_36, p_18_36)
        self.add_line('face-8', p_18_36, p_13_36)
        self.add_line('face-9', p_13_36, p_15_25)
        self.add_line('plume-attachment', p_26_13, p_33_4)
        self.add_arc('plume', p_33_4, p_8_28, radius_x=25, radius_y=24, sweep=False, large_arc=False)
        self.add_line('plume-end', p_8_28, p_8_37)
        self.add_line('neck-1', p_18_36, p_11_44)
        self.add_line('neck-2', p_11_44, p_23_41)
        self.add_line('neck-3', p_23_41, p_30_44)
        self.add_line('neck-4', p_30_44, p_27_37)
        self.add_contour('helmet', 'dome-left', 'dome-right', 'face-1', 'face-2', 'face-3', 'face-4', 'face-5', 'face-6', 'face-7', 'face-8', 'face-9', closed=True)
        self.add_contour('crest', 'plume-attachment', 'plume', 'plume-end', closed=False)
        self.add_contour('neck', 'neck-1', 'neck-2', 'neck-3', 'neck-4', closed=False)
        self.relate('connect', 'helmet', 'crest')
        self.relate('connect', 'helmet', 'neck')
