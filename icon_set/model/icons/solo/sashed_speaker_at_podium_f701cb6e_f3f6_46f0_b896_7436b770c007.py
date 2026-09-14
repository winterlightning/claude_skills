"""Frontal sashed speaker behind a lectern. VRECT_XL extremes 8,4–40,44. Lucide user-round circular head and mirrored shoulder arcs; reduce sash to diagonal band edge."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f701cb6e-f3f6-46f0-b896-7436b770c007'
SOURCE_PATH = 'pictographic-primitives/social/election politician podium man_f701cb6e-f3f6-46f0-b896-7436b770c007.svg'
AUTHOR = 'gpt-6'

class SashedSpeakerAtPodium(Solo48):
    icon_id = 'sashed-speaker-at-podium'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/social"
    aliases = ()
    keywords = ('person', 'speaker', 'podium', 'sash', 'politician', 'election')

    def build(self):
        self.add_arc('head-top', (19,9), (29,9), radius_x=5)
        self.add_arc('head-bottom', (29,9), (19,9), radius_x=5)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulder-left', (12,34), (20,23), radius_x=8, radius_y=11)
        self.add_line('shoulder-top', (20,23), (28,23))
        self.add_arc('shoulder-right', (28,23), (36,34), radius_x=8, radius_y=11)
        self.add_contour('body', 'shoulder-left', 'shoulder-top', 'shoulder-right')
        self.add_polyline('podium', (8,44), (8,34), (12,34), (36,34), (40,34), (40,44))
        self.add_line('sash', (28,23), (16,34))
        self.relate('connect', 'body','podium')
        self.relate('connect','body','sash')
        self.relate('connect','sash','podium')
