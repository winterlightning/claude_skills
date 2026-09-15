"""Three horizontal capsules stagger down the canvas: one at the upper right, a longer one at the left ending in a round cap, and one at the lower right.

Plan: Three staggered horizontal bars; shared 16-unit row pitch.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful exact brand match; shared bar construction.
Simplification: Capsule outlines become rounded strokes; middle cap seam omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae83bf52-94cf-4649-96cd-9fa9840a8ca6'
SOURCE_PATH = 'pictographic-primitives/logos/google studio logo_ae83bf52-94cf-4649-96cd-9fa9840a8ca6.svg'
AUTHOR = 'gpt-6'


class GoogleDataStudioLogo(Solo48):
    icon_id = 'google-data-studio-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-data-studio', 'looker-studio', 'google', 'reports', 'logo', 'brand', 'data')

    def build(self):
        for i,(left,right,y) in enumerate(((20,44,8),(4,30,24),(20,44,40))):
            self.add_line(f'bar-{i}',(left,y),(right,y))
