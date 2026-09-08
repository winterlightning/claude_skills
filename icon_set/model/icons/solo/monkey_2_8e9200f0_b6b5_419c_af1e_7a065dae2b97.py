"""Monkey face with a broad rounded forehead panel and a softly narrowed lower muzzle. Restored large round ears and lower muzzle proportions from the supplied source. Small mouth line omitted; mirrored about x=24. Lucide cat informs smooth paired skull arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e9200f0-b6b5-419c-af1e-7a065dae2b97'
SOURCE_PATH = 'pictographic-primitives/animals/monkey 2_8e9200f0-b6b5-419c-af1e-7a065dae2b97.svg'
AUTHOR = 'gpt-6'


class MonkeyFace(Solo48):
    icon_id = 'monkey-face'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('monkey', 'face', 'animal')

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
        self.add_arc('chin-right', (40, 35), (24, 43), radius_x=16, radius_y=8, sweep=True)
        self.add_arc('chin-left', (24, 43), (8, 35), radius_x=16, radius_y=8, sweep=True)
        self.add_contour('chin', 'chin-right', 'chin-left', closed=False)
        self.relate("connect", 'chin', 'skull')
        self.add_arc('panel-left-top', (15, 23), (22, 16), radius_x=7, radius_y=7, sweep=True)
        self.add_line('panel-top', (22, 16), (26, 16))
        self.add_arc('panel-right-top', (26, 16), (33, 23), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('panel-right', (33, 23), (31, 29), radius_x=10, radius_y=10, sweep=True)
        self.add_line('muzzle-right', (31, 29), (31, 34))
        self.add_arc('muzzle-bottom', (31, 34), (17, 34), radius_x=9, radius_y=2, sweep=True)
        self.add_line('muzzle-left', (17, 34), (17, 29))
        self.add_arc('panel-left', (17, 29), (15, 23), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('panel', 'panel-left-top', 'panel-top', 'panel-right-top', 'panel-right', 'muzzle-right', 'muzzle-bottom', 'muzzle-left', 'panel-left', closed=True)
