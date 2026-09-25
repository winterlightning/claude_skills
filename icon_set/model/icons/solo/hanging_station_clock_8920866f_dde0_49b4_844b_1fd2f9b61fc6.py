"""Hanging Station Clock, rebuilt from the supplied reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8920866f-dde0-49b4-844b-1fd2f9b61fc6'
SOURCE_PATH = 'pictographic-primitives/transportation/clock station_8920866f-dde0-49b4-844b-1fd2f9b61fc6.svg'
AUTHOR = 'gpt-6'

class HangingStationClock(Solo48):
    icon_id = 'hanging-station-clock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('station clock', 'clock', 'railway', 'time', 'hanging clock', 'platform', 'schedule', 'station')

    def build(self) -> None:
        # SQUARE: current contract centerline extremes (6, 6)-(42, 42).
        self.add_polyline('post',(6,42),(6,6),(29,6),(42,6))
        self.add_line('hanger',(29,6),(29,16))
        self.relate('connect','post','hanger')
        self.add_arc('face-right',(29,16),(29,42),radius_x=13)
        self.add_arc('face-left',(29,42),(29,16),radius_x=13)
        self.add_contour('face','face-right','face-left',closed=True)
        self.relate('connect','hanger','face')
        self.add_polyline('hands',(29,25),(29,29),(33,29))
