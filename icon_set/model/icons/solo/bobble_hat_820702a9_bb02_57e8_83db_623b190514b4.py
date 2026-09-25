'Bobble hat.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '820702a9-bb02-57e8-83db-623b190514b4'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/beanie winter_820702a9-bb02-57e8-83db-623b190514b4.svg'
AUTHOR = 'gpt-6'

class BobbleHat(Solo48):
    icon_id = 'bobble-hat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('beanie', 'hat', 'bobble hat', 'winter', 'knit', 'pompom', 'cap', 'clothing')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_24_14 = (24, 14)
        p_24_8 = (24, 8)
        p_6_28 = (6, 28)
        p_42_28 = (42, 28)
        p_42_31 = (42, 31)
        p_6_31 = (6, 31)
        p_7_31 = (7, 31)
        p_41_31 = (41, 31)
        p_44_33 = (44, 33)
        p_44_38 = (44, 38)
        p_41_40 = (41, 40)
        p_7_40 = (7, 40)
        p_4_38 = (4, 38)
        p_4_33 = (4, 33)
        self.add_arc('pompom-a', p_24_14, p_24_8, radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('pompom-b', p_24_8, p_24_14, radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('crown-left', p_6_28, p_24_14, radius_x=18, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('crown-right', p_24_14, p_42_28, radius_x=18, radius_y=15, sweep=True, large_arc=False)
        self.add_line('crown-r', p_42_28, p_42_31)
        self.add_line('crown-l', p_6_31, p_6_28)
        self.add_line('cuff-0', p_7_31, p_41_31)
        self.add_arc('cuff-1', p_41_31, p_44_33, radius_x=3, radius_y=2, sweep=True, large_arc=False)
        self.add_line('cuff-2', p_44_33, p_44_38)
        self.add_arc('cuff-3', p_44_38, p_41_40, radius_x=3, radius_y=2, sweep=True, large_arc=False)
        self.add_line('cuff-4', p_41_40, p_7_40)
        self.add_arc('cuff-5', p_7_40, p_4_38, radius_x=3, radius_y=2, sweep=True, large_arc=False)
        self.add_line('cuff-6', p_4_38, p_4_33)
        self.add_arc('cuff-7', p_4_33, p_7_31, radius_x=3, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('pompom', 'pompom-a', 'pompom-b', closed=True)
        self.add_contour('crown', 'crown-l', 'crown-left', 'crown-right', 'crown-r', closed=False)
        self.add_contour('cuff', 'cuff-0', 'cuff-1', 'cuff-2', 'cuff-3', 'cuff-4', 'cuff-5', 'cuff-6', 'cuff-7', closed=True)
        self.relate('connect', 'pompom', 'crown')
        self.relate('connect', 'crown', 'cuff')
