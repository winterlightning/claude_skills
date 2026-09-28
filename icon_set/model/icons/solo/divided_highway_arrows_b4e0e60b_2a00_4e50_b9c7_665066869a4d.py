"""Divided Highway Arrows, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b4e0e60b-2a00-4e50-b9c7-665066869a4d'
SOURCE_PATH = 'pictographic-primitives/transportation/divided highway ahead_b4e0e60b-2a00-4e50-b9c7-665066869a4d.svg'
AUTHOR = 'gpt-6'

class DividedHighwayArrows(Solo48):
    icon_id = 'divided-highway-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('divided highway', 'dual carriageway', 'two way', 'traffic', 'arrows', 'road sign', 'lanes', 'median')

    def build(self) -> None:
        # Current contract centerline extremes: (6,6)-(42,42).
        self.add_line('up-shaft',(12,42),(12,6))
        self.add_polyline('up-head',(6,12),(12,6),(18,12))
        self.relate('connect','up-shaft','up-head')
        self.add_line('median',(27,6),(27,18))
        self.add_line('down-upper',(40,6),(40,20))
        self.add_arc('down-bend-a',(40,20),(38,24),radius_x=2,radius_y=4)
        self.add_arc('down-bend-b',(38,24),(36,28),radius_x=2,radius_y=4,sweep=False)
        self.add_line('down-lower',(36,28),(36,42))
        self.add_contour('down-shaft','down-upper','down-bend-a','down-bend-b','down-lower')
        self.add_polyline('down-head',(30,36),(36,42),(42,36))
        self.relate('connect','down-shaft','down-head')
