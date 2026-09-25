'Open umbrella with scalloped canopy.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05df3587-30f8-46af-94fa-4633b7974c08'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/umbrella_05df3587-30f8-46af-94fa-4633b7974c08.svg'
AUTHOR = 'gpt-6'

class OpenUmbrellaWithScallopedCanopy(Solo48):
    icon_id = 'open-umbrella-with-scalloped-canopy'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('accessories', 'state')
    aliases = ()
    keywords = ('open', 'umbrella', 'with', 'scalloped', 'canopy')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_26 = (6, 26)
        p_24_9 = (24, 9)
        p_42_26 = (42, 26)
        p_31_26 = (31, 26)
        p_24_22 = (24, 22)
        p_17_26 = (17, 26)
        p_24_6 = (24, 6)
        p_24_37 = (24, 37)
        p_14_37 = (14, 37)
        p_14_35 = (14, 35)
        self.add_arc('dome-left', p_6_26, p_24_9, radius_x=18, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('dome-right', p_24_9, p_42_26, radius_x=18, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('scallop-right', p_42_26, p_31_26, radius_x=6, radius_y=3, sweep=False, large_arc=False)
        self.add_arc('scallop-middle-right', p_31_26, p_24_22, radius_x=7, radius_y=4, sweep=False, large_arc=False)
        self.add_arc('scallop-middle-left', p_24_22, p_17_26, radius_x=7, radius_y=4, sweep=False, large_arc=False)
        self.add_arc('scallop-left', p_17_26, p_6_26, radius_x=6, radius_y=3, sweep=False, large_arc=False)
        self.add_line('finial', p_24_6, p_24_9)
        self.add_line('shaft', p_24_22, p_24_37)
        self.add_arc('hook', p_24_37, p_14_37, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('hook-tip', p_14_37, p_14_35)
        self.add_contour('canopy', 'dome-left', 'dome-right', 'scallop-right', 'scallop-middle-right', 'scallop-middle-left', 'scallop-left', closed=True)
        self.add_contour('handle', 'shaft', 'hook', 'hook-tip', closed=False)
        self.relate('connect', 'canopy', 'finial')
        self.relate('connect', 'canopy', 'handle')
