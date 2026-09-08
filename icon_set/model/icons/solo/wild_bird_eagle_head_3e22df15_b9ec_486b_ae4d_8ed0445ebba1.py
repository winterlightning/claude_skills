"""Front eagle head with scalloped feather hem and centered beak; extremes (2,2)-(46,46). Mirrored dome and brow strokes; three broad scallops replace small feather repetitions."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e22df15-b9ec-486b-ae4d-8ed0445ebba1'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird eagle head_3e22df15-b9ec-486b-ae4d-8ed0445ebba1.svg'
AUTHOR = 'gpt-6'


class EagleHeadFront(Solo48):
    icon_id = 'eagle-head-front'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('eagle', 'head', 'front', 'beak', 'feathers', 'raptor', 'bird', 'wildlife')

    def build(self) -> None:
        self.add_arc('dome-left', (4, 23), (24, 2), radius_x=20, radius_y=21, sweep=True)
        self.add_arc('dome-right', (24, 2), (44, 23), radius_x=20, radius_y=21, sweep=True)
        self.add_line('side-right', (44, 23), (46, 40))
        self.add_arc('feather-right', (46, 40), (34, 40), radius_x=6, radius_y=4, sweep=True)
        self.add_line('hem-right', (34, 40), (30, 42))
        self.add_arc('feather-center', (30, 42), (18, 42), radius_x=6, radius_y=4, sweep=True)
        self.add_line('hem-left', (18, 42), (14, 40))
        self.add_arc('feather-left', (14, 40), (2, 40), radius_x=6, radius_y=4, sweep=True)
        self.add_line('side-left', (2, 40), (4, 23))
        self.add_contour('head', 'dome-left', 'dome-right', 'side-right', 'feather-right', 'hem-right', 'feather-center', 'hem-left', 'feather-left', 'side-left', closed=True)
        self.add_line('brow-left', (12, 16), (17, 18))
        self.add_line('brow-right', (31, 18), (36, 16))
        self.add_arc('beak-top', (19, 26), (29, 26), radius_x=5, radius_y=4, sweep=True)
        self.add_line('beak-base-1', (29, 26), (32, 29))
        self.add_line('beak-base-2', (32, 29), (28, 30))
        self.add_line('beak-base-3', (28, 30), (24, 36))
        self.add_line('beak-base-4', (24, 36), (20, 30))
        self.add_line('beak-base-5', (20, 30), (16, 29))
        self.add_line('beak-base-6', (16, 29), (19, 26))
        self.add_contour('beak', 'beak-top', 'beak-base-1', 'beak-base-2', 'beak-base-3', 'beak-base-4', 'beak-base-5', 'beak-base-6', closed=True)
