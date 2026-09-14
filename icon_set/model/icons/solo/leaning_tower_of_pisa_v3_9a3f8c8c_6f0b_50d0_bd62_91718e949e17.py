# Variant of leaning-tower-of-pisa; parent file remains unchanged.
'Leaning Tower of Pisa outline with all internal floor bands removed as requested; retained lean and ground.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a3f8c8c-6f0b-50d0-bd62-91718e949e17'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/pisa tower_9a3f8c8c-6f0b-50d0-bd62-91718e949e17.svg'
AUTHOR = 'gpt-6'

class LeaningTowerOfPisaVariant3(Solo48):
    icon_id = 'leaning-tower-of-pisa-v3'
    variant_of = 'leaning-tower-of-pisa'
    variant_label = 'Remove interior floor lines'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('pisa', 'tower', 'italy', 'leaning', 'landmark', 'campanile', 'travel', 'architecture')

    def build(self) -> None:
        self.add_polyline('shaft', (11, 42), (13, 36), (15, 26), (17, 16), (19, 6), (35, 6), (33, 20), (31, 30), (29, 40), (28, 42), (11, 42), closed=True)
        self.add_polyline('ground', (6, 42), (11, 42), (28, 42), (42, 42))
        self.relate('connect', 'ground', 'shaft')
