'A cigarette tilts upward to the right above a shallow open ashtray. Two curling smoke trails rise from its left end, while the tray has a flat bottom and upturned ends.\n\nConstruction: One diagonal cigarette above an open tray and one curl of smoke; reduced two smoke strands to one. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8dbec6e-b3b3-4d69-bfb5-484ff8729edb'
SOURCE_PATH = 'pictographic-primitives/wayfinding/cigarette disposal_c8dbec6e-b3b3-4d69-bfb5-484ff8729edb.svg'
AUTHOR = 'gpt-6'

class CigaretteInAshtray(Solo48):
    icon_id = 'cigarette-in-ashtray'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('cigarette', 'ashtray', 'smoking', 'disposal', 'tobacco', 'smoke')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('tray-1', (4, 31), (4, 40))
        self.add_line('tray-2', (4, 40), (44, 40))
        self.add_line('tray-3', (44, 40), (44, 31))
        self.add_line('cigarette-1', (17, 22), (36, 10))
        self.add_line('cigarette-2', (36, 10), (41, 18))
        self.add_line('cigarette-3', (41, 18), (22, 30))
        self.add_line('cigarette-4', (22, 30), (17, 22))
        self.add_arc('smoke', (4, 8), (10, 14), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('smoke-tail', (10, 14), (10, 16))
        self.add_contour('tray', 'tray-1', 'tray-2', 'tray-3', closed=False)
        self.add_contour('cigarette', 'cigarette-1', 'cigarette-2', 'cigarette-3', 'cigarette-4', closed=True)
        self.add_contour('smoke-trail', 'smoke', 'smoke-tail', closed=False)
