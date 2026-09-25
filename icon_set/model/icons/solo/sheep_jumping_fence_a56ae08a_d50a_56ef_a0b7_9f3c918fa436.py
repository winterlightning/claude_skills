'Sheep jumping fence.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a56ae08a-d50a-56ef-a0b7-9f3c918fa436'
SOURCE_PATH = 'pictographic-primitives/animals/sleep helper_a56ae08a-d50a-56ef-a0b7-9f3c918fa436.svg'
AUTHOR = 'gpt-6'

class SheepJumpingFence(Solo48):
    icon_id = 'sheep-jumping-fence'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('sheep', 'fence', 'jump', 'sleep', 'counting', 'insomnia', 'bedtime', 'rest')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_19_11 = (19, 11)
        p_29_11 = (29, 11)
        p_40_17 = (40, 17)
        p_35_28 = (35, 28)
        p_24_28 = (24, 28)
        p_17_23 = (17, 23)
        p_11_11 = (11, 11)
        p_11_23 = (11, 23)
        p_11_28 = (11, 28)
        p_40_32 = (40, 32)
        p_20_40 = (20, 40)
        p_20_42 = (20, 42)
        p_33_40 = (33, 40)
        p_33_42 = (33, 42)
        p_33_41 = (33, 41)
        p_10_42 = (10, 42)
        p_42_42 = (42, 42)
        self.add_arc('wool-top', p_19_11, p_29_11, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('wool-shoulder', p_29_11, p_40_17, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('wool-rump', p_40_17, p_35_28, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('wool-base', p_35_28, p_24_28, radius_x=5, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('wool-left', p_24_28, p_17_23, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('wool-neck', p_17_23, p_19_11)
        self.add_line('head-top', p_19_11, p_11_11)
        self.add_arc('muzzle', p_11_11, p_11_23, radius_x=5, radius_y=6, sweep=False, large_arc=False)
        self.add_line('jaw', p_11_23, p_17_23)
        self.add_line('front-hoof', p_17_23, p_11_28)
        self.add_line('rear-hoof', p_35_28, p_40_32)
        self.add_line('post-l', p_20_40, p_20_42)
        self.add_line('post-r', p_33_40, p_33_42)
        self.add_line('rail', p_20_40, p_33_41)
        self.add_line('ground-l', p_10_42, p_20_42)
        self.add_line('ground-r', p_33_42, p_42_42)
        self.add_contour('fleece', 'wool-top', 'wool-shoulder', 'wool-rump', 'wool-base', 'wool-left', 'wool-neck', closed=True)
        self.add_contour('head', 'head-top', 'muzzle', 'jaw', closed=False)
        self.relate('connect', 'fleece', 'head')
        self.relate('connect', 'fleece', 'front-hoof')
        self.relate('connect', 'fleece', 'rear-hoof')
        self.relate('connect', 'head', 'front-hoof')
        self.relate('connect', 'post-l', 'ground-l')
        self.relate('connect', 'post-r', 'ground-r')
