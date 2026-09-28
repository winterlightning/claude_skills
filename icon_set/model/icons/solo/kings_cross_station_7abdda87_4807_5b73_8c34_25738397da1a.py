'Kings Cross station: retain the arched facade, centred circular clock and broad entrance; omit illegible clock hands to keep the small clock clear.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7abdda87-4807-5b73-8c34-25738397da1a'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/kings cross london_7abdda87-4807-5b73-8c34-25738397da1a.svg'
AUTHOR = 'gpt-6'


class KingsCrossStation(Solo48):
    icon_id = 'kings-cross-station'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    categories = ("landmarks", "primitives")
    aliases = ()
    keywords = ('kings cross', 'london', 'station', 'railway', 'clock', 'arch', 'landmark', 'travel')

    def build(self) -> None:
        self.add_line('wall-left',(6,42),(6,24))
        self.add_bezier('roof',(6,24),((6,14),(15,6),(24,6)),((33,6),(42,14),(42,24)))
        self.add_line('wall-right',(42,24),(42,42))
        self.add_contour('facade','wall-left','roof','wall-right')

        self.add_arc('clock-top', (19,20), (29,20), radius_x=5, radius_y=5)
        self.add_arc('clock-bottom', (29,20), (19,20), radius_x=5, radius_y=5)
        self.add_contour('clock', 'clock-top', 'clock-bottom', closed=True)

        self.add_arc('entrance',(15,42),(33,42),radius_x=9,radius_y=8)
