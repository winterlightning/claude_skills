'Simple open umbrella.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb6872fb-7ad7-4948-9e90-e03cf896cf9a'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/umbrella_bb6872fb-7ad7-4948-9e90-e03cf896cf9a.svg'
AUTHOR = 'gpt-6'

class SimpleOpenUmbrella(Solo48):
    icon_id = 'simple-open-umbrella'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('umbrella', 'rain', 'parasol', 'weather', 'canopy', 'handle', 'shelter', 'accessory')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_26 = (8, 26)
        p_24_9 = (24, 9)
        p_40_26 = (40, 26)
        p_24_26 = (24, 26)
        p_24_4 = (24, 4)
        p_24_39 = (24, 39)
        p_14_39 = (14, 39)
        self.add_arc('canopy-l', p_8_26, p_24_9, radius_x=16, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('canopy-r', p_24_9, p_40_26, radius_x=16, radius_y=17, sweep=True, large_arc=False)
        self.add_line('edge-1', p_40_26, p_24_26)
        self.add_line('edge-2', p_24_26, p_8_26)
        self.add_line('finial', p_24_4, p_24_9)
        self.add_line('shaft', p_24_26, p_24_39)
        self.add_arc('hook', p_24_39, p_14_39, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('canopy', 'canopy-l', 'canopy-r', 'edge-1', 'edge-2', closed=True)
        self.add_contour('handle', 'shaft', 'hook', closed=False)
        self.relate('connect', 'finial', 'canopy')
        self.relate('connect', 'handle', 'canopy')
