"""Used an oval dial to retain eight-unit strap bands inside the upright envelope; retained two hands.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: watch: centered dial with paired attached straps.
"""
# Independent repair of analogue-wristwatch; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f3e245f-ff22-445c-9c0b-9969d193eb11'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/watch_6f3e245f-ff22-445c-9c0b-9969d193eb11.svg'
AUTHOR = 'gpt-6'

class AnalogueWristwatchVariant5(Solo48):
    icon_id = 'analogue-wristwatch-v5'
    variant_of = 'analogue-wristwatch'
    variant_label = 'Fit current SOLO48 bounds and spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('watch', 'wristwatch', 'time', 'clock', 'analogue', 'dial', 'strap', 'accessory')

    def build(self) -> None:
        # VRECT_L centerlines (8,4)-(40,44). Elliptical dial leaves an
        # eight-unit strap band; both straps attach at split cardinal nodes.
        cx, cy, rx, ry = 24, 24, 16, 12
        for name,a,b in [('ne',(cx,cy-ry),(cx+rx,cy)),
                         ('se',(cx+rx,cy),(cx,cy+ry)),
                         ('sw',(cx,cy+ry),(cx-rx,cy)),
                         ('nw',(cx-rx,cy),(cx,cy-ry))]:
            self.add_arc(name,a,b,radius_x=rx,radius_y=ry)
        self.add_contour('face','ne','se','sw','nw',closed=True)
        self.add_polyline('upper-strap',(24,12),(16,12),(16,4),(32,4),(32,12),(24,12))
        self.add_polyline('lower-strap',(24,36),(16,36),(16,44),(32,44),(32,36),(24,36))
        self.relate('connect','upper-strap','face')
        self.relate('connect','lower-strap','face')
        self.add_polyline('hands',(20,23),(24,26),(28,22))
