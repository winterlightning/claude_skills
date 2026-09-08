"""Eagle head; centerline extremes (2,2)-(46,46). Hooked beak and three feather tips retained; beak slit omitted. Lucide bird informs continuous crown; right-facing asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17ad6602-c748-513a-a410-1c550f7c60d8'
SOURCE_PATH = 'pictographic-primitives/animals/indian eagle_17ad6602-c748-513a-a410-1c550f7c60d8.svg'
AUTHOR = 'gpt-6'


class EagleHeadProfile(Solo48):
    icon_id = 'eagle-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('eagle', 'head', 'profile', 'beak', 'bird', 'raptor', 'feathers', 'wildlife')

    def build(self) -> None:
        # Eagle head; centerline extremes (2,2)-(46,46). Hooked beak and three feather tips retained; beak slit omitted. Lucide bird informs continuous crown; right-facing asymmetry.
        self.add_arc('crown-left', (2, 24), (24, 2), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('crown-right', (24, 2), (37, 9), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('beak-top', (37, 9), (46, 22), radius_x=9, radius_y=13, sweep=True)
        self.add_arc('throat', (39, 23), (33, 32), radius_x=10, radius_y=10, sweep=False)
        self.add_line('beak-hook-1', (46, 22), (46, 28))
        self.add_line('beak-hook-2', (46, 28), (39, 23))
        self.add_line('feathers-1', (33, 32), (38, 42))
        self.add_line('feathers-2', (38, 42), (24, 36))
        self.add_line('feathers-3', (24, 36), (23, 46))
        self.add_line('feathers-4', (23, 46), (14, 34))
        self.add_line('feathers-5', (14, 34), (6, 40))
        self.add_line('feathers-6', (6, 40), (8, 24))
        self.add_line('feathers-7', (8, 24), (2, 24))
        self.add_contour('outline', 'crown-left', 'crown-right', 'beak-top', 'beak-hook-1', 'beak-hook-2', 'throat', 'feathers-1', 'feathers-2', 'feathers-3', 'feathers-4', 'feathers-5', 'feathers-6', 'feathers-7', closed=True)
        self.add_line('brow', (23, 14), (31, 16))
