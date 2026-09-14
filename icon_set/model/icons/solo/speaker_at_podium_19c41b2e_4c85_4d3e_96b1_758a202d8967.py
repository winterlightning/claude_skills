"""Speaker behind podium with bent microphone on the left. SQUARE extremes 6,6–42,42. Lucide user-round head and shoulders; microphone reduced to stem and angled head; offset speaker preserves space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19c41b2e-4c85-4d3e-96b1-758a202d8967'
SOURCE_PATH = 'pictographic-primitives/social/election speech 1_19c41b2e-4c85-4d3e-96b1-758a202d8967.svg'
AUTHOR = 'gpt-6'

class SpeakerAtPodium(Solo48):
    icon_id = 'speaker-at-podium'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/social"
    aliases = ()
    keywords = ('speaker', 'podium', 'microphone', 'speech', 'person', 'address')

    def build(self):
        self.add_arc('head-top', (22,11), (32,11), radius_x=5)
        self.add_arc('head-bottom', (32,11), (22,11), radius_x=5)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulders', (16,32), (38,32), radius_x=11, radius_y=7)
        self.add_polyline('podium', (8,42), (6,32), (42,32), (40,42))
        self.add_polyline('microphone', (10,32), (6,21), (12,15))
        self.relate('connect','shoulders','podium')
        self.relate('connect','microphone','podium')
