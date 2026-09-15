'Knit winter hat.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc66d74c-cb01-4d93-a56d-1c086f98ec0d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/hat winter_bc66d74c-cb01-4d93-a56d-1c086f98ec0d.svg'
AUTHOR = 'gpt-6'

class KnitWinterHat(Solo48):
    icon_id = 'knit-winter-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('hat', 'winter hat', 'beanie', 'knit', 'cuff', 'cold', 'headwear', 'clothing')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_9_29 = (9, 29)
        p_9_23 = (9, 23)
        p_39_23 = (39, 23)
        p_39_29 = (39, 29)
        p_42_33 = (42, 33)
        p_42_38 = (42, 38)
        p_39_42 = (39, 42)
        p_9_42 = (9, 42)
        p_6_38 = (6, 38)
        p_6_33 = (6, 33)
        self.add_line('crown-left', p_9_29, p_9_23)
        self.add_arc('dome', p_9_23, p_39_23, radius_x=15, radius_y=17, sweep=True, large_arc=False)
        self.add_line('crown-right', p_39_23, p_39_29)
        self.add_line('cuff-0', p_9_29, p_39_29)
        self.add_arc('cuff-1', p_39_29, p_42_33, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('cuff-2', p_42_33, p_42_38)
        self.add_arc('cuff-3', p_42_38, p_39_42, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('cuff-4', p_39_42, p_9_42)
        self.add_arc('cuff-5', p_9_42, p_6_38, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('cuff-6', p_6_38, p_6_33)
        self.add_arc('cuff-7', p_6_33, p_9_29, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('crown', 'crown-left', 'dome', 'crown-right', closed=False)
        self.add_contour('cuff', 'cuff-0', 'cuff-1', 'cuff-2', 'cuff-3', 'cuff-4', 'cuff-5', 'cuff-6', 'cuff-7', closed=True)
        self.relate('connect', 'crown', 'cuff')
