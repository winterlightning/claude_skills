'Inscribed stone tablet.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0d17f74-4c9a-4f28-9e4f-254a27312c2d'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/resetta stone_b0d17f74-4c9a-4f28-9e4f-254a27312c2d.svg'
AUTHOR = 'gpt-6'

class InscribedStoneTablet(Solo48):
    icon_id = 'inscribed-stone-tablet'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('rosetta stone', 'tablet', 'inscription', 'hieroglyph', 'ancient', 'archaeology', 'stone', 'script')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_15 = (8, 15)
        p_21_4 = (21, 4)
        p_35_4 = (35, 4)
        p_40_9 = (40, 9)
        p_40_39 = (40, 39)
        p_35_44 = (35, 44)
        p_13_44 = (13, 44)
        p_8_39 = (8, 39)
        p_17_19 = (17, 19)
        p_31_19 = (31, 19)
        p_17_27 = (17, 27)
        p_20_27 = (20, 27)
        p_28_27 = (28, 27)
        p_31_27 = (31, 27)
        p_17_35 = (17, 35)
        p_31_35 = (31, 35)
        self.add_line('fracture', p_8_15, p_21_4)
        self.add_line('top', p_21_4, p_35_4)
        self.add_arc('ne', p_35_4, p_40_9, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('east', p_40_9, p_40_39)
        self.add_arc('se', p_40_39, p_35_44, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('base', p_35_44, p_13_44)
        self.add_arc('sw', p_13_44, p_8_39, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('west', p_8_39, p_8_15)
        self.add_line('inscription-top', p_17_19, p_31_19)
        self.add_line('inscription-middle-left', p_17_27, p_20_27)
        self.add_line('inscription-middle-right', p_28_27, p_31_27)
        self.add_line('inscription-bottom', p_17_35, p_31_35)
        self.add_contour('stone', 'fracture', 'top', 'ne', 'east', 'se', 'base', 'sw', 'west', closed=True)
