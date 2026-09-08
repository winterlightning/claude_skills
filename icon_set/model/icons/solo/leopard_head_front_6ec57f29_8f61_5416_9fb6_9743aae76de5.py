"""Cheetah face with rounded ears and paired tear marks. Lucide cat informs mirrored head construction. Nose reduced to an open chevron ; mouth omitted for clearance; cheek marks carry species identity."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ec57f29-8f61-5416-9fb6-9743aae76de5'
SOURCE_PATH = 'pictographic-primitives/animals/leopard head front_6ec57f29-8f61-5416-9fb6-9743aae76de5.svg'
AUTHOR = 'gpt-6'


class CheetahFace(Solo48):
    icon_id = 'cheetah-face'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('cheetah', 'leopard', 'face', 'head', 'big cat', 'tear marks', 'feline', 'wildlife')

    def build(self) -> None:
        # Exact visible extremes: (0, 3, 48, 45); centerline inset 2.
        self.add_arc('crown', (14, 10), (34, 10), radius_x=18, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('ear-right-top', (34, 10), (40, 5), radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('ear-right-round', (40, 5), (46, 11), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('ear-right-side', (46, 11), (42, 17), radius_x=4, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('cheek-right', (42, 17), (24, 43), radius_x=18, radius_y=26, sweep=True, large_arc=False)
        self.add_arc('cheek-left', (24, 43), (6, 17), radius_x=18, radius_y=26, sweep=True, large_arc=False)
        self.add_arc('ear-left-side', (6, 17), (2, 11), radius_x=4, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('ear-left-round', (2, 11), (8, 5), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('ear-left-top', (8, 5), (14, 10), radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('outline', 'crown', 'ear-right-top', 'ear-right-round', 'ear-right-side', 'cheek-right', 'cheek-left', 'ear-left-side', 'ear-left-round', 'ear-left-top', closed=True)
        self.add_line('eye-left', (13, 19), (17, 19))
        self.add_arc('tear-left', (17, 19), (15, 29), radius_x=9, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('mark-left', 'eye-left', 'tear-left', closed=False)
        self.add_line('eye-right', (35, 19), (31, 19))
        self.add_arc('tear-right', (31, 19), (33, 29), radius_x=9, radius_y=10, sweep=False, large_arc=False)
        self.add_contour('mark-right', 'eye-right', 'tear-right', closed=False)
        self.add_polyline('nose', (21, 32), (24, 35), (27, 32))
