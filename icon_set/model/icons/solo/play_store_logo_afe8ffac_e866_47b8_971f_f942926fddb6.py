"""Play store logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'afe8ffac-e866-47b8-971f-f942926fddb6'
SOURCE_PATH = 'pictographic-primitives/logos/play store logo_afe8ffac-e866-47b8-971f-f942926fddb6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PlayStoreLogo(Solo48):
    icon_id = 'play-store-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('play', 'store', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (8, 7), (8, 41))
        self.add_line('e1', (12, 44), (38, 27))
        self.add_line('e2', (38, 21), (13, 5))
        self.add_arc('e3-1', (13, 5), (11, 4), radius_x=3, sweep=False)
        self.add_arc('e3-2', (11, 4), (8, 7), radius_x=3, sweep=False)
        self.add_arc('e4-1', (8, 41), (10, 44), radius_x=4, sweep=False)
        self.add_line('e4-2', (10, 44), (12, 44))
        self.add_line('e5-1', (38, 27), (40, 24))
        self.add_line('e5-2', (40, 24), (38, 21))
        self.add_contour('c0', 'e3-1', 'e3-2', 'e0', 'e4-1', 'e4-2', 'e1', 'e5-1', 'e5-2', 'e2', closed=True)
