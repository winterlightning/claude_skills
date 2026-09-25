"""An open roll-cage dune buggy facing right; repeated wheels and a low chassis. HRECT_L ink (6,6)-(42,42). Lucide car-front informs shared body attachments; hubs and minor frame bars omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb0b20be-48e9-58c8-a781-dea110e7df94'
SOURCE_PATH = 'pictographic-primitives/transportation/adventure car atv_bb0b20be-48e9-58c8-a781-dea110e7df94.svg'
AUTHOR = 'gpt-6'

class DuneBuggy(Solo48):
    icon_id = 'dune-buggy'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('buggy', 'dune buggy', 'off-road', 'atv', 'vehicle', 'adventure', 'roll cage', 'offroad')

    def build(self) -> None:
        # The paired wheels share a radius and baseline; front cage slopes intentionally.
        wheel_y, radius = 34, 6
        for side,x in [('rear',10),('front',38)]:
            self.add_arc(side+'-upper',(x-radius,wheel_y),(x+radius,wheel_y),radius_x=radius)
            self.add_arc(side+'-lower',(x+radius,wheel_y),(x-radius,wheel_y),radius_x=radius)
            self.add_contour(side+'-wheel',side+'-upper',side+'-lower',closed=True)
        self.add_polyline('cage',(7,19),(14,8),(25,8),(35,19))
        self.add_polyline('body',(6,19),(7,19),(16,19),(22,24),(26,24),(35,19),(42,19))
        self.relate('connect','cage','body')
