"""A two-lobed speech cloud with a downward-left tail. Unequal lobes follow the reference.

Keyshape HRECT_XL; visible bounds (0, 4, 64, 60); centerline extremes (2, 6)-(62, 58).
Construction reference: Lucide cloud: large left lobe and smaller right lobe, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (cloud-speech-bubble HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class CloudSpeechBubble(Container64):
    icon_id = 'cloud-speech-bubble'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('cloud-shaped-speech-bubble',)
    keywords = ('cloud', 'speech', 'bubble')

    def build(self) -> None:
        self.add_arc('large-nw', (4, 28), (22, 10), radius_x=18)
        self.add_arc('large-ne', (22, 10), (41, 22), radius_x=19, radius_y=12)
        self.add_arc('small-shoulder', (41, 22), (47, 20), radius_x=10)
        self.add_arc('small-ne', (47, 20), (60, 33), radius_x=13)
        self.add_arc('small-se', (60, 33), (47, 46), radius_x=13)
        self.add_line('floor', (47, 46), (37, 46))
        self.add_line('tail-out', (37, 46), (25, 54))
        self.add_line('tail-in', (25, 54), (25, 46))
        self.add_line('floor-left', (25, 46), (22, 46))
        self.add_arc('large-sw', (22, 46), (4, 28), radius_x=18)
        self.add_contour('outline', 'large-nw', 'large-ne', 'small-shoulder', 'small-ne', 'small-se', 'floor', 'tail-out', 'tail-in', 'floor-left', 'large-sw', closed=True)
