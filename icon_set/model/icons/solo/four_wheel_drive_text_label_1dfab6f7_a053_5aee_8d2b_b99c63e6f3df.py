"""4WD Text Label, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1dfab6f7-a053-5aee-8d2b-b99c63e6f3df'
SOURCE_PATH = 'pictographic-primitives/transportation/four wheel drive_1dfab6f7-a053-5aee-8d2b-b99c63e6f3df.svg'
AUTHOR = 'gpt-6'

class FourWheelDriveTextLabel(Solo48):
    icon_id = 'four-wheel-drive-text-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('4wd', 'four wheel drive', '4x4', 'drivetrain', 'car', 'dashboard', 'text', 'label')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_polyline('four-top',(6,8),(6,24),(11,24))
        self.add_polyline('four-stem',(11,8),(11,24),(11,40))
        self.relate('connect','four-top','four-stem')
        self.add_polyline('w',(20,8),(22,40),(24,24),(26,40),(28,8))
        self.add_line('d-stem',(37,8),(37,40))
        self.add_arc('d-bowl',(37,40),(37,8),radius_x=7,radius_y=16,sweep=False)
        self.add_contour('d','d-stem','d-bowl',closed=True)
