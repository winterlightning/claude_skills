"""headphones-audio: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa'
SOURCE_PATH = 'pictographic-primitives/audio/headphones_2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class HeadphonesAudio(Solo48):
    icon_id = 'headphones-audio'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'state')
    aliases = ()
    keywords = ('headphones', 'audio')

    def build(self):
        # SQUARE (6,6)-(42,42); mirror cups around x=24, shared width and height.
        # Construction reference: Lucide headphones: semicircle headband and paired cups
        self.add_arc('headband',(6,24),(42,24),radius_x=18)
        self.add_line('left-side',(6,24),(6,42))
        self.add_line('right-side',(42,24),(42,42))
        self.add_contour('band','left-side')
        self.add_polyline('left-cup',(6,30),(14,30),(14,42),(6,42))
        self.add_polyline('right-cup',(42,30),(34,30),(34,42),(42,42))
        self.relate('connect','headband','left-side')
        self.relate('connect','headband','right-side')
        self.relate('connect','left-side','left-cup')
        self.relate('connect','right-side','right-cup')
