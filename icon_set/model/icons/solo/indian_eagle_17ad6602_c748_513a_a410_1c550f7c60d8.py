"""Eagle head; centerline extremes (6,6)-(42,42). Hooked beak and three feather tips retained; beak slit omitted. Lucide bird informs continuous crown; right-facing asymmetry."""
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
    category = "animals"
    aliases = ()
    keywords = ('eagle', 'head', 'profile', 'beak', 'bird', 'raptor', 'feathers', 'wildlife')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('crown-left', (6, 24), (24, 6), radius_x=22, radius_y=22, large_arc=False, sweep=True)
        self.add_bezier('crown-right', (24, 6), *(((28.56344039, 6), (33.31019002, 6.154836), (37, 9)),))
        self.add_bezier('beak-top', (37, 9), *(((40.38747008, 11.39251246), (42, 16.58158672), (42, 22)),))
        self.add_arc('throat', (39, 23), (33, 32), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('beak-hook-1', (42, 22), (42, 28))
        self.add_line('beak-hook-2', (42, 28), (39, 23))
        self.add_line('feathers-1', (33, 32), (38, 42))
        self.add_line('feathers-2', (38, 42), (24, 36))
        self.add_line('feathers-3', (24, 36), (23, 42))
        self.add_line('feathers-4', (23, 42), (14, 34))
        self.add_line('feathers-5', (14, 34), (6, 40))
        self.add_line('feathers-6', (6, 40), (8, 24))
        self.add_line('feathers-7', (8, 24), (6, 24))
        self.add_line('brow', (23, 15), (31, 17))
        self.add_contour('outline', *('crown-left', 'crown-right', 'beak-top', 'beak-hook-1', 'beak-hook-2', 'throat', 'feathers-1', 'feathers-2', 'feathers-3', 'feathers-4', 'feathers-5', 'feathers-6', 'feathers-7'), closed=True)
