"""text-bold: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8004bf6f-3430-545f-9b06-3c0cc0268453'
SOURCE_PATH = 'pictographic-primitives/interface-essential/text bold_8004bf6f-3430-545f-9b06-3c0cc0268453.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class TextBold(Solo48):
    icon_id = 'text-bold'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('text', 'bold', 'interface-essential')

    def build(self):
        # VRECT_L (8,4)-(40,44); two equal ellipse halves with horizontal end tangents.
        # Construction reference: Lucide bold: shared bowl dimensions
        left, bowl_x, radius_x, radius_y = 8,28,12,10
        self.add_line('top',(left,4),(bowl_x,4))
        self.add_arc('upper-bowl',(bowl_x,4),(bowl_x,24),radius_x=radius_x,radius_y=radius_y)
        self.add_arc('lower-bowl',(bowl_x,24),(bowl_x,44),radius_x=radius_x,radius_y=radius_y)
        self.add_line('bottom',(bowl_x,44),(left,44))
        self.add_line('stem',(left,44),(left,4))
        self.add_contour('letter','top','upper-bowl','lower-bowl','bottom','stem',closed=True)
        self.add_line('middle',(left,24),(bowl_x,24))
        self.relate('connect','middle','letter')
