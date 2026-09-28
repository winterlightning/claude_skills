'Clock: retain its left-and-down hand direction with the pivot at the center; give the long hand radial clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7f654f6-570d-40dd-84e5-be7ff0923e87'
SOURCE_PATH = 'pictographic-primitives/office/clock_e7f654f6-570d-40dd-84e5-be7ff0923e87.svg'
AUTHOR = 'gpt-6'

class ClockE7f654f6(Solo48):
    icon_id = 'clock-e7f654f6'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    categories = ('office', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('clock', 'office')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_polyline('hands',(13,24),(24,24),(24,33))
