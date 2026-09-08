"""Right-facing eagle head with hooked beak and feather hem; extremes (2,5)-(46,43). Broad rounded crown; directional asymmetry retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4eec1cf-c3e3-4378-acb6-422b50d1da15'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird eagle_a4eec1cf-c3e3-4378-acb6-422b50d1da15.svg'
AUTHOR = 'gpt-6'


class EagleHead(Solo48):
    icon_id = 'eagle-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('eagle', 'head', 'profile', 'beak', 'hawk', 'raptor', 'bird', 'wildlife')

    def build(self) -> None:
        self.add_line('tuft', (2, 5), (25, 5))
        self.add_arc('crown', (25, 5), (36, 16), radius_x=11, radius_y=11, sweep=True)
        self.add_arc('face', (36, 16), (32, 26), radius_x=14, radius_y=14, sweep=True)
        self.add_line('neck', (32, 26), (32, 37))
        self.add_arc('hem-right', (32, 37), (24, 43), radius_x=8, radius_y=6, sweep=True)
        self.add_line('feathers-1', (24, 43), (19, 39))
        self.add_line('feathers-2', (19, 39), (14, 43))
        self.add_line('feathers-3', (14, 43), (9, 39))
        self.add_line('feathers-4', (9, 39), (4, 43))
        self.add_line('feathers-5', (4, 43), (4, 19))
        self.add_line('feathers-6', (4, 19), (8, 13))
        self.add_line('feathers-7', (8, 13), (2, 5))
        self.add_contour('head', 'tuft', 'crown', 'face', 'neck', 'hem-right', 'feathers-1', 'feathers-2', 'feathers-3', 'feathers-4', 'feathers-5', 'feathers-6', 'feathers-7', closed=True)
        self.add_arc('beak-outer', (36, 16), (46, 30), radius_x=10, radius_y=14, sweep=True)
        self.add_arc('beak-inner', (46, 30), (32, 26), radius_x=14, radius_y=8, sweep=False)
        self.add_contour('beak', 'beak-outer', 'beak-inner', closed=False)
        self.relate("connect", 'beak', 'head')
