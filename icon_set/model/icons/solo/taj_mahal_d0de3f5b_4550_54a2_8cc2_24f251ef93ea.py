'Taj Mahal with pointed dome, crescent and paired minaret uprights. SQUARE centerlines (6,6)-(42,42). Dome joins the cornice; terrace ornament omitted; arched doorway retained. Source supplies identity; shared-axis construction follows Lucide landmark.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0de3f5b-4550-54a2-8cc2-24f251ef93ea'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/taj mahal_d0de3f5b-4550-54a2-8cc2-24f251ef93ea.svg'
AUTHOR = 'gpt-6'

class TajMahal(Solo48):
    icon_id = 'taj-mahal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    aliases = ()
    keywords = ('taj mahal', 'india', 'agra', 'mausoleum', 'dome', 'minaret', 'landmark', 'heritage')

    def build(self) -> None:
        axis, left, right, bottom = 24, 6, 42, 42
        self.add_arc('crescent-left',(20,6),(axis,10),radius_x=4,sweep=False)
        self.add_arc('crescent-right',(axis,10),(28,6),radius_x=4,sweep=False)
        self.add_contour('crescent','crescent-left','crescent-right')
        self.add_line('finial',(axis,10),(axis,17))
        self.add_arc('dome-left',(axis,17),(14,28),radius_x=12,radius_y=11,sweep=False)
        self.add_arc('dome-right',(34,28),(axis,17),radius_x=12,radius_y=11,sweep=False)
        self.add_polyline('roof',(left,28),(14,28),(20,28),(28,28),(34,28),(right,28))
        self.add_polyline('terrace',(left,20),(left,28),(left,bottom),(axis,bottom),(right,bottom),(right,28),(right,20))
        self.add_line('door-left',(20,bottom),(20,37))
        self.add_arc('door-arch',(20,37),(28,37),radius_x=4)
        self.add_line('door-right',(28,37),(28,bottom))
        self.add_contour('entrance','door-left','door-arch','door-right')
        for a,b in [('crescent','finial'),('finial','dome-left'),('finial','dome-right'),('dome-left','dome-right'),('dome-left','roof'),('dome-right','roof'),('roof','terrace'),('entrance','terrace')]:
            self.relate('connect',a,b)
