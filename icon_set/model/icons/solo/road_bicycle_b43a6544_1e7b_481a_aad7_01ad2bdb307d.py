"""A road bicycle with a diamond frame and drop handlebar. SQUARE ink (6,6)-(42,42) gives the frame room over the wheels. Lucide bike informed equal circles; spokes omitted and open struts avoid crossed holes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b43a6544-1e7b-481a-aad7-01ad2bdb307d'
SOURCE_PATH = 'pictographic-primitives/transportation/bicycle_b43a6544-1e7b-481a-aad7-01ad2bdb307d.svg'
SOURCE_REFERENCES = (('b43a6544-1e7b-481a-aad7-01ad2bdb307d', 'pictographic-primitives/transportation/bicycle_b43a6544-1e7b-481a-aad7-01ad2bdb307d.svg'),)
AUTHOR = 'gpt-6'

class RoadBicycle(Solo48):
    icon_id = 'road-bicycle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('bicycle', 'bike', 'road bike', 'racing', 'cycling', 'drop handlebar', 'pedal', 'sport')

    def build(self) -> None:
        for side,x in [('rear',12),('front',36)]:
            self.add_arc(side+'-right',(x,30),(x,42),radius_x=6)
            self.add_arc(side+'-left',(x,42),(x,30),radius_x=6)
            self.add_contour(side+'-wheel',side+'-right',side+'-left',closed=True)
        self.add_polyline('frame',(12,21),(20,10),(30,10),(25,21),(12,21),closed=True)
        self.add_line('rear-strut',(12,21),(12,30))
        self.add_polyline('fork',(36,30),(30,10),(28,6),(38,6))
        self.add_arc('bar-curl',(38,6),(38,14),radius_x=4)
        self.add_line('seat-post',(20,10),(16,6))
        self.add_polyline('saddle',(12,6),(16,6),(20,6))
        for a,b in [('frame','fork'),('fork','bar-curl'),('frame','seat-post'),('seat-post','saddle'),('rear-strut','frame'),('rear-strut','rear-wheel'),('fork','front-wheel')]:
            self.relate('connect',a,b)

        # Low racing frame keeps its large open counter; the internal seat tube is omitted.
