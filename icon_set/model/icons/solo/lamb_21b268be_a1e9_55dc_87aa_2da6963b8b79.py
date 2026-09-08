"""Right-facing sheep. Lucide cloud informs broad fleece lobes; smooth head contrasts with wool. Tiny ear omitted, two legs retained; pose intentionally asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21b268be-a1e9-55dc-87aa-2da6963b8b79'
SOURCE_PATH = 'pictographic-primitives/animals/lamb_21b268be-a1e9-55dc-87aa-2da6963b8b79.svg'
AUTHOR = 'gpt-6'


class FluffySheep(Solo48):
    icon_id = 'fluffy-sheep'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('sheep', 'wool', 'fluffy', 'lamb', 'farm', 'livestock', 'ewe', 'animal')

    def build(self) -> None:
        # Exact visible extremes: (0, 6, 48, 42); centerline inset 2.
        self.add_arc('fleece-top-left', (8, 16), (17, 11), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('fleece-top', (17, 11), (29, 11), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('fleece-bottom-right', (36, 26), (28, 33), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('fleece-bottom', (28, 33), (16, 33), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('fleece-bottom-left', (16, 33), (8, 30), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('fleece-left-bottom', (8, 30), (2, 23), radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('fleece-left-top', (2, 23), (8, 16), radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('fleece', 'fleece-bottom-right', 'fleece-bottom', 'fleece-bottom-left', 'fleece-left-bottom', 'fleece-left-top', 'fleece-top-left', 'fleece-top', closed=False)
        self.add_arc('head-top-left', (29, 11), (36, 8), radius_x=7, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('head-top-right', (36, 8), (46, 20), radius_x=10, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (46, 20), (36, 26), radius_x=10, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('head-back', (36, 26), (29, 11), radius_x=9, radius_y=12, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top-left', 'head-top-right', 'head-bottom', 'head-back', closed=True)
        self.relate("connect", 'head', 'fleece')
        self.add_line('leg-left', (8, 30), (8, 40))
        self.add_line('leg-right', (28, 33), (28, 40))
        self.relate("connect", 'leg-left', 'fleece')
        self.relate("connect", 'leg-right', 'fleece')
