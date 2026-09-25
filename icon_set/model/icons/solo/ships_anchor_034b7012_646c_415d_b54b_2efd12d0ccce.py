'Ships anchor.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '034b7012-646c-415d-b54b-2efd12d0ccce'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-08/anchor_034b7012-646c-415d-b54b-2efd12d0ccce.svg'
AUTHOR = 'gpt-6'

class ShipsAnchor(Solo48):
    icon_id = 'ships-anchor'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    categories = ('landmarks', 'state')
    aliases = ('anchor', 'ship-anchor')
    keywords = ('ship', 'nautical', 'marine', 'harbour', 'port', 'sailing', 'sea', 'maritime')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_24_14 = (24, 14)
        p_24_6 = (24, 6)
        p_24_22 = (24, 22)
        p_24_42 = (24, 42)
        p_16_22 = (16, 22)
        p_32_22 = (32, 22)
        p_12_31 = (12, 31)
        p_6_26 = (6, 26)
        p_42_26 = (42, 26)
        p_36_31 = (36, 31)
        self.add_arc('ring-left', p_24_14, p_24_6, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('ring-right', p_24_6, p_24_14, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('shank-upper', p_24_14, p_24_22)
        self.add_line('shank-lower', p_24_22, p_24_42)
        self.add_line('stock-1', p_16_22, p_24_22)
        self.add_line('stock-2', p_24_22, p_32_22)
        self.add_line('fluke-left', p_12_31, p_6_26)
        self.add_arc('arm-left', p_6_26, p_24_42, radius_x=18, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('arm-right', p_24_42, p_42_26, radius_x=18, radius_y=16, sweep=False, large_arc=False)
        self.add_line('fluke-right', p_42_26, p_36_31)
        self.add_contour('ring', 'ring-left', 'ring-right', closed=True)
        self.add_contour('shank', 'shank-upper', 'shank-lower', closed=False)
        self.add_contour('stock', 'stock-1', 'stock-2', closed=False)
        self.add_contour('arms', 'fluke-left', 'arm-left', 'arm-right', 'fluke-right', closed=False)
        self.relate('connect', 'ring', 'shank')
        self.relate('connect', 'stock', 'shank')
        self.relate('connect', 'arms', 'shank')
