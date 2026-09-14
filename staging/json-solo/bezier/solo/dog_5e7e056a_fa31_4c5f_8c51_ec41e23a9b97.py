"""Dog (pets), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e7e056a-fa31-4c5f-8c51-ec41e23a9b97'
SOURCE_PATH = 'icons-json/pets/dog_5e7e056a-fa31-4c5f-8c51-ec41e23a9b97.json'
AUTHOR = 'json_to_solo'

class Dog5e7e056a(Solo48):
    icon_id = 'dog-5e7e056a'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('dog', 'pets')

    def build(self):
        self.add_line('e0', (6, 35), (9, 27))
        self.add_line('e1', (17, 11), (21, 6))
        self.add_line('e2', (28, 17), (35, 18))
        self.add_line('e3', (25, 33), (23, 42))
        self.add_bezier('e4', (9, 27), ((10.923, 22.68), (13.094, 18.665), (15.385, 14.525)), ((16.055, 13.323), (16.231, 12.145), (17, 11)))
        self.add_bezier('e5', (21, 6), ((21.933, 8.135), (22.47, 10.312), (23.182, 12.529)), ((23.542, 13.658), (23.73, 15.262), (24.532, 16.17)), ((25.35, 17.095), (26.871, 16.861), (28, 17)))
        self.add_bezier('e6', (35, 18), ((38.003, 18.376), (41.984, 20.335), (41.984, 23.984)), ((41.992, 24.04), (42, 24.088), (42, 24.145)), ((42, 24.145), (42, 24.146), (42, 24.147)), ((41.992, 24.205), (41.992, 24.27), (41.984, 24.327)), ((41.984, 25.587), (41.55, 26.888), (40.953, 27.976)), ((37.975, 33.409), (30.195, 32.362), (25, 33)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6', 'e3')
