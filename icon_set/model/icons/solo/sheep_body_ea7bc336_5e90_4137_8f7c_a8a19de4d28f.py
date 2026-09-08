from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea7bc336-5e90-4137-8f7c-a8a19de4d28f'
SOURCE_PATH = 'pictographic-primitives/animals/sheep body_ea7bc336-5e90-4137-8f7c-a8a19de4d28f.svg'
AUTHOR = 'gpt-6'


class WoollySheep(Solo48):
    icon_id = 'woolly-sheep'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/farm"
    aliases = ()
    keywords = ('sheep', 'wool', 'fluffy', 'farm', 'lamb', 'ewe', 'livestock', 'animal')

    def build(self) -> None:
        self.add_arc('fleece-top', (2, 25), (18, 9), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('fleece-shoulder', (18, 9), (28, 10), radius_x=30, radius_y=30, sweep=True, large_arc=False)
        self.add_arc('fleece-right', (34, 25), (18, 37), radius_x=16, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('fleece-left', (18, 37), (2, 25), radius_x=16, radius_y=12, sweep=True, large_arc=False)
        self.add_contour('fleece', 'fleece-right', 'fleece-left', 'fleece-top', 'fleece-shoulder', closed=False)
        self.add_arc('head-left', (28, 10), (36, 24), radius_x=8, radius_y=14, sweep=False, large_arc=False)
        self.add_arc('head-right', (36, 24), (44, 10), radius_x=8, radius_y=14, sweep=False, large_arc=False)
        self.add_arc('crown', (44, 10), (28, 10), radius_x=8, radius_y=5, sweep=False, large_arc=False)
        self.add_contour('head', 'head-left', 'head-right', 'crown', closed=True)
        self.relate("connect", 'fleece', 'head')
        self.add_line('ear', (44, 10), (46, 5))
        self.relate("connect", 'ear', 'head')
        self.add_line('hind-leg', (10, 36), (10, 43))
        self.add_line('front-leg', (28, 35), (28, 43))
        self.relate("connect", 'hind-leg', 'fleece')
        self.relate("connect", 'front-leg', 'fleece')
