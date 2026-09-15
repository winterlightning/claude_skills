"""shapes: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80482a3e-5b08-4ded-ac07-3afb54321744'
SOURCE_PATH = 'pictographic-primitives/design/shapes_80482a3e-5b08-4ded-ac07-3afb54321744.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Shapes(Solo48):
    icon_id = 'shapes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shapes', 'design')

    def build(self):
        # SQUARE (6,6)-(42,42); true circle partially hidden behind square.
        # Construction reference: Lucide shapes: simple geometric subjects
        self.add_polyline('square',(20,20),(42,20),(42,42),(20,42),closed=True)
        self.add_arc('circle-top',(32,19),(6,19),radius_x=13,sweep=False)
        self.add_arc('circle-bottom',(6,19),(19,32),radius_x=13,sweep=False)
        self.add_line('right-contact',(32,19),(32,20))
        self.add_line('bottom-contact',(19,32),(20,32))
        self.add_contour('circle','circle-top','circle-bottom','bottom-contact')
        self.relate('connect','circle','square')
        self.relate('connect','circle','right-contact')
        self.relate('connect','right-contact','square')
