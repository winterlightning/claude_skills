"""Round hand fan with diagonal handle and one rib. Extrema (2,2)-(46,46). Paddle retained from supplied image; no useful Lucide subject match. Diagonal pose is intentional."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7be3733e-dd31-5735-a409-964d8f89d37b'
SOURCE_PATH = 'pictographic-primitives/animals/ray_7be3733e-dd31-5735-a409-964d8f89d37b.svg'
AUTHOR = 'gpt-6'


class RoundHandFan(Solo48):
    icon_id = 'round-hand-fan'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/household'
    aliases = ()
    keywords = ('fan', 'hand fan', 'uchiwa', 'handle', 'cooling', 'japanese', 'round', 'paddle')

    def build(self) -> None:
        # Round hand fan with diagonal handle and one rib. Extrema (2,2)-(46,46). Paddle retained from supplied image; no useful Lucide subject match. Diagonal pose is intentional.
        self.add_arc('blade-upper-left', (14, 12), (32, 2), radius_x=18, radius_y=10, sweep=True)
        self.add_arc('blade-upper-right', (32, 2), (46, 18), radius_x=14, radius_y=16, sweep=True)
        self.add_arc('blade-lower-right', (46, 18), (32, 36), radius_x=14, radius_y=18, sweep=True)
        self.add_arc('blade-tip', (32, 36), (25, 34), radius_x=8, radius_y=8, sweep=True)
        self.add_line('blade-bottom', (25, 34), (20, 29))
        self.add_line('blade-bottom-left', (20, 29), (14, 23))
        self.add_arc('blade-left', (14, 23), (14, 12), radius_x=9, radius_y=9, sweep=True)
        self.add_contour('blade', 'blade-upper-left', 'blade-upper-right', 'blade-lower-right', 'blade-tip', 'blade-bottom', 'blade-bottom-left', 'blade-left')
        self.add_line('handle', (2, 46), (20, 29))
        self.add_line('rib', (20, 29), (30, 16))
        self.add_contour('shaft', 'handle', 'rib')
        self.relate("connect", 'shaft', 'blade')
