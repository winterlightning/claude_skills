'Cockatoo head portrait with swept crest and a large hooked parrot beak. Wing and tail omitted to enlarge the requested head; Lucide bird informs the rounded crown and dot eye.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9442c76e-74c3-56b2-8dda-349c7fd38db5'
SOURCE_PATH = 'pictographic-primitives/animals/parrot_9442c76e-74c3-56b2-8dda-349c7fd38db5.svg'
AUTHOR = 'gpt-6'

class Cockatoo(Solo48):
    icon_id = 'cockatoo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('cockatoo',)

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        # VRECT_XL centerline extremes (6,6)-(42,42). Enlarged head portrait.
        self.add_arc('nape', (8, 44), (10,19), radius_x=2, radius_y=25)
        self.add_line('crest-back', (10,19), (8, 4))
        self.add_arc('crest-top', (8, 4), (23,10), radius_x=15, radius_y=6)
        self.add_arc('crown', (23,10), (35,22), radius_x=12)
        self.add_arc('beak-top', (35,22), (40, 30), radius_x=5, radius_y=8)
        self.add_arc('beak-hook', (40, 30), (35,38), radius_x=5, radius_y=8)
        self.add_line('beak-inner', (35,38), (35,30))
        self.add_arc('chin', (35,30), (23, 44), radius_x=12, radius_y=14)
        self.add_line('neck', (23, 44), (23, 44))
        self.add_contour('outline', 'nape','crest-back','crest-top','crown','beak-top','beak-hook','beak-inner','chin','neck')
        self.add_dot('eye', (24,23))
