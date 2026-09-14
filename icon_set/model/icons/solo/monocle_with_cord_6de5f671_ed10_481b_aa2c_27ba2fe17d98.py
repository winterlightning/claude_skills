'Monocle with cord.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6de5f671-ed10-481b-aa2c-27ba2fe17d98'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/glasses monocle_6de5f671-ed10-481b-aa2c-27ba2fe17d98.svg'
AUTHOR = 'gpt-6'

class MonocleWithCord(Solo48):
    icon_id = 'monocle-with-cord'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('monocle', 'glasses', 'lens', 'eyeglass', 'cord', 'vintage', 'eyewear', 'accessory')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_18_6 = (18, 6)
        p_30_18 = (30, 18)
        p_18_30 = (18, 30)
        p_30_35 = (30, 35)
        p_42_35 = (42, 35)
        p_42_22 = (42, 22)
        self.add_arc('lens-tr', p_18_6, p_30_18, radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('lens-br', p_30_18, p_18_30, radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('lens-left', p_18_30, p_18_6, radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_line('cord-down', p_30_18, p_30_35)
        self.add_arc('cord-bottom', p_30_35, p_42_35, radius_x=6, radius_y=7, sweep=False, large_arc=False)
        self.add_line('cord-up', p_42_35, p_42_22)
        self.add_contour('lens', 'lens-tr', 'lens-br', 'lens-left', closed=True)
        self.add_contour('cord', 'cord-down', 'cord-bottom', 'cord-up', closed=False)
        self.relate('connect', 'cord', 'lens')
