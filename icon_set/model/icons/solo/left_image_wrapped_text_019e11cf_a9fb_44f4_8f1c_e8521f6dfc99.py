'Image Left Text Wrap.\n\nSymbol plan: Image placeholder with abstract text rules; reduce short rules from three to two. No literal text or typeface glyphs.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '019e11cf-a9fb-44f4-8f1c-e8521f6dfc99'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/text image left 1_019e11cf-a9fb-44f4-8f1c-e8521f6dfc99.svg'
AUTHOR = 'gpt-6'

class LeftImageWrappedText(Solo48):
    icon_id = 'left-image-wrapped-text'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('left', 'image', 'wrapped', 'text')

    def build(self):
        # Image placeholder with abstract text rules; reduce short rules from three to two. No literal text or typeface glyphs.
        axis_x = 24
        p_6_19 = (6, 19)
        p_6_29 = (6, 29)
        p_9_16 = (9, 16)
        p_9_32 = (9, 32)
        p_21_16 = (21, 16)
        p_21_32 = (21, 32)
        p_22_6 = (22, 6)
        p_22_42 = (22, 42)
        p_24_19 = (24, 19)
        p_24_29 = (24, 29)
        p_33_19 = (33, 19)
        p_33_29 = (33, 29)
        p_42_6 = (42, 6)
        p_42_19 = (2 * axis_x - p_6_19[0], p_6_19[1])
        p_42_29 = (2 * axis_x - p_6_29[0], p_6_29[1])
        p_42_42 = (42, 42)
        self.add_line('image-1', p_9_16, p_21_16)
        self.add_arc('image-2', p_21_16, p_24_19, radius_x=3, radius_y=3, sweep=True)
        self.add_line('image-3', p_24_19, p_24_29)
        self.add_arc('image-4', p_24_29, p_21_32, radius_x=3, radius_y=3, sweep=True)
        self.add_line('image-5', p_21_32, p_9_32)
        self.add_arc('image-6', p_9_32, p_6_29, radius_x=3, radius_y=3, sweep=True)
        self.add_line('image-7', p_6_29, p_6_19)
        self.add_arc('image-8', p_6_19, p_9_16, radius_x=3, radius_y=3, sweep=True)
        self.add_contour('image', 'image-1', 'image-2', 'image-3', 'image-4', 'image-5', 'image-6', 'image-7', 'image-8', closed=True)
        self.add_line('top-1', p_22_6, p_42_6)
        self.add_contour('top', 'top-1', closed=False)
        self.add_line('bottom-1', p_22_42, p_42_42)
        self.add_contour('bottom', 'bottom-1', closed=False)
        self.add_line('short-top-1', p_33_19, p_42_19)
        self.add_contour('short-top', 'short-top-1', closed=False)
        self.add_line('short-bottom-1', p_33_29, p_42_29)
        self.add_contour('short-bottom', 'short-bottom-1', closed=False)
