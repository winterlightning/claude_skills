'Kitchen Knife Block.\n\nSymbol plan: Curved knife block and two parallel exposed knife handles reduced to single strokes; block grain omitted.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00074a61-3ed9-40d1-8059-4735820ac11b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/knives set_00074a61-3ed9-40d1-8059-4735820ac11b.svg'
AUTHOR = 'gpt-6'

class KnifeBlockTwoKnives(Solo48):
    icon_id = 'knife-block-two-knives'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('knife', 'block', 'two', 'knives')

    def build(self):
        # Curved knife block and two parallel exposed knife handles reduced to single strokes; block grain omitted.
        axis_x = 24
        p_6_24 = (6, 24)
        p_6_42 = (6, 42)
        p_11_25 = (11, 25)
        p_16_24 = (16, 24)
        p_22_34 = (22, 34)
        p_24_32 = (24, 32)
        p_24_42 = (24, 42)
        p_27_6 = (27, 6)
        p_42_15 = (42, 15)
        self.add_line('block-1', p_6_42, p_6_24)
        self.add_bezier('block-2', p_6_24, (p_16_24, p_24_32, p_24_42))
        self.add_line('block-3', p_24_42, p_6_42)
        self.add_contour('block', 'block-1', 'block-2', 'block-3', closed=True)
        self.add_line('knife-left-1', p_11_25, p_27_6)
        self.add_contour('knife-left', 'knife-left-1', closed=False)
        self.relate("connect", 'block', 'knife-left')
        self.add_line('knife-right-1', p_22_34, p_42_15)
        self.add_contour('knife-right', 'knife-right-1', closed=False)
        self.relate("connect", 'block', 'knife-right')
