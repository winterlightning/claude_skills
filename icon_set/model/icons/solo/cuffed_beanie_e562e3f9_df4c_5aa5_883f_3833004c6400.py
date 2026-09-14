'Cuffed beanie.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e562e3f9-df4c-5aa5-883f-3833004c6400'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/beanie_e562e3f9-df4c-5aa5-883f-3833004c6400.svg'
AUTHOR = 'gpt-6'

class CuffedBeanie(Solo48):
    icon_id = 'cuffed-beanie'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('beanie', 'hat', 'winter', 'knit', 'cap', 'cuff', 'clothing', 'headwear')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_7_30 = (7, 30)
        p_8_30 = (8, 30)
        p_40_30 = (40, 30)
        p_41_30 = (41, 30)
        p_44_32 = (44, 32)
        p_44_37 = (44, 37)
        p_41_40 = (41, 40)
        p_7_40 = (7, 40)
        p_4_37 = (4, 37)
        p_4_32 = (4, 32)
        p_8_23 = (8, 23)
        p_40_23 = (40, 23)
        self.add_line('cuff0', p_7_30, p_8_30)
        self.add_line('cuff-top', p_8_30, p_40_30)
        self.add_line('cuff-end', p_40_30, p_41_30)
        self.add_arc('cuff1', p_41_30, p_44_32, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cuff2', p_44_32, p_44_37)
        self.add_arc('cuff3', p_44_37, p_41_40, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cuff4', p_41_40, p_7_40)
        self.add_arc('cuff5', p_7_40, p_4_37, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cuff6', p_4_37, p_4_32)
        self.add_arc('cuff7', p_4_32, p_7_30, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('crown-l', p_8_30, p_8_23)
        self.add_arc('crown', p_8_23, p_40_23, radius_x=16, radius_y=15, sweep=True, large_arc=False)
        self.add_line('crown-r', p_40_23, p_40_30)
        self.add_contour('cuff', 'cuff0', 'cuff-top', 'cuff-end', 'cuff1', 'cuff2', 'cuff3', 'cuff4', 'cuff5', 'cuff6', 'cuff7', closed=True)
        self.add_contour('crown-outline', 'crown-l', 'crown', 'crown-r', closed=False)
        self.relate('connect', 'cuff', 'crown-outline')
