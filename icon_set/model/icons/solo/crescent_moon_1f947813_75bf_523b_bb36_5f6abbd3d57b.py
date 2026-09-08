"""Left-opening crescent. VRECT_L extremes (8,2)-(40,46). Lucide moon: paired coherent arcs; opening deliberately faces left."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f947813-75bf-523b-bb36-5f6abbd3d57b'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/astrology moon_1f947813-75bf-523b-bb36-5f6abbd3d57b.svg'
AUTHOR = 'astra-chatgpt'


class CrescentMoon(Solo48):
    icon_id = 'crescent-moon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('moon', 'crescent', 'lunar', 'night', 'astrology', 'symbol', 'sky', 'phase')

    def build(self) -> None:
        self.add_arc('outer', (8, 2), (8, 46), radius_x=32, radius_y=22, sweep=True)
        self.add_arc('inner', (8, 46), (8, 2), radius_x=17, radius_y=22, sweep=False)
        self.add_contour('crescent', 'outer', 'inner', closed=True)
