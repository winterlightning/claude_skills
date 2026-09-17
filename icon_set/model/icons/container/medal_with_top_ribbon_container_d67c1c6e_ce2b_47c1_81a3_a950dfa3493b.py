"""Round Achievement Medal: independently authored container.

Construction plan: Circular medal below a triangular folded neck ribbon; shared horizontal axis, no award glyph.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/rewards/medal_d67c1c6e-ce2b-47c1-81a3-a950dfa3493b.svg. Lucide trophy original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'd67c1c6e-ce2b-47c1-81a3-a950dfa3493b'
SOURCE_PATH = 'pictographic-primitives/rewards/medal_d67c1c6e-ce2b-47c1-81a3-a950dfa3493b.svg'
AUTHOR = 'gpt-6'


class MedalWithTopRibbonContainer(Container64):
    icon_id = 'medal-with-top-ribbon-container'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('medal', 'with', 'top', 'ribbon', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        ellipse(self,'medal',32,42,20)
        poly('ribbon',(20,26),(10,2),(54,2),(44,26));join('ribbon','medal')
