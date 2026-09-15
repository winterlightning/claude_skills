"""glass-blowing: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fef50d84-6d4d-401d-81a7-a9ae8775c6dd'
SOURCE_PATH = 'pictographic-primitives/hobbies/glass blowing_fef50d84-6d4d-401d-81a7-a9ae8775c6dd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class GlassBlowing(Solo48):
    icon_id = 'glass-blowing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('glass', 'blowing', 'hobbies')

    def build(self):
        # SQUARE (6,6)-(42,42); smooth glass bulb and shared diagonal neck attachment.
        # Construction reference: Lucide cloud: coherent rounded lobes; source supplies blowpipe and bulb
        self.add_line('pipe',(6,42),(18,30))
        self.add_bezier('left-neck',(18,30),((14,28),(16,25),(16,22)))
        self.add_bezier('bulb',(16,22),((16,13),(22,6),(30,6)),((37,6),(42,11),(42,18)),((42,26),(35,32),(26,32)))
        self.add_bezier('right-neck',(26,32),((23,32),(20,34),(18,30)))
        self.add_contour('glass','left-neck','bulb','right-neck',closed=True)
        self.relate('connect','pipe','glass')
