from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '403c6d7a-f554-4477-bbd6-4a46c6ec47dc'
SOURCE_PATH = 'pictographic-primitives/transportation/right curve 1_403c6d7a-f554-4477-bbd6-4a46c6ec47dc.svg'
AUTHOR = 'gpt-6'

class SCurveArrow(Solo48):
    icon_id = 's-curve-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('curve', 'road', 'arrow', 'bend', 'winding', 'direction', 'traffic', 'right curve')

    def build(self):
        self.add_line('lower',(8,44),(8,34))
        self.add_arc('lower-bend',(8,34),(20,22),radius_x=12,sweep=True)
        self.add_arc('upper-bend',(20,22),(32,10),radius_x=12,sweep=False)
        self.add_line('upper',(32,10),(32,4))
        self.add_contour('shaft','lower','lower-bend','upper-bend','upper')
        self.add_polyline('head',(24,12),(32,4),(40,12))
        self.relate('connect','shaft','head')
