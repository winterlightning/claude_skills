"""flag-buoy-on-waves: Flag above a separate domed float and one water row; the directional pennant follows the source."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fdd7bd39-46cd-5b2f-9155-bc0b50b30900'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flag-buoy-on-waves/20260927T034714Z-thuan-mac-1/reference/diving flag buoys_fdd7bd39-46cd-5b2f-9155-bc0b50b30900.svg'
AUTHOR = "gpt-6"


class FlagBuoyOnWaves(Solo48):
    icon_id = 'flag-buoy-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('buoy', 'flag', 'diving', 'marker', 'sea', 'water', 'float', 'safety', 'outdoors-batch-01')

    def build(self):
        # Flag, domed float and water occupy separate visual tiers.
        self.add_polyline('pennant', (24, 6), (40, 10), (34, 12))
        self.add_line('mast', (24, 6), (24, 18))
        self.relate('connect', 'pennant', 'mast')
        self.add_arc('dome-left', (16, 30), (24, 18),
                     radius_x=8, radius_y=12, sweep=True)
        self.add_arc('dome-right', (24, 18), (32, 30),
                     radius_x=8, radius_y=12, sweep=True)
        self.add_line('float-base', (32, 30), (16, 30))
        self.add_contour('float', 'dome-left', 'dome-right', 'float-base', closed=True)
        self.relate('connect', 'mast', 'float')
        self.add_arc('water-left', (6, 41), (18, 41),
                     radius_x=6, radius_y=1, sweep=True)
        self.add_arc('water-middle', (18, 41), (30, 41),
                     radius_x=6, radius_y=1, sweep=False)
        self.add_arc('water-right', (30, 41), (42, 41),
                     radius_x=6, radius_y=1, sweep=True)
        self.add_contour('water', 'water-left', 'water-middle', 'water-right')
