"""Mirrored hyena face with large rounded ears, slanted brows and tapering muzzle; tiny W mouth reduced to short nose. Lucide cat/dog guide ear and jaw contours."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f38e4453-f8b7-421c-a515-5872890a9484'
SOURCE_PATH = 'pictographic-primitives/animals/hyena head front_f38e4453-f8b7-421c-a515-5872890a9484.svg'
AUTHOR = 'gpt-6'


class HyenaHeadFront(Solo48):
    icon_id = 'hyena-head-front'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('hyena', 'head', 'face', 'front', 'ears', 'muzzle', 'animal', 'wildlife')

    def build(self) -> None:
        # Keyshape ink extremes: (0, 0, 48, 48); centerlines inset by stroke radius 2.
        self.add_line('head-1', (8, 21), (2, 14))
        self.add_line('head-2', (2, 14), (2, 8))
        self.add_arc('head-3', (2, 8), (8, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('head-4', (8, 2), (16, 10), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('head-5', (16, 10), (24, 9), radius_x=24, radius_y=24, sweep=True)
        self.add_arc('head-6', (24, 9), (32, 10), radius_x=24, radius_y=24, sweep=True)
        self.add_arc('head-7', (32, 10), (40, 2), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('head-8', (40, 2), (46, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('head-9', (46, 8), (46, 14))
        self.add_line('head-10', (46, 14), (40, 21))
        self.add_line('head-11', (40, 21), (38, 29))
        self.add_line('head-12', (38, 29), (32, 37))
        self.add_line('head-13', (32, 37), (30, 43))
        self.add_arc('head-14', (30, 43), (24, 46), radius_x=7, radius_y=6, sweep=True)
        self.add_arc('head-15', (24, 46), (18, 43), radius_x=7, radius_y=6, sweep=True)
        self.add_line('head-16', (18, 43), (16, 37))
        self.add_line('head-17', (16, 37), (10, 29))
        self.add_line('head-18', (10, 29), (8, 21))
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', 'head-5', 'head-6', 'head-7', 'head-8', 'head-9', 'head-10', 'head-11', 'head-12', 'head-13', 'head-14', 'head-15', 'head-16', 'head-17', 'head-18', closed=True)
        self.add_line('brow-left', (15, 22), (19, 24))
        self.add_line('brow-right', (33, 22), (29, 24))
        self.add_line('nose', (22, 35), (26, 35))
