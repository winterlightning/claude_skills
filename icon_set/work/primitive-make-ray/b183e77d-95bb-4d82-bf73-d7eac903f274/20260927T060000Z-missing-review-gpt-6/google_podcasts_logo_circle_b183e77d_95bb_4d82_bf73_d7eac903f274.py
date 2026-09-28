"""A large circle holds a symmetrical audio waveform of vertical bars, tallest at the centre and shortening toward both sides.

Plan: Circular badge radius 20; three mirrored waveform bars on 9-unit pitch.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: audio-lines: repeated vertical strokes.
Simplification: Seven fine waveform strokes reduce to three.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b183e77d-95bb-4d82-bf73-d7eac903f274'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-podcasts-logo-circle/20260927T055654Z-thuan-mac-1/reference/google podcast logo 1_b183e77d-95bb-4d82-bf73-d7eac903f274.svg'
AUTHOR = "gpt-6"


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
        for i,half in enumerate((5,11,5)):
            x=15+9*i
            self.add_line(f'bar-{i}',(x,24-half),(x,24+half))
