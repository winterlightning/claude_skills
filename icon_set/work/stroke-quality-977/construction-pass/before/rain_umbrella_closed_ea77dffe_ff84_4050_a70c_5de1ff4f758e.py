"""Rain umbrella closed (weather), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea77dffe-ff84-4050-a70c-5de1ff4f758e'
SOURCE_PATH = 'pictographic-primitives/weather/rain umbrella closed_ea77dffe-ff84-4050-a70c-5de1ff4f758e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class RainUmbrellaClosed(Solo48):
    icon_id = 'rain-umbrella-closed'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('rain', 'umbrella', 'closed', 'weather')

    def build(self):
        self.add_line('e0', (24, 4), (24, 6))
        self.add_line('e1', (24, 41), (24, 31))
        self.add_line('e2', (24, 31), (40, 31))
        self.add_line('e3', (40, 31), (24, 6))
        self.add_line('e4', (24, 31), (8, 31))
        self.add_line('e5', (8, 31), (24, 6))
        self.add_line('e6-1', (16, 41), (17, 43))
        self.add_line('e6-2', (17, 43), (20, 44))
        self.add_arc('e6-3', (20, 44), (24, 41), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e6-1', 'e6-2', 'e6-3', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4', 'e5')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
