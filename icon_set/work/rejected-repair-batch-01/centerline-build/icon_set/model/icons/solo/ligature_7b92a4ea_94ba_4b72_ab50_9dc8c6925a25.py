"""ligature: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b92a4ea-94ba-4b72-ab50-9dc8c6925a25'
SOURCE_PATH = 'pictographic-primitives/interface-essential/ligature_7b92a4ea-94ba-4b72-ab50-9dc8c6925a25.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Ligature(Solo48):
    icon_id = 'ligature'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('ligature', 'interface-essential')

    def build(self):
        # VRECT_L (8,4)-(40,44); round arch joins the f stem tangentially.
        # Construction reference: Lucide type: continuous stems and crossbars
        self.add_arc('arch',(36,16),(12,16),radius_x=12,sweep=False)
        self.add_line('stem',(12,16),(12,44))
        self.add_contour('f-stem','arch','stem')
        self.add_polyline('i-stem',(12,26),(36,26),(36,44))
        self.add_line('left-foot',(8,44),(16,44))
        self.add_line('right-foot',(32,44),(40,44))
        self.add_line('left-crossbar',(8,26),(12,26))
        for a,b in [('f-stem','i-stem'),('f-stem','left-foot'),('f-stem','left-crossbar'),('i-stem','right-foot'),('i-stem','left-crossbar')]: self.relate('connect',a,b)
