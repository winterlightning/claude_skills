"""Hyena profile; centerline extremes (2,8)-(46,40). Broad muzzle and ear retained; loose mane reduced. Deliberately right-facing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '753d11ca-ec60-486c-857b-55d44895af07'
SOURCE_PATH = 'pictographic-primitives/animals/hyena head side_753d11ca-ec60-486c-857b-55d44895af07.svg'
AUTHOR = 'gpt-6'


class HyenaHeadProfile(Solo48):
    icon_id = 'hyena-head-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('hyena', 'head', 'profile', 'side', 'snout', 'ear', 'animal', 'wildlife')

    def build(self) -> None:
        # Hyena profile; centerline extremes (2,8)-(46,40). Broad muzzle and ear retained; loose mane reduced. Deliberately right-facing.
        self.add_arc('forehead', (25, 18), (35, 25), radius_x=13, radius_y=13, sweep=True)
        self.add_line('snout', (35, 25), (46, 29))
        self.add_arc('nose', (46, 29), (39, 36), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('neck', (22, 34), (10, 40), radius_x=18, radius_y=18, sweep=False)
        self.add_line('mane-1', (2, 16), (10, 16))
        self.add_line('mane-2', (10, 16), (6, 8))
        self.add_line('mane-3', (6, 8), (19, 13))
        self.add_line('mane-4', (19, 13), (23, 8))
        self.add_line('mane-5', (23, 8), (25, 18))
        self.add_line('mouth-1', (39, 36), (30, 31))
        self.add_line('mouth-2', (30, 31), (33, 40))
        self.add_line('mouth-3', (33, 40), (22, 34))
        self.add_contour('profile', 'mane-1', 'mane-2', 'mane-3', 'mane-4', 'mane-5', 'forehead', 'snout', 'nose', 'mouth-1', 'mouth-2', 'mouth-3', 'neck', closed=False)
        self.add_dot('eye', (27, 25))
