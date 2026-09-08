"""A two-lobed speech cloud with a downward-left tail. Unequal lobes follow the reference.

Keyshape HRECT_XL; visible bounds (0, 4, 64, 60); centerline extremes (2, 6)-(62, 58).
Construction reference: Lucide cloud: large left lobe and smaller right lobe, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class CloudSpeechBubble(Container64):
    icon_id = 'cloud-speech-bubble'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('cloud-shaped-speech-bubble',)
    keywords = ('cloud', 'speech', 'bubble')

    def build(self) -> None:
        # HRECT_XL centerline (2,6)-(62,58): broad cloud plus pointed tail.
        self.add_arc("large-nw", (2,26), (22,6), radius_x=20)
        self.add_arc("large-ne", (22,6), (42,22), radius_x=20, radius_y=16)
        self.add_arc("small-shoulder", (42,22), (48,20), radius_x=10)
        self.add_arc("small-ne", (48,20), (62,33), radius_x=14, radius_y=13)
        self.add_arc("small-se", (62,33), (48,46), radius_x=14, radius_y=13)
        self.add_line("floor", (48,46), (38,46))
        self.add_line("tail-out", (38,46), (24,58))
        self.add_line("tail-in", (24,58), (24,46))
        self.add_line("floor-left", (24,46), (22,46))
        self.add_arc("large-sw", (22,46), (2,26), radius_x=20)
        self.add_contour("outline", "large-nw", "large-ne", "small-shoulder", "small-ne", "small-se", "floor", "tail-out", "tail-in", "floor-left", "large-sw", closed=True)
