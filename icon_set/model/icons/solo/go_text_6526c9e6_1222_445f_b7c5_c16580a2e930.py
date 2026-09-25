'GO lettering: round cap and baseline curves share exact HRECT_L extrema.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6526c9e6-1222-445f-b7c5-c16580a2e930'
SOURCE_PATH = 'pictographic-primitives/symbol/GO_6526c9e6-1222-445f-b7c5-c16580a2e930.svg'
AUTHOR = 'gpt-6'


class GoText(Solo48):
    icon_id = 'go-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    aliases = ()
    keywords = ('go', 'start', 'begin', 'text', 'action', 'proceed', 'letters')

    def build(self) -> None:
        # Equal cap heights and round ends; shared 8-unit radii on the two letters.
        self.add_arc('g-top',(20,16),(4,16),radius_x=8,sweep=False)
        self.add_line('g-left',(4,16),(4,32))
        self.add_arc('g-bottom',(4,32),(20,32),radius_x=8,sweep=False)
        self.add_polyline('g-bar',(20,32),(20,25),(12,25))
        self.add_contour('g','g-top','g-left','g-bottom')
        self.relate('connect','g','g-bar')
        self.add_arc('o-top',(28,16),(44,16),radius_x=8)
        self.add_line('o-right',(44,16),(44,32))
        self.add_arc('o-bottom',(44,32),(28,32),radius_x=8)
        self.add_line('o-left',(28,32),(28,16))
        self.add_contour('o','o-top','o-right','o-bottom','o-left',closed=True)
