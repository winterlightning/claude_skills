"""Remove both internal crown seams. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '145bee6b-f64f-518f-a631-9a382415349d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/beanie winter_145bee6b-f64f-518f-a631-9a382415349d.svg'
AUTHOR = 'gpt-6'

class BobbleHatWithSeams(Solo48):
    icon_id = 'bobble-hat-with-seams'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('beanie', 'hat', 'bobble hat', 'winter', 'knit', 'pompom', 'cap', 'clothing')

    def build(self) -> None:
        """Symbol plan: Remove both internal crown seams. Reference: inspected current parent; no useful exact Lucide match selected."""
        p_7_31 = (7, 31)
        p_41_31 = (41, 31)
        p_44_33 = (44, 33)
        p_44_38 = (44, 38)
        p_41_40 = (41, 40)
        p_7_40 = (7, 40)
        p_4_38 = (4, 38)
        p_4_33 = (4, 33)
        p_7_28 = (7, 28)
        p_24_16 = (24, 16)
        p_41_28 = (41, 28)
        p_24_8 = (24, 8)
        p_17_25 = (17, 25)
        p_17_31 = (17, 31)
        p_31_25 = (31, 25)
        p_31_31 = (31, 31)
        self.add_line('cuff0', p_7_31, p_41_31)
        self.add_arc('cuff1', p_41_31, p_44_33, radius_x=3, radius_y=2, sweep=True, large_arc=False)
        self.add_line('cuff2', p_44_33, p_44_38)
        self.add_arc('cuff3', p_44_38, p_41_40, radius_x=3, radius_y=2, sweep=True, large_arc=False)
        self.add_line('cuff4', p_41_40, p_7_40)
        self.add_arc('cuff5', p_7_40, p_4_38, radius_x=3, radius_y=2, sweep=True, large_arc=False)
        self.add_line('cuff6', p_4_38, p_4_33)
        self.add_arc('cuff7', p_4_33, p_7_31, radius_x=3, radius_y=2, sweep=True, large_arc=False)
        self.add_line('crown-l', p_7_31, p_7_28)
        self.add_arc('crown-a', p_7_28, p_24_16, radius_x=17, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('crown-b', p_24_16, p_41_28, radius_x=17, radius_y=12, sweep=True, large_arc=False)
        self.add_line('crown-r', p_41_28, p_41_31)
        self.add_arc('bobble-a', p_24_8, p_24_16, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('bobble-b', p_24_16, p_24_8, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('cuff', 'cuff0', 'cuff1', 'cuff2', 'cuff3', 'cuff4', 'cuff5', 'cuff6', 'cuff7', closed=True)
        self.add_contour('crown', 'crown-l', 'crown-a', 'crown-b', 'crown-r', closed=False)
        self.add_contour('bobble', 'bobble-a', 'bobble-b', closed=True)
        self.relate('connect', 'crown', 'cuff')
        self.relate('connect', 'bobble', 'crown')
