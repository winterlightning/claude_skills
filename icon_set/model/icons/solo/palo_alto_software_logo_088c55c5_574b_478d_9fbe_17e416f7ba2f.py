"""Two identical mirrored upward chevron strokes, spaced by one shared vertical step. Lucide chevrons-up informs coherent strokes; omit double outlines."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '088c55c5-574b-478d-9fbe-17e416f7ba2f'
SOURCE_PATH = 'pictographic-primitives/logos/palo alto software logo_088c55c5-574b-478d-9fbe-17e416f7ba2f.svg'
AUTHOR = 'gpt-6'

class PaloAltoSoftwareLogo(Solo48):
    icon_id = 'palo-alto-software-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('palo-alto-software', 'chevrons', 'up', 'logo', 'brand', 'business', 'planning')

    def build(self):
        # Plan: Two identical mirrored upward chevron strokes, spaced by one shared vertical step. Lucide chevrons-up informs coherent strokes; omit double outlines.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        axis=24
        for i,y in enumerate((6,24)):
            self.add_polyline('chevron-'+str(i),(6,y+18),(axis,y),(42,y+18))

