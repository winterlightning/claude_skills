"""A symmetrical audio waveform of five thick rounded vertical bars, the tallest at the centre and the shortest at the outer edges.

Plan: Five mirrored waveform strokes; shared x pitch 10 and heights 4,16,32,16,4.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: audio-lines: repeated vertical strokes with shared spacing.
Simplification: Outlined capsules reduce to single rounded strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79ee2543-57a6-47b2-878d-4e073d7ac97a'
SOURCE_PATH = 'pictographic-primitives/logos/google podcast logo_79ee2543-57a6-47b2-878d-4e073d7ac97a.svg'
AUTHOR = 'gpt-6'


class GooglePodcastsLogo(Solo48):
    icon_id = 'google-podcasts-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-podcasts', 'podcast', 'audio', 'waveform', 'logo', 'brand', 'google')

    def build(self):
        for i,half in enumerate((2,8,16,8,2)):
            x=4+10*i
            self.add_line(f'bar-{i}',(x,24-half),(x,24+half))
