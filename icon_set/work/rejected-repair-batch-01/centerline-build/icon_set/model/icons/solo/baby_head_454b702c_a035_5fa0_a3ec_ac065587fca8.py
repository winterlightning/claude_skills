"""Add two evenly spaced dot eyes to the baby face. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '454b702c-a035-5fa0-a3ec-ac065587fca8'
SOURCE_PATH = 'pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'
AUTHOR = 'gpt-6'

class BabyHead(Solo48):
    icon_id = 'baby-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('baby', 'head', 'infant', 'nursery')

    def build(self) -> None:
        """Symbol plan: Add two evenly spaced dot eyes to the baby face. Reference: Lucide baby: paired dot eyes; shared human reference for face proportions."""
        p_11_20 = (11, 20)
        p_24_10 = (24, 10)
        p_32_10 = (32, 10)
        p_24_17 = (24, 17)
        p_31_13 = (31, 13)
        p_37_20 = (37, 20)
        p_39_25 = (39, 25)
        p_39_30 = (39, 30)
        p_35_37 = (35, 37)
        p_13_37 = (13, 37)
        p_9_30 = (9, 30)
        p_9_25 = (9, 25)
        p_6_42 = (6, 42)
        p_42_42 = (42, 42)
        self.add_arc('crown-left', p_11_20, p_24_10, radius_x=13, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('curl-up', p_24_10, p_32_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('curl-down', p_32_10, p_24_17, radius_x=8, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('crown-right', p_31_13, p_37_20, radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('upper-cheek-right', p_37_20, p_39_25, radius_x=11, radius_y=11, sweep=True, large_arc=False)
        self.add_arc('ear-right', p_39_25, p_39_30, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('jaw-right', p_39_30, p_35_37, radius_x=15, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('jaw-bottom', p_35_37, p_13_37, radius_x=11, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('jaw-left', p_13_37, p_9_30, radius_x=15, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('ear-left', p_9_30, p_9_25, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('upper-cheek-left', p_9_25, p_11_20, radius_x=11, radius_y=11, sweep=True, large_arc=False)
        self.add_arc('shoulder-left', p_13_37, p_6_42, radius_x=9, radius_y=9, sweep=False, large_arc=False)
        self.add_arc('shoulder-right', p_42_42, p_35_37, radius_x=9, radius_y=9, sweep=False, large_arc=False)
        self.add_contour('face', 'crown-right', 'upper-cheek-right', 'ear-right', 'jaw-right', 'jaw-bottom', 'jaw-left', 'ear-left', 'upper-cheek-left', 'crown-left', 'curl-up', 'curl-down', closed=False)
        self.relate('connect', 'face', 'shoulder-left')
        self.relate('connect', 'face', 'shoulder-right')
        self.add_dot('eye-left', (18, 26))
        self.add_dot('eye-right', (30, 26))
