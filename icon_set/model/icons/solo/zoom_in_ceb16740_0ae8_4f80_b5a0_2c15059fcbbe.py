'Zoom in: round glass and centred equal plus arms; clear internal margins and attached handle.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ceb16740-0ae8-4f80-b5a0-2c15059fcbbe'
SOURCE_PATH = 'icons-json/interface-essential/zoom in_ceb16740-0ae8-4f80-b5a0-2c15059fcbbe.json'
AUTHOR = 'gpt-6'

class ZoomInInterfaceEssential(Solo48):
    icon_id = 'zoom-in-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zoom', 'in', 'interface-essential')

    def build(self) -> None:
        self.add_arc('glass-top', (6,21), (36,21), radius_x=15, radius_y=15)
        self.add_arc('glass-bottom', (36,21), (6,21), radius_x=15, radius_y=15)
        self.add_contour('glass', 'glass-top', 'glass-bottom', closed=True)

        self.add_polyline('plus-horizontal',(15,21),(21,21),(27,21))
        self.add_polyline('plus-vertical',(21,15),(21,21),(21,27))
        self.relate('connect','plus-horizontal','plus-vertical')
        self.add_line('handle',(30,33),(42,42))
        self.relate('connect','handle','glass')
