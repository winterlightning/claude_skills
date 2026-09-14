"""A person slipping with arms flung out and feet to the lower left. SQUARE extremes (6,6)-(42,42). Lucide person-standing informs the connected stick framework; follow the source image pose rather than mirroring its directional text. Preserve the asymmetric splayed limbs and falling lean."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f0ac7d1-2c65-44de-9523-d762d29b36e3'
SOURCE_PATH = 'pictographic-primitives/symbol/person slipping rocky_7f0ac7d1-2c65-44de-9523-d762d29b36e3.svg'
AUTHOR = 'gpt-6'


class PersonSlippingBackward(Solo48):
    icon_id = 'person-slipping-backward'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('slip', 'fall', 'person', 'accident', 'hazard', 'trip', 'injury', 'warning')

    def build(self) -> None:
        cx, cy, radius = 32, 10, 4
        self.add_arc('head-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body-leg',(24,22),(20,32),(14,42))
        self.add_polyline('arm-left',(24,22),(14,16),(10,10))
        self.add_polyline('arm-right',(24,22),(36,24),(42,32))
        self.add_polyline('leg-left',(20,32),(12,32),(6,38))
        for part in ['arm-left','arm-right','leg-left']:
            self.relate('connect','body-leg',part)
