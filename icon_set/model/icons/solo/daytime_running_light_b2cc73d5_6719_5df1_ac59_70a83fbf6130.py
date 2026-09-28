"""Daytime Running Light, rebuilt from the supplied reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2cc73d5-6719-5df1-ac59-70a83fbf6130'
SOURCE_PATH = 'pictographic-primitives/transportation/day time running light_b2cc73d5-6719-5df1-ac59-70a83fbf6130.svg'
AUTHOR = 'gpt-6'

class DaytimeRunningLight(Solo48):
    icon_id = 'daytime-running-light'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('daytime running light', 'drl', 'headlight', 'lamp', 'car', 'dashboard', 'lighting', 'indicator')

    def build(self) -> None:
        # HRECT_L: current contract centerline extremes (6, 8)-(42, 40).
        self.add_line('lamp-back',(28,8),(28,40))
        self.add_arc('lamp-face',(28,40),(28,8),radius_x=16,sweep=False)
        self.add_contour('lamp','lamp-back','lamp-face',closed=True)
        for i in range(3):
            y=12+i*10
            self.add_line(f'beam-{i}',(4,y),(18,y+3))
