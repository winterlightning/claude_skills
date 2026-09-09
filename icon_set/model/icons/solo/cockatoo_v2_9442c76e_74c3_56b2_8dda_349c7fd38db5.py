# Variant of cockatoo; parent file remains unchanged.
'Cockatoo head portrait with swept crest and a large hooked parrot beak. Wing and tail omitted to enlarge the requested head; Lucide bird informs the rounded crown and dot eye.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9442c76e-74c3-56b2-8dda-349c7fd38db5'
SOURCE_PATH = 'pictographic-primitives/animals/parrot_9442c76e-74c3-56b2-8dda-349c7fd38db5.svg'
AUTHOR = 'gpt-6'

class CockatooVariant2(Solo48):
    icon_id = 'cockatoo-v2'
    variant_of = 'cockatoo'
    variant_label = 'Clear crested parrot head'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('cockatoo',)

    def build(self) -> None:
        # VRECT_XL centerline extremes (5,2)-(43,46). Enlarged head portrait.
        self.add_arc('nape', (5,46), (10,19), radius_x=5, radius_y=27)
        self.add_line('crest-back', (10,19), (5,2))
        self.add_arc('crest-top', (5,2), (23,10), radius_x=18, radius_y=8)
        self.add_arc('crown', (23,10), (35,22), radius_x=12)
        self.add_arc('beak-top', (35,22), (43,30), radius_x=8)
        self.add_arc('beak-hook', (43,30), (35,38), radius_x=8)
        self.add_line('beak-inner', (35,38), (35,30))
        self.add_arc('chin', (35,30), (23,42), radius_x=12)
        self.add_line('neck', (23,42), (23,46))
        self.add_contour('outline', 'nape','crest-back','crest-top','crown','beak-top','beak-hook','beak-inner','chin','neck')
        self.add_dot('eye', (24,23))
