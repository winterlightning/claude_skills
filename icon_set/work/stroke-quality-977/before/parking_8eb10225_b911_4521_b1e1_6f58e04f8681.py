"""parking: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8eb10225-b911-4521-b1e1-6f58e04f8681'
SOURCE_PATH = 'pictographic-primitives/transportation/parking_8eb10225-b911-4521-b1e1-6f58e04f8681.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Parking(Solo48):
    icon_id = 'parking'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('parking', 'transportation')

    def build(self):
        # VRECT_L (8,4)-(40,44); one circular bowl, purposeful corners at the spine.
        # Construction reference: Lucide bold: clean bowl meeting straight stems
        self.add_line('stem',(8,44),(8,4))
        self.add_line('top',(8,4),(28,4))
        self.add_arc('bowl',(28,4),(28,28),radius_x=12)
        self.add_line('middle',(28,28),(8,28))
        self.add_contour('letter','stem','top','bowl','middle')
