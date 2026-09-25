'White House with pediment, broad wings and right-facing flag. HRECT_XL centerlines (6,8)-(42,40) emphasizes breadth. Lucide landmark informs pediment and columns; window ticks and internal portico divisions omitted; arched doorway retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '263f612f-d3a5-4c8d-9aaf-a7b8d76d3289'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/white house dc_263f612f-d3a5-4c8d-9aaf-a7b8d76d3289.svg'
AUTHOR = 'gpt-6'

class WhiteHouse(Solo48):
    icon_id = 'white-house'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    aliases = ()
    keywords = ('white house', 'washington', 'usa', 'president', 'government', 'mansion', 'landmark', 'flag')

    def build(self) -> None:
        axis, left, right, bottom = 24, 4, 44, 40
        self.add_polyline('flag',(axis,16),(34,16),(34,8),(axis,8),(axis,16),(axis,23))
        self.add_polyline('pediment',(14,30),(axis,23),(34,30))
        self.add_polyline('facade',(14,30),(left,30),(left,bottom),(20,bottom),(28,bottom),(right,bottom),(right,30),(34,30))
        self.add_line('door-left',(20,bottom),(20,36))
        self.add_arc('door-arch',(20,36),(28,36),radius_x=4)
        self.add_line('door-right',(28,36),(28,bottom))
        self.add_contour('door','door-left','door-arch','door-right')
        for a,b in [('flag','pediment'),('pediment','facade'),('door','facade')]:
            self.relate('connect',a,b)
