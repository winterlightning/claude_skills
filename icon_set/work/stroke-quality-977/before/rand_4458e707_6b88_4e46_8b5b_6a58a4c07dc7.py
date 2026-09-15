"""rand: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4458e707-6b88-4e46-8b5b-6a58a4c07dc7'
SOURCE_PATH = 'pictographic-primitives/money/rand_4458e707-6b88-4e46-8b5b-6a58a4c07dc7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Rand(Solo48):
    icon_id = 'rand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('rand', 'money')

    def build(self):
        # VRECT_L (8,4)-(40,44); one circular bowl, purposeful corners at the spine.
        # Construction reference: Lucide bold: clean bowl meeting straight stems
        self.add_line('stem',(8,44),(8,4))
        self.add_line('top',(8,4),(28,4))
        self.add_arc('bowl',(28,4),(28,28),radius_x=12)
        self.add_line('middle',(28,28),(8,28))
        self.add_contour('letter','stem','top','bowl','middle')
        self.add_line('leg',(28,28),(40,44))
        self.relate('connect','letter','leg')
