"""A windscreen with two rising airflow arrows; the small middle dash is omitted. HRECT_L ink (6,6)-(42,42). Lucide car-front informs the bilateral screen construction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41f88605-cfdf-537e-9777-6da8f3a89587'
SOURCE_PATH = 'pictographic-primitives/transportation/air conditioner front_41f88605-cfdf-537e-9777-6da8f3a89587.svg'
AUTHOR = 'gpt-6'

class WindscreenAirflow(Solo48):
    icon_id = 'windscreen-airflow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('windscreen', 'windshield', 'defrost', 'demist', 'airflow', 'air conditioning', 'car', 'dashboard')

    def build(self) -> None:
        # A shared axis owns the screen and paired air streams.
        self.add_arc('screen-top',(6,16),(42,16),radius_x=29,radius_y=29)
        self.add_line('screen-right',(42,16),(41,24))
        self.add_line('screen-left',(7,24),(6,16))
        self.add_contour('screen','screen-left','screen-top','screen-right')
        for i,x in enumerate((17,31)):
            self.add_polyline(f'air-{i}',(x,40),(x,23))
            self.add_polyline(f'head-{i}',(x-3,28),(x,23),(x+3,28))
            self.relate('connect',f'air-{i}',f'head-{i}')
