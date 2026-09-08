"""Mirrored hippo face with round ears and broad muzzle; eyes and nostrils reduced to one pair of sparse marks. Lucide dog informs facial reduction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa6b0258-1bc2-51ef-819c-45e3b36a42d4'
SOURCE_PATH = 'pictographic-primitives/animals/hippo_fa6b0258-1bc2-51ef-819c-45e3b36a42d4.svg'
AUTHOR = 'gpt-6'


class HippoFace(Solo48):
    icon_id = 'hippo-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('hippo', 'hippopotamus', 'face', 'head', 'muzzle', 'ears', 'animal', 'cute')

    def build(self) -> None:
        # Keyshape ink extremes: (0, 0, 48, 48); centerlines inset by stroke radius 2.
        self.add_line('head-1', (6, 22), (2, 8))
        self.add_arc('head-2', (2, 8), (8, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('head-3', (8, 2), (15, 9), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('head-4', (15, 9), (24, 7), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('head-5', (24, 7), (33, 9), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('head-6', (33, 9), (40, 2), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('head-7', (40, 2), (46, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('head-8', (46, 8), (42, 22))
        self.add_arc('head-9', (42, 22), (46, 34), radius_x=4, radius_y=12, sweep=True)
        self.add_arc('head-10', (46, 34), (34, 46), radius_x=12, radius_y=12, sweep=True)
        self.add_line('head-11', (34, 46), (14, 46))
        self.add_arc('head-12', (14, 46), (2, 34), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('head-13', (2, 34), (6, 22), radius_x=4, radius_y=12, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', 'head-5', 'head-6', 'head-7', 'head-8', 'head-9', 'head-10', 'head-11', 'head-12', 'head-13', closed=True)
        self.add_line('muzzle-1', (16, 25), (32, 25))
        self.add_arc('muzzle-2', (32, 25), (39, 32), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('muzzle-3', (39, 32), (32, 39), radius_x=7, radius_y=7, sweep=True)
        self.add_line('muzzle-4', (32, 39), (16, 39))
        self.add_arc('muzzle-5', (16, 39), (9, 32), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('muzzle-6', (9, 32), (16, 25), radius_x=7, radius_y=7, sweep=True)
        self.add_contour('muzzle', 'muzzle-1', 'muzzle-2', 'muzzle-3', 'muzzle-4', 'muzzle-5', 'muzzle-6', closed=True)
        self.add_dot('nostril-left', (19, 32))
        self.add_dot('nostril-right', (29, 32))
