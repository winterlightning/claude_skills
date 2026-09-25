'Open umbrella with ribs.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82042441-8abf-5e1b-9607-fac33bc3b256'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/umbrella_82042441-8abf-5e1b-9607-fac33bc3b256.svg'
AUTHOR = 'gpt-6'

class OpenUmbrellaWithRibs(Solo48):
    icon_id = 'open-umbrella-with-ribs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('umbrella', 'rain', 'parasol', 'weather', 'canopy', 'rib', 'handle', 'shelter')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_24 = (6, 24)
        p_24_6 = (24, 6)
        p_42_24 = (42, 24)
        p_32_24 = (32, 24)
        p_24_22 = (24, 22)
        p_16_24 = (16, 24)
        p_24_37 = (24, 37)
        p_34_37 = (34, 37)
        p_34_34 = (34, 34)
        self.add_arc('canopy-l', p_6_24, p_24_6, radius_x=18, radius_y=18, sweep=True, large_arc=False)
        self.add_arc('canopy-r', p_24_6, p_42_24, radius_x=18, radius_y=18, sweep=True, large_arc=False)
        self.add_arc('scallop-r', p_42_24, p_32_24, radius_x=5, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('scallop-mid-r', p_32_24, p_24_22, radius_x=8, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('scallop-mid-l', p_24_22, p_16_24, radius_x=8, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('scallop-l', p_16_24, p_6_24, radius_x=5, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('rib-l', p_24_6, p_16_24, radius_x=8, radius_y=18, sweep=False, large_arc=False)
        self.add_arc('rib-r', p_24_6, p_32_24, radius_x=8, radius_y=18, sweep=True, large_arc=False)
        self.add_line('shaft', p_24_22, p_24_37)
        self.add_arc('hook', p_24_37, p_34_37, radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('hook-tip', p_34_37, p_34_34)
        self.add_contour('canopy', 'canopy-l', 'canopy-r', 'scallop-r', 'scallop-mid-r', 'scallop-mid-l', 'scallop-l', closed=True)
        self.add_contour('handle', 'shaft', 'hook', 'hook-tip', closed=False)
        self.relate('connect', 'rib-l', 'canopy')
        self.relate('connect', 'rib-r', 'canopy')
        self.relate('connect', 'rib-l', 'rib-r')
        self.relate('connect', 'handle', 'canopy')
