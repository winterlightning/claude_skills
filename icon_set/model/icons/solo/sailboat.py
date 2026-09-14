'Sailboat.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/sailboat.py'
AUTHOR = 'gpt-6'

class Sailboat(Solo48):
    icon_id = 'sailboat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transport'
    aliases = ('sailing-boat', 'sailing-boat-with-single-sail')
    keywords = ('boat', 'sailboat', 'sail', 'sailing', 'ship', 'nautical', 'travel', 'sea')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_24_6 = (24, 6)
        p_38_24 = (38, 24)
        p_24_24 = (24, 24)
        p_24_32 = (24, 32)
        p_6_32 = (6, 32)
        p_42_32 = (42, 32)
        p_34_42 = (34, 42)
        p_14_42 = (14, 42)
        self.add_arc('sail-leech', p_24_6, p_38_24, radius_x=23, radius_y=23, sweep=True, large_arc=False)
        self.add_line('sail-foot', p_38_24, p_24_24)
        self.add_line('sail-luff', p_24_24, p_24_6)
        self.add_line('mast', p_24_24, p_24_32)
        self.add_line('gunwale-left', p_6_32, p_24_32)
        self.add_line('gunwale-right', p_24_32, p_42_32)
        self.add_arc('hull-starboard', p_42_32, p_34_42, radius_x=8, radius_y=10, sweep=True, large_arc=False)
        self.add_line('hull-keel', p_34_42, p_14_42)
        self.add_arc('hull-port', p_14_42, p_6_32, radius_x=8, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('sail', 'sail-leech', 'sail-foot', 'sail-luff', closed=True)
        self.add_contour('hull', 'gunwale-left', 'gunwale-right', 'hull-starboard', 'hull-keel', 'hull-port', closed=True)
        self.relate('connect', 'sail', 'mast')
        self.relate('connect', 'mast', 'hull')
