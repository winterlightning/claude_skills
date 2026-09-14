"""A sports bicycle with a diamond frame and drop handlebar. SQUARE ink (6,6)-(42,42) gives the frame room over the wheels. Lucide bike informed equal circles; spokes omitted and open struts avoid crossed holes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de1e3329-5d1d-5faf-89b6-906f5dde19a6'
SOURCE_PATH = 'pictographic-primitives/transportation/bicycle sports_de1e3329-5d1d-5faf-89b6-906f5dde19a6.svg'
SOURCE_REFERENCES = (('de1e3329-5d1d-5faf-89b6-906f5dde19a6', 'pictographic-primitives/transportation/bicycle sports_de1e3329-5d1d-5faf-89b6-906f5dde19a6.svg'),)
AUTHOR = 'gpt-6'

class SportsBicycle(Solo48):
    icon_id = 'sports-bicycle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('bicycle', 'bike', 'sports', 'racing', 'road bike', 'cycling', 'drop handlebar', 'pedal')

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

        self.add_line('seat-tube',(20,10),(25,21))
        self.relate('connect','seat-tube','frame')
