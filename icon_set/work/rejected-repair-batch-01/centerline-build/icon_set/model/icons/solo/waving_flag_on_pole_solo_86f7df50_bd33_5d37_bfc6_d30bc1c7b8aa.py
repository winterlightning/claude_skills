"""Notched flag waves right from an upright pole. SQUARE centerline extremes 6,6–42,42; Lucide flag informs repeated wave edges. Both supplied flag references describe the same construction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86f7df50-bd33-5d37-bfc6-d30bc1c7b8aa'
SOURCE_PATH = 'pictographic-primitives/social/flag_86f7df50-bd33-5d37-bfc6-d30bc1c7b8aa.svg'
AUTHOR = 'gpt-6'

class WavingFlagOnPoleSolo(Solo48):
    icon_id = 'waving-flag-on-pole-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/social"
    aliases = ()
    keywords = ('flag', 'pole', 'banner', 'pennant', 'waving', 'standard')

    def build(self):
        # Shared wave: half ellipses of equal width/depth, repeated 20 units below.
        self.add_line('pole-upper', (6,6), (6,10))
        self.add_line('pole-middle', (6,10), (6,30))
        self.add_line('pole-lower', (6,30), (6,42))
        self.add_contour('pole', 'pole-upper', 'pole-middle', 'pole-lower')
        self.add_arc('wave-top-left', (6,10), (24,10), radius_x=9, radius_y=3, sweep=False)
        self.add_arc('wave-top-right', (24,10), (42,10), radius_x=9, radius_y=3)
        self.add_polyline('notch', (42,10), (36,20), (42,30))
        self.add_arc('wave-bottom-right', (42,30), (24,30), radius_x=9, radius_y=3, sweep=False)
        self.add_arc('wave-bottom-left', (24,30), (6,30), radius_x=9, radius_y=3)
        self.add_contour('top', 'wave-top-left', 'wave-top-right')
        self.add_contour('bottom', 'wave-bottom-right', 'wave-bottom-left')
        self.relate('connect', 'pole', 'top')
        self.relate('connect', 'pole', 'bottom')
        self.relate('connect', 'top', 'notch')
        self.relate('connect', 'bottom', 'notch')
