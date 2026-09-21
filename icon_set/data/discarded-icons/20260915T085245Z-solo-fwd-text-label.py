"""FWD Text Label, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '06084d76-f689-41e9-af67-fb957a5c2084'
SOURCE_PATH = 'pictographic-primitives/transportation/front wheel drive_06084d76-f689-41e9-af67-fb957a5c2084.svg'
AUTHOR = 'gpt-6'

class FwdTextLabel(Solo48):
    icon_id = 'fwd-text-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('fwd', 'front wheel drive', 'drivetrain', 'car', 'dashboard', 'text', 'label', 'transmission')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_polyline('f',(4,40),(4,24),(4,8),(11,8))
        self.add_line('f-crossbar',(4,24),(11,24))
        self.relate('connect','f','f-crossbar')
        self.add_polyline('w',(20,8),(22,40),(24,24),(26,40),(28,8))
        self.add_line('d-stem',(37,8),(37,40))
        self.add_arc('d-bowl',(37,40),(37,8),radius_x=7,radius_y=16,sweep=False)
        self.add_contour('d','d-stem','d-bowl',closed=True)
