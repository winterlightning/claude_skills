"""Mirror an outlined X about x=24; preserve four broad terminals and the pinched waist."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5c47af8-333c-45af-9c23-fe2b97c5c953'
SOURCE_PATH = 'pictographic-primitives/logos/osx logo_e5c47af8-333c-45af-9c23-fe2b97c5c953.svg'
AUTHOR = 'gpt-6'

class MacosXLogo(Solo48):
    icon_id = 'macos-x-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('osx', 'macos', 'apple', 'letter-x', 'logo', 'brand', 'operating-system')

    def build(self):
        # Plan: Mirror an outlined X about x=24; preserve four broad terminals and the pinched waist.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('x',(6,6),(16,6),(24,18),(32,6),(42,6),(30,24),(42,42),(32,42),(24,30),(16,42),(6,42),(18,24),closed=True)

