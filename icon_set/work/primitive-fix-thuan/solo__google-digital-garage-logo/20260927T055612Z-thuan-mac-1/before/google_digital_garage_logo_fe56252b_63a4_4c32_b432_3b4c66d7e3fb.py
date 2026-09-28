"""Three stacked bands, each folded at the centre like an open book seen from the front, rising slightly toward a middle crease.

Plan: Three equal folded strokes, mirrored about x=24; row step 12.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: layers: shared repeated chevrons.
Simplification: Outlined band thickness and crease seams reduce to three folded strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe56252b-63a4-4c32-b432-3b4c66d7e3fb'
SOURCE_PATH = 'pictographic-primitives/logos/google digital garage logo_fe56252b-63a4-4c32-b432-3b4c66d7e3fb.svg'
AUTHOR = 'gpt-6'


class GoogleDigitalGarageLogo(Solo48):
    icon_id = 'google-digital-garage-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-digital-garage', 'google', 'learning', 'logo', 'brand', 'training', 'stack')

    def build(self):
        axis=24
        for i,y in enumerate((8,20,32)):
            self.add_polyline(f'fold-{i}',(4,y+8),(axis,y),(2*axis-4,y+8))
