"""Electric Kick Scooter, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5a173d3f-0f7b-4dcd-a49d-423f38bee3a7'
SOURCE_PATH = 'pictographic-primitives/transportation/e scooter_5a173d3f-0f7b-4dcd-a49d-423f38bee3a7.svg'
AUTHOR = 'gpt-6'

class ElectricKickScooter(Solo48):
    icon_id = 'electric-kick-scooter'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('e-scooter', 'kick scooter', 'scooter', 'electric', 'micromobility', 'ride', 'transport', 'side view')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        for i,x in enumerate((10,38)):
            self.add_arc(f'wheel-{i}-a',(x-6,34),(x+6,34),radius_x=6)
            self.add_arc(f'wheel-{i}-b',(x+6,34),(x-6,34),radius_x=6)
            self.add_contour(f'wheel-{i}',f'wheel-{i}-a',f'wheel-{i}-b',closed=True)
        self.add_polyline('deck',(16,34),(27,34),(32,28),(38,28))
        self.relate('connect','deck','wheel-0')
        self.relate('connect','deck','wheel-1')
        self.add_line('steering',(30,8),(38,28))
        self.relate('connect','steering','deck')
        self.relate('connect','steering','wheel-1')
        self.add_polyline('handlebar',(26,8),(30,8),(36,8))
        self.relate('connect','handlebar','steering')
