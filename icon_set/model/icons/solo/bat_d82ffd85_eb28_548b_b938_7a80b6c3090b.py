"""Bat with paired ears and scalloped wings; centerline extremes (2,8)-(46,40). Mirrored silhouette; tiny wing notches omitted. No useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd82ffd85-eb28-548b-b938-7a80b6c3090b'
SOURCE_PATH = 'pictographic-primitives/animals/bat_d82ffd85-eb28-548b-b938-7a80b6c3090b.svg'
AUTHOR = 'gpt-6'


class Bat(Solo48):
    icon_id = 'bat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('bat', 'wings', 'flying', 'halloween', 'night', 'animal', 'nocturnal', 'vampire')

    def build(self) -> None:
        # Bat with paired ears and scalloped wings; centerline extremes (2,8)-(46,40). Mirrored silhouette; tiny wing notches omitted. No useful Lucide match.
        self.add_line('ears-1', (18, 19), (17, 8))
        self.add_line('ears-2', (17, 8), (24, 12))
        self.add_line('ears-3', (24, 12), (31, 8))
        self.add_line('ears-4', (31, 8), (30, 19))
        self.add_arc('right-shoulder', (30, 19), (38, 11), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('right-wing', (38, 11), (46, 33), radius_x=8, radius_y=22, sweep=True)
        self.add_arc('right-scallop', (46, 33), (34, 33), radius_x=8, radius_y=6, sweep=False)
        self.add_arc('right-base', (34, 33), (24, 40), radius_x=10, radius_y=7, sweep=False)
        self.add_arc('left-base', (24, 40), (14, 33), radius_x=10, radius_y=7, sweep=False)
        self.add_arc('left-scallop', (14, 33), (2, 33), radius_x=8, radius_y=6, sweep=False)
        self.add_arc('left-wing', (2, 33), (10, 11), radius_x=8, radius_y=22, sweep=True)
        self.add_arc('left-shoulder', (10, 11), (18, 19), radius_x=8, radius_y=8, sweep=False)
        self.add_contour('bat-outline', 'ears-1', 'ears-2', 'ears-3', 'ears-4', 'right-shoulder', 'right-wing', 'right-scallop', 'right-base', 'left-base', 'left-scallop', 'left-wing', 'left-shoulder', closed=True)
