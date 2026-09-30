"""Round Achievement Medal: independently authored container.

Construction plan: Circular medal below a triangular folded neck ribbon; shared horizontal axis, no award glyph.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/rewards/medal_d67c1c6e-ce2b-47c1-81a3-a950dfa3493b.svg. Lucide trophy original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (medal-with-top-ribbon-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'd67c1c6e-ce2b-47c1-81a3-a950dfa3493b'
SOURCE_PATH = 'pictographic-primitives/rewards/medal_d67c1c6e-ce2b-47c1-81a3-a950dfa3493b.svg'
AUTHOR = 'claude-opus-5-5'


class MedalWithTopRibbonContainer(Container64):
    icon_id = 'medal-with-top-ribbon-container'
    keyshape = Keyshape.VRECT_M
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases = ()
    keywords = ('medal', 'with', 'top', 'ribbon', 'container')

    def build(self) -> None:
        self.add_arc('medal-0', (14, 42), (50, 42), radius_x=18)
        self.add_arc('medal-1', (50, 42), (14, 42), radius_x=18)
        self.add_line('ribbon-1', (22, 27), (12, 4))
        self.add_line('ribbon-2', (12, 4), (52, 4))
        self.add_line('ribbon-3', (52, 4), (42, 27))
        self.add_contour('medal', 'medal-0', 'medal-1', closed=True)
        self.add_contour('ribbon', 'ribbon-1', 'ribbon-2', 'ribbon-3')
        self.relate('connect', 'ribbon', 'medal')
