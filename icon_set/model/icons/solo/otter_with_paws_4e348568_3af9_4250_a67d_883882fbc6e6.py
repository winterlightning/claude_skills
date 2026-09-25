'Otter with paws.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e348568-3af9-4250-a67d-883882fbc6e6'
SOURCE_PATH = 'pictographic-primitives/animals/otter_4e348568-3af9-4250-a67d-883882fbc6e6.svg'
AUTHOR = 'gpt-6'

class OtterWithPaws(Solo48):
    icon_id = 'otter-with-paws'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('otter', 'with', 'paws')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_12 = (8, 12)
        p_20_12 = (20, 12)
        p_28_12 = (28, 12)
        p_40_12 = (40, 12)
        p_40_22 = (40, 22)
        p_35_28 = (35, 28)
        p_13_28 = (13, 28)
        p_8_22 = (8, 22)
        p_6_35 = (6, 35)
        p_20_35 = (20, 35)
        p_28_35 = (28, 35)
        p_42_35 = (42, 35)
        p_17_20 = (17, 20)
        p_31_20 = (31, 20)
        p_24_24 = (24, 24)
        self.add_arc('ear-left', p_8_12, p_20_12, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('crown', p_20_12, p_28_12)
        self.add_arc('ear-right', p_28_12, p_40_12, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('side-right', p_40_12, p_40_22)
        self.add_arc('cheek-right', p_40_22, p_35_28, radius_x=5, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('cheek-left', p_13_28, p_8_22, radius_x=5, radius_y=6, sweep=True, large_arc=False)
        self.add_line('side-left', p_8_22, p_8_12)
        self.add_arc('paw-left-top', p_6_35, p_20_35, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('paw-left-bottom', p_20_35, p_6_35, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('paw-right-top', p_28_35, p_42_35, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('paw-right-bottom', p_42_35, p_28_35, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('eye-left', p_17_20, p_17_20)
        self.add_line('eye-right', p_31_20, p_31_20)
        self.add_line('nose', p_24_24, p_24_24)
        self.add_contour('head', 'cheek-left', 'side-left', 'ear-left', 'crown', 'ear-right', 'side-right', 'cheek-right', closed=False)
        self.add_contour('paw-left', 'paw-left-top', 'paw-left-bottom', closed=True)
        self.add_contour('paw-right', 'paw-right-top', 'paw-right-bottom', closed=True)
        self.relate('connect', 'head', 'paw-left')
        self.relate('connect', 'head', 'paw-right')
