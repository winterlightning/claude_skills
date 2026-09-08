"""King's Cross: round-headed station facade, clock with hands and arched entrance; ledges and mullion omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7abdda87-4807-5b73-8c34-25738397da1a'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/kings cross london_7abdda87-4807-5b73-8c34-25738397da1a.svg'
AUTHOR = 'gpt-6'


class KingsCrossStation(Solo48):
    icon_id = 'kings-cross-station'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('kings cross', 'london', 'station', 'railway', 'clock', 'arch', 'landmark', 'travel')

    def build(self) -> None:
        # Centerline extremes: (5,2)-(43,46).
        self.add_line('wall-left',(5,46),(5,21))
        self.add_arc('roof',(5,21),(43,21),radius_x=19,sweep=True)
        self.add_line('wall-right',(43,21),(43,46))
        self.add_contour('facade','wall-left','roof','wall-right')
        self.add_arc('clock-a',(24,11),(24,29),radius_x=9,sweep=True)
        self.add_arc('clock-b',(24,29),(24,11),radius_x=9,sweep=True)
        self.add_contour('clock','clock-a','clock-b',closed=True)
        self.add_polyline('hands',(24,18),(24,21),(26,21))
        self.add_arc('entrance',(15,46),(33,46),radius_x=9,sweep=True)
