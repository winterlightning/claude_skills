# Variant of leaning-tower-of-pisa; parent file remains unchanged.
'Leaning tower reduced to two floor bands. VRECT_XL preserves its rightward lean and ground line. Lucide landmark informs sparse structural detail.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a3f8c8c-6f0b-50d0-bd62-91718e949e17'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/pisa tower_9a3f8c8c-6f0b-50d0-bd62-91718e949e17.svg'
AUTHOR = 'gpt-6'

class LeaningTowerOfPisaVariant2(Solo48):
    icon_id = 'leaning-tower-of-pisa-v2'
    variant_of = 'leaning-tower-of-pisa'
    variant_label = 'Fewer floor bands'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('pisa', 'tower', 'italy', 'leaning', 'landmark', 'campanile', 'travel', 'architecture')

    def build(self) -> None:
        # VRECT_XL extremes (5,2)-(43,46); intentional rightward lean.
        self.add_polyline('shaft',(11,46),(14,31),(17,16),(19,2),(35,6),(33,20),(30,35),(28,46),(11,46),closed=True)
        self.add_line('upper-floor',(17,16),(33,20))
        self.add_line('lower-floor',(14,31),(30,35))
        self.relate('connect','upper-floor','shaft')
        self.relate('connect','lower-floor','shaft')
        self.add_polyline('ground',(5,46),(11,46),(28,46),(43,46))
        self.relate('connect','ground','shaft')
