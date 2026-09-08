"""Diagonally drifting jellyfish with three trailing tentacles. Centerline extremes (2,2)-(46,46). No useful exact Lucide match. Intentional diagonal pose follows the source; no decorative features."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef0702b0-d65f-5955-8954-f383064a984c'
SOURCE_PATH = 'pictographic-primitives/animals/jellyfish_ef0702b0-d65f-5955-8954-f383064a984c.svg'
AUTHOR = 'gpt-6'


class DriftingJellyfish(Solo48):
    icon_id = 'drifting-jellyfish'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('jellyfish', 'drift', 'sea', 'ocean', 'marine', 'tentacles', 'bell', 'swim')

    def build(self) -> None:
        self.add_arc('bell-top', (14, 6), (26, 2), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('bell-right', (26, 2), (46, 22), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('bell-bottom', (46, 22), (38, 38), radius_x=20, radius_y=20, sweep=True)
        self.add_line('rim-0', (38, 38), (32, 30))
        self.add_line('rim-1', (32, 30), (26, 22))
        self.add_line('rim-2', (26, 22), (20, 14))
        self.add_line('rim-3', (20, 14), (14, 6))
        self.add_contour('bell', 'bell-top', 'bell-right', 'bell-bottom', 'rim-0', 'rim-1', 'rim-2', 'rim-3', closed=True)
        self.add_arc('tentacle-0', (20, 14), (2, 29), radius_x=40, radius_y=40, sweep=True)
        self.relate("connect", 'bell', 'tentacle-0')
        self.add_arc('tentacle-1', (26, 22), (10, 39), radius_x=40, radius_y=40, sweep=True)
        self.relate("connect", 'bell', 'tentacle-1')
        self.add_arc('tentacle-2', (32, 30), (20, 46), radius_x=40, radius_y=40, sweep=True)
        self.relate("connect", 'bell', 'tentacle-2')
