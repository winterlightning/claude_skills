"""A large circle holds a symmetrical audio waveform of vertical bars, tallest at the centre and shortening toward both sides.

Plan: Circular badge radius 20; three mirrored waveform bars on 9-unit pitch.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: audio-lines: repeated vertical strokes.
Simplification: Seven fine waveform strokes reduce to three.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b183e77d-95bb-4d82-bf73-d7eac903f274'
SOURCE_PATH = 'pictographic-primitives/logos/google podcast logo 1_b183e77d-95bb-4d82-bf73-d7eac903f274.svg'
AUTHOR = 'gpt-6'


class GooglePodcastsLogoCircle(Solo48):
    icon_id = 'google-podcasts-logo-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-podcasts', 'podcast', 'audio', 'waveform', 'logo', 'brand', 'google')

    def build(self):
        self.add_arc('top',(4,24),(44,24),radius_x=20)
        self.add_arc('bottom',(44,24),(4,24),radius_x=20)
        self.add_contour('circle','top','bottom',closed=True)
        for i,half in enumerate((4,11,4)):
            x=15+9*i
            self.add_line(f'bar-{i}',(x,24-half),(x,24+half))
