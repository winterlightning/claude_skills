"""White House pediment, flag and broad wings. Centerline extremes (2,5)-(46,43). Lucide landmark informs portico rhythm. Window ticks omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '263f612f-d3a5-4c8d-9aaf-a7b8d76d3289'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/white house dc_263f612f-d3a5-4c8d-9aaf-a7b8d76d3289.svg'
AUTHOR = 'gpt-6'

class WhiteHouse(Solo48):
    icon_id = 'white-house'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('white house', 'washington', 'usa', 'president', 'government', 'mansion', 'landmark', 'flag')

    def build(self) -> None:
        self.add_polyline('flag', (24, 13), (34, 13), (34, 5), (24, 5), (24, 13), (24, 20), closed=False)
        self.add_polyline('pediment', (12, 28), (24, 20), (36, 28), closed=True)
        self.add_polyline('facade', (12, 28), (12, 43), (20, 43), (28, 43), (36, 43), (36, 28), closed=False)
        self.add_polyline('left-wing', (12, 28), (2, 28), (2, 43), (12, 43), closed=False)
        self.add_polyline('right-wing', (36, 28), (46, 28), (46, 43), (36, 43), closed=False)
        self.add_line('door-left', (20, 43), (20, 39))
        self.add_arc('door-arch', (20, 39), (28, 39), radius_x=4, radius_y=4, sweep=True)
        self.add_line('door-right', (28, 39), (28, 43))
        self.add_contour('door', 'door-left', 'door-arch', 'door-right', closed=False)
        self.relate("connect", 'flag', 'pediment')
        self.relate("connect", 'pediment', 'facade')
        self.relate("connect", 'pediment', 'left-wing')
        self.relate("connect", 'pediment', 'right-wing')
        self.relate("connect", 'facade', 'left-wing')
        self.relate("connect", 'facade', 'right-wing')
        self.relate("connect", 'facade', 'door')
