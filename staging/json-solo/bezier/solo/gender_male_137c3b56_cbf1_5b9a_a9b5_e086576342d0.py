"""Gender male (users), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '137c3b56-cbf1-5b9a-a9b5-e086576342d0'
SOURCE_PATH = 'icons-json/users/gender male_137c3b56-cbf1-5b9a-a9b5-e086576342d0.json'
AUTHOR = 'json_to_solo'

class GenderMale137c3b56(Solo48):
    icon_id = 'gender-male-137c3b56'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    aliases = ()
    keywords = ('gender', 'male', 'users')

    def build(self):
        self.add_line('e0', (32, 6), (42, 6))
        self.add_line('e1', (42, 6), (29, 20))
        self.add_line('e2', (42, 16), (42, 6))
        self.add_arc('e3-top', (6, 29), (32, 29), radius_x=13)
        self.add_arc('e3-bottom', (32, 29), (6, 29), radius_x=13)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
