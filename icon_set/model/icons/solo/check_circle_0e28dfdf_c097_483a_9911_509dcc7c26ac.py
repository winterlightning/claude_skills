'Checked circle: concentric rim and optically centered check, retaining the rising diagonal. Lucide circle-check reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e28dfdf-c097-483a-9911-509dcc7c26ac'
SOURCE_PATH = 'icons-json/interface-essential/check circle_0e28dfdf-c097-483a-9911-509dcc7c26ac.json'
AUTHOR = 'gpt-6'

class CheckCircle(Solo48):
    icon_id = 'check-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('check', 'circle', 'interface-essential')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_polyline('check',(15,25),(21,30),(31,17))
