"""Monkey head with a heart-shaped facial mask flowing into a broad projecting muzzle. Restored large round ears and lower muzzle proportions from the supplied source. Small mouth line omitted; mirrored about x=24. Lucide cat informs smooth paired skull arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a46ab9a-ddfa-4f55-af29-5b8c5fbf44f9'
SOURCE_PATH = 'pictographic-primitives/animals/monkey 1_9a46ab9a-ddfa-4f55-af29-5b8c5fbf44f9.svg'
AUTHOR = 'gpt-6'


class MonkeyHead(Solo48):
    icon_id = 'monkey-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('monkey', 'head', 'animal')

    def build(self) -> None:
        # HRECT_XL: authored to its exact SOLO48 centerline bounds.
        self.add_arc('skull-left', (8, 21), (24, 5), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('skull-right', (24, 5), (40, 21), radius_x=16, radius_y=16, sweep=True)
        self.add_line('wall-right', (40, 21), (40, 33))
        self.add_line('cheek-right', (40, 33), (40, 35))
        self.add_line('wall-left', (8, 33), (8, 21))
        self.add_line('cheek-left', (8, 35), (8, 33))
        self.add_contour('skull', 'cheek-left', 'wall-left', 'skull-left', 'skull-right', 'wall-right', 'cheek-right', closed=False)
        self.add_arc('ear-left', (8, 21), (8, 33), radius_x=6, radius_y=6, sweep=False)
        self.add_arc('ear-right', (40, 21), (40, 33), radius_x=6, radius_y=6, sweep=True)
        self.relate("connect", 'skull', 'ear-left')
        self.relate("connect", 'skull', 'ear-right')
        self.add_arc('muzzle-left-top', (8, 35), (15, 29), radius_x=7, radius_y=6, sweep=True)
        self.add_arc('muzzle-left-crown', (15, 29), (24, 27), radius_x=9, radius_y=2, sweep=True)
        self.add_arc('muzzle-right-crown', (24, 27), (33, 29), radius_x=9, radius_y=2, sweep=True)
        self.add_arc('muzzle-right-top', (33, 29), (40, 35), radius_x=7, radius_y=6, sweep=True)
        self.add_arc('muzzle-right-low', (40, 35), (24, 43), radius_x=16, radius_y=8, sweep=True)
        self.add_arc('muzzle-left-low', (24, 43), (8, 35), radius_x=16, radius_y=8, sweep=True)
        self.add_contour('muzzle', 'muzzle-left-top', 'muzzle-left-crown', 'muzzle-right-crown', 'muzzle-right-top', 'muzzle-right-low', 'muzzle-left-low', closed=True)
        self.relate("connect", 'muzzle', 'skull')
        self.add_line('mask-left', (15, 29), (15, 21))
        self.add_arc('brow-left', (15, 21), (24, 19), radius_x=5, radius_y=6, sweep=True)
        self.add_arc('brow-right', (24, 19), (33, 21), radius_x=5, radius_y=6, sweep=True)
        self.add_line('mask-right', (33, 21), (33, 29))
        self.add_contour('mask', 'mask-left', 'brow-left', 'brow-right', 'mask-right', closed=False)
        self.relate("connect", 'mask', 'muzzle')
