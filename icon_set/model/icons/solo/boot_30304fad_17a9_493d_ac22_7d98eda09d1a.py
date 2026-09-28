"""Boot. Keeps two lace hooks, ankle shaft and heel step; drops the narrow doubled rim.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30304fad-17a9-493d-ac22-7d98eda09d1a'
SOURCE_PATH = 'pictographic-primitives/symbol/boot_30304fad-17a9-493d-ac22-7d98eda09d1a.svg'
AUTHOR = 'gpt-6'


class Boot(Solo48):
    icon_id = 'boot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('boot', 'shoe', 'footwear', 'hiking', 'work', 'ankle', 'fashion', 'winter')

    def build(self) -> None:
        self.add_line('shaft-1', (6, 6), (24, 6))
        self.add_line('shaft-2', (24, 6), (24, 16))
        self.add_line('shaft-3', (24, 16), (24, 24))
        self.add_arc('instep', (24, 24), (32, 32), radius_x=8, radius_y=8, sweep=False)
        self.add_line('toe-top', (32, 32), (36, 32))
        self.add_arc('toe', (36, 32), (42, 38), radius_x=6, radius_y=6, sweep=True)
        self.add_line('toe-side', (42, 38), (42, 42))
        self.add_line('sole-1', (42, 42), (22, 42))
        self.add_line('sole-2', (22, 42), (18, 38))
        self.add_line('sole-3', (18, 38), (6, 38))
        self.add_line('sole-4', (6, 38), (6, 6))
        self.add_contour('boot', 'shaft-1', 'shaft-2', 'shaft-3', 'instep', 'toe-top', 'toe', 'toe-side', 'sole-1', 'sole-2', 'sole-3', 'sole-4', closed=True)
        self.add_line('lace-one', (24, 16), (30, 16))
        self.add_line('lace-two', (24, 24), (30, 24))
        self.relate("connect", 'boot', 'lace-one')
        self.relate("connect", 'boot', 'lace-two')
