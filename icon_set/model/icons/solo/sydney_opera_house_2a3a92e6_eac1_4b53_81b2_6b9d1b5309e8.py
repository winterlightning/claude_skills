"""Three pointed shell sails on a low podium; rear shell and ribs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a3a92e6-eac1-4b53-81b2-6b9d1b5309e8'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/sydney opera house_2a3a92e6-eac1-4b53-81b2-6b9d1b5309e8.svg'
AUTHOR = 'gpt-6'

class SydneyOperaHouse(Solo48):
    icon_id = 'sydney-opera-house'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('sydney opera house', 'australia', 'opera', 'shells', 'sails', 'landmark', 'architecture', 'harbour')

    def build(self) -> None:
        # HRECT_L centerline extremes (2,8)-(46,40).
        self.add_polyline('podium', (2, 32), (46, 32), (46, 40), (2, 40), closed=True)
        self.add_line('main-leading', (20, 32), (16, 8))
        self.add_arc('main-back', (16, 8), (30, 32), radius_x=25, sweep=True)
        self.add_contour('main-shell', 'main-leading', 'main-back')
        self.add_line('left-leading', (8, 32), (2, 18))
        self.add_arc('left-back', (2, 18), (18, 20), radius_x=23, sweep=True)
        self.add_contour('left-shell', 'left-leading', 'left-back')
        self.add_arc('right-back', (30, 32), (46, 19), radius_x=22, sweep=True)
        self.add_line('right-leading', (46, 19), (40, 32))
        self.add_contour('right-shell', 'right-back', 'right-leading')
        self.relate('connect', 'podium', 'main-shell')
        self.relate('connect', 'podium', 'left-shell')
        self.relate('connect', 'podium', 'right-shell')
        self.relate('connect', 'main-shell', 'left-shell')
        self.relate('connect', 'main-shell', 'right-shell')
