"""Symmetric diagonal X with four equal arms sharing the center. Reduce capsule outlines to round-ended crossing strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8bd78f24-b77d-4c8c-a30d-c966f70d1418'
SOURCE_PATH = 'pictographic-primitives/logos/x pack logo_8bd78f24-b77d-4c8c-a30d-c966f70d1418.svg'
AUTHOR = 'gpt-6'

class ElasticXPackLogo(Solo48):
    icon_id = 'elastic-x-pack-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('x-pack', 'elastic', 'letter-x', 'cross', 'logo', 'brand', 'security')

    def build(self):
        # Plan: Symmetric diagonal X with four equal arms sharing the center. Reduce capsule outlines to round-ended crossing strokes.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        for j,p in enumerate([(6,6),(42,6),(42,42),(6,42)]):self.add_line('arm-'+str(j),(24,24),p)
        for j in range(4):
            for k in range(j+1,4):self.relate('connect','arm-'+str(j),'arm-'+str(k))

