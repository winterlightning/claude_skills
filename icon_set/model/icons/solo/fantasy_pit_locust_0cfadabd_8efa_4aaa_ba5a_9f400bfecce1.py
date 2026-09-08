"""Mirrored swept wings and tapered abdomen, informed by Lucide bug symmetry; omit tiny side legs and segmentation."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cfadabd-8efa-4aaa-ba5a-9f400bfecce1'
SOURCE_PATH = 'pictographic-primitives/animals/fantasy pit locust_0cfadabd-8efa-4aaa-ba5a-9f400bfecce1.svg'
AUTHOR = 'gpt-6'


class WingedInsect(Solo48):
    icon_id = 'winged-insect'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('winged', 'insect')

    def build(self) -> None:
        # Visible keyshape bounds: (0, 0, 48, 48); centerlines inset by 2.
        self.add_polyline('thorax', (17, 13), (17, 22), (31, 22), (31, 13), (17, 13))
        self.add_polyline('antenna-left', (17, 13), (13, 2))
        self.add_polyline('antenna-right', (31, 13), (35, 2))
        self.relate("connect", 'thorax', 'antenna-left')
        self.relate("connect", 'thorax', 'antenna-right')
        self.add_arc('wing-left-outer', (17, 22), (2, 38), radius_x=50, radius_y=50, sweep=False)
        self.add_arc('wing-left-tip', (2, 38), (15, 39), radius_x=9, radius_y=9, sweep=False)
        self.add_line('wing-left-inner', (15, 39), (17, 22))
        self.add_contour('left-wing', 'wing-left-outer', 'wing-left-tip', 'wing-left-inner')
        self.add_arc('wing-right-outer', (31, 22), (46, 38), radius_x=50, radius_y=50, sweep=True)
        self.add_arc('wing-right-tip', (46, 38), (33, 39), radius_x=9, radius_y=9, sweep=True)
        self.add_line('wing-right-inner', (33, 39), (31, 22))
        self.add_contour('right-wing', 'wing-right-outer', 'wing-right-tip', 'wing-right-inner')
        self.relate("connect", 'thorax', 'left-wing')
        self.relate("connect", 'thorax', 'right-wing')
        self.add_arc('abdomen-left', (17, 30), (24, 46), radius_x=22, radius_y=22, sweep=False)
        self.add_arc('abdomen-right', (24, 46), (31, 30), radius_x=22, radius_y=22, sweep=False)
        self.add_contour('abdomen', 'abdomen-left', 'abdomen-right')
        self.relate("connect", 'left-wing', 'abdomen')
        self.relate("connect", 'right-wing', 'abdomen')
