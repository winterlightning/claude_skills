"""Military Drone from Above. Symmetric overhead fuselage and tapered wings; tiny propeller marks omitted.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e69b65dc-1f55-4022-b7dd-ae536b0ce78f'
SOURCE_PATH = 'pictographic-primitives/war/military drone_e69b65dc-1f55-4022-b7dd-ae536b0ce78f.svg'
AUTHOR = 'gpt-6'

class MilitaryDroneOverheadVariant2(Solo48):
    icon_id = 'military-drone-overhead-v2'
    variant_of = 'military-drone-overhead'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('drone', 'aircraft', 'military', 'wing', 'propeller', 'overhead')

    def build(self) -> None:
        # Mirror the wing and tail geometry; nine-unit wing tips keep the thin wing slots open.
        right = [(24, 4), (28, 10), (28, 18), (40, 22), (40, 31), (28, 27), (28, 36), (34, 40), (24, 44)]
        left = [(48 - x, y) for x, y in reversed(right[1:-1])]
        self.add_polyline('airframe', *right + left, closed=True)
