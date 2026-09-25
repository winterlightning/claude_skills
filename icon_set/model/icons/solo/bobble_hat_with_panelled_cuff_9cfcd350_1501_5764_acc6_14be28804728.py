"""Remove both cuff divider lines; retain the single crown-to-cuff division. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9cfcd350-1501-5764-acc6-14be28804728'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/beanie winter_9cfcd350-1501-5764-acc6-14be28804728.svg'
AUTHOR = 'gpt-6'

class BobbleHatWithPanelledCuff(Solo48):
    icon_id = 'bobble-hat-with-panelled-cuff'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('beanie', 'hat', 'bobble hat', 'winter', 'knit', 'pompom', 'cuff', 'clothing')

    def build(self) -> None:
        """Symbol plan: Remove both cuff divider lines; retain the single crown-to-cuff division. Reference: inspected current parent; no useful exact Lucide match selected."""
        p_11_31 = (11, 31)
        p_19_31 = (19, 31)
        p_29_31 = (29, 31)
        p_37_31 = (37, 31)
        p_40_34 = (40, 34)
        p_40_41 = (40, 41)
        p_37_44 = (37, 44)
        p_29_44 = (29, 44)
        p_19_44 = (19, 44)
        p_11_44 = (11, 44)
        p_8_41 = (8, 41)
        p_8_34 = (8, 34)
        p_24_13 = (24, 13)
        p_24_4 = (24, 4)
        p_28_9 = (28, 9)
        p_20_9 = (20, 9)
        self.add_line('cuff-0-attach-0', p_11_31, p_19_31)
        self.add_line('cuff-0-attach-1', p_19_31, p_29_31)
        self.add_line('cuff-0-attach-2', p_29_31, p_37_31)
        self.add_arc('cuff-1', p_37_31, p_40_34, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cuff-2', p_40_34, p_40_41)
        self.add_arc('cuff-3', p_40_41, p_37_44, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cuff-4-attach-0', p_37_44, p_29_44)
        self.add_line('cuff-4-attach-1', p_29_44, p_19_44)
        self.add_line('cuff-4-attach-2', p_19_44, p_11_44)
        self.add_arc('cuff-5', p_11_44, p_8_41, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cuff-6', p_8_41, p_8_34)
        self.add_arc('cuff-7', p_8_34, p_11_31, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('crown-left', p_11_31, p_24_13, radius_x=13, radius_y=18, sweep=True, large_arc=False)
        self.add_arc('crown-right', p_24_13, p_37_31, radius_x=13, radius_y=18, sweep=True, large_arc=False)
        self.add_arc('bobble-0', p_24_4, p_28_9, radius_x=4, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('bobble-1', p_28_9, p_24_13, radius_x=4, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('bobble-2', p_24_13, p_20_9, radius_x=4, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('bobble-3', p_20_9, p_24_4, radius_x=4, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('cuff', 'cuff-0-attach-0', 'cuff-0-attach-1', 'cuff-0-attach-2', 'cuff-1', 'cuff-2', 'cuff-3', 'cuff-4-attach-0', 'cuff-4-attach-1', 'cuff-4-attach-2', 'cuff-5', 'cuff-6', 'cuff-7', closed=True)
        self.add_contour('crown', 'crown-left', 'crown-right', closed=False)
        self.add_contour('bobble', 'bobble-0', 'bobble-1', 'bobble-2', 'bobble-3', closed=True)
        self.relate('connect', 'bobble', 'crown')
        self.relate('connect', 'cuff', 'crown')
