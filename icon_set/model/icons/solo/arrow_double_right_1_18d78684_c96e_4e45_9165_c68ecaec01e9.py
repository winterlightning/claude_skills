'Double right arrow: two equal, widely separated stroked chevrons; removed cramped hollow ribbon interiors while preserving direction. Lucide chevron-right reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18d78684-c96e-4e45-9165-c68ecaec01e9'
SOURCE_PATH = 'icons-json/arrows/arrow double right 1_18d78684-c96e-4e45-9165-c68ecaec01e9.json'
AUTHOR = 'gpt-6'

class ArrowDoubleRight1(Solo48):
    icon_id = 'arrow-double-right-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'double', 'right', 'arrows')

    def build(self) -> None:
        # Two equal chevrons; open strokes avoid cramped hollow ribbon counters at 48px.
        for label,x in (('left',4),('right',30)):
            self.add_polyline(label,(x,8),(x+14,24),(x,40))
