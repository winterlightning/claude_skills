'Feathered war bonnet.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ae08697-a439-498f-937f-0695fa985da7'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/indian feather_5ae08697-a439-498f-937f-0695fa985da7.svg'
AUTHOR = 'gpt-6'

class FeatheredWarBonnet(Solo48):
    icon_id = 'feathered-war-bonnet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('headdress', 'war bonnet', 'feather', 'native american', 'tribal', 'ceremonial', 'plains', 'culture')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_11_34 = (11, 34)
        p_37_34 = (37, 34)
        p_20_22 = (20, 22)
        p_20_13 = (20, 13)
        p_24_6 = (24, 6)
        p_28_13 = (28, 13)
        p_28_22 = (28, 22)
        p_12_24 = (12, 24)
        p_8_16 = (8, 16)
        p_6_10 = (6, 10)
        p_12_13 = (12, 13)
        p_36_24 = (36, 24)
        p_40_16 = (40, 16)
        p_42_10 = (42, 10)
        p_36_13 = (36, 13)
        p_11_42 = (11, 42)
        p_37_42 = (37, 42)
        self.add_arc('band', p_11_34, p_37_34, radius_x=20, radius_y=10, sweep=True, large_arc=False)
        self.add_line('center-feather-1', p_20_22, p_20_13)
        self.add_line('center-feather-2', p_20_13, p_24_6)
        self.add_line('center-feather-3', p_24_6, p_28_13)
        self.add_line('center-feather-4', p_28_13, p_28_22)
        self.add_line('left-feather-1', p_12_24, p_8_16)
        self.add_line('left-feather-2', p_8_16, p_6_10)
        self.add_line('left-feather-3', p_6_10, p_12_13)
        self.add_line('right-feather-1', p_36_24, p_40_16)
        self.add_line('right-feather-2', p_40_16, p_42_10)
        self.add_line('right-feather-3', p_42_10, p_36_13)
        self.add_arc('left-pendant', p_11_34, p_11_42, radius_x=4, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('right-pendant', p_37_34, p_37_42, radius_x=4, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('center-feather', 'center-feather-1', 'center-feather-2', 'center-feather-3', 'center-feather-4', closed=False)
        self.add_contour('left-feather', 'left-feather-1', 'left-feather-2', 'left-feather-3', closed=False)
        self.add_contour('right-feather', 'right-feather-1', 'right-feather-2', 'right-feather-3', closed=False)
        self.relate('connect', 'band', 'left-pendant')
        self.relate('connect', 'band', 'right-pendant')
