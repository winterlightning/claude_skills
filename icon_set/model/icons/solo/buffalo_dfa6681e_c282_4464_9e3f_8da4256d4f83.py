"""Front-facing buffalo with upturned horns and rounded muzzle. Matched circular horn lobes; ears omitted to keep the heavy horns distinct. No useful exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfa6681e-c282-4464-9e3f-8da4256d4f83'
SOURCE_PATH = 'pictographic-primitives/animals/buffalo_dfa6681e-c282-4464-9e3f-8da4256d4f83.svg'
AUTHOR = 'gpt-6'


class BuffaloHead(Solo48):
    icon_id = 'buffalo-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('buffalo', 'bison', 'head', 'horns', 'cattle', 'animal', 'wildlife', 'ox')

    def build(self) -> None:
        # HRECT_XL centerline extremes recorded in batch-02-review.md.
        self.add_arc('horn-left-outer', (2, 5), (14, 23), radius_x=12, radius_y=18, sweep=False)
        self.add_arc('brow-left', (14, 23), (24, 19), radius_x=14, radius_y=10, sweep=False)
        self.add_arc('brow-right', (24, 19), (34, 23), radius_x=14, radius_y=10, sweep=False)
        self.add_arc('horn-right-outer', (34, 23), (46, 5), radius_x=12, radius_y=18, sweep=False)
        self.add_contour('horns', 'horn-left-outer', 'brow-left', 'brow-right', 'horn-right-outer', closed=False)
        self.add_line('face-left', (14, 23), (17, 38))
        self.add_arc('jaw-left', (17, 38), (22, 43), radius_x=5, radius_y=5, sweep=True)
        self.add_line('chin', (22, 43), (26, 43))
        self.add_arc('jaw-right', (26, 43), (31, 38), radius_x=5, radius_y=5, sweep=True)
        self.add_line('face-right', (31, 38), (34, 23))
        self.add_contour('face', 'face-left', 'jaw-left', 'chin', 'jaw-right', 'face-right', closed=False)
        self.relate("connect", 'face', 'horns')
        self.add_line('muzzle', (16, 33), (32, 33))
        self.relate("connect", 'face', 'muzzle')
