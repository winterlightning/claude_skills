'Magic Wand with Sparkles.\n\nSymbol plan: Diagonal magic wand and two sparkle crosses; reduce three tiny four-point sparkles to two.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: wand-sparkles.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95a90bce-b096-4222-b188-44abc2788637'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/wand sparkles_95a90bce-b096-4222-b188-44abc2788637.svg'
AUTHOR = 'gpt-6'

class SparklingMagicWand(Solo48):
    icon_id = 'sparkling-magic-wand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('sparkling', 'magic', 'wand')

    def build(self):
        # Diagonal magic wand and two sparkle crosses; reduce three tiny four-point sparkles to two.
        axis_x = 24
        p_6_42 = (6, 42)
        p_13_10 = (13, 10)
        p_17_6 = (17, 6)
        p_17_14 = (17, 14)
        p_21_10 = (21, 10)
        p_33_15 = (33, 15)
        p_34_33 = (34, 33)
        p_38_29 = (38, 29)
        p_38_37 = (38, 37)
        p_42_33 = (42, 33)
        self.add_line('wand-1', p_6_42, p_33_15)
        self.add_contour('wand', 'wand-1', closed=False)
        self.add_line('sparkle-top-v-1', p_17_6, p_17_14)
        self.add_contour('sparkle-top-v', 'sparkle-top-v-1', closed=False)
        self.add_line('sparkle-top-h-1', p_13_10, p_21_10)
        self.add_contour('sparkle-top-h', 'sparkle-top-h-1', closed=False)
        self.relate("connect", 'sparkle-top-v', 'sparkle-top-h')
        self.add_line('sparkle-right-v-1', p_38_29, p_38_37)
        self.add_contour('sparkle-right-v', 'sparkle-right-v-1', closed=False)
        self.add_line('sparkle-right-h-1', p_34_33, p_42_33)
        self.add_contour('sparkle-right-h', 'sparkle-right-h-1', closed=False)
        self.relate("connect", 'sparkle-right-v', 'sparkle-right-h')
