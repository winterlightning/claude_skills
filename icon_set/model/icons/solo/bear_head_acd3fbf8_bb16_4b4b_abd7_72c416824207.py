"""Bear face, round ears and two eyes; centerline extremes (2,5)-(46,43). Mirrored arcs with a broad rounded chin; no muzzle in source. No useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'acd3fbf8-bb16-4b4b-abd7-72c416824207'
SOURCE_PATH = 'pictographic-primitives/animals/bear head_acd3fbf8-bb16-4b4b-abd7-72c416824207.svg'
AUTHOR = 'gpt-6'


class BearFace(Solo48):
    icon_id = 'bear-face'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('bear', 'face', 'head', 'cute', 'animal', 'teddy', 'wildlife', 'round')

    def build(self) -> None:
        # Bear face, round ears and two eyes; centerline extremes (2,5)-(46,43). Mirrored arcs with a broad rounded chin; no muzzle in source. No useful Lucide match.
        self.add_line('forehead', (16, 11), (32, 11))
        self.add_arc('right-temple', (32, 11), (40, 19), radius_x=8, radius_y=8, sweep=True)
        self.add_line('right-cheek', (40, 19), (40, 27))
        self.add_arc('chin', (40, 27), (8, 27), radius_x=16, radius_y=16, sweep=True)
        self.add_line('left-cheek', (8, 27), (8, 19))
        self.add_arc('left-temple', (8, 19), (16, 11), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('face', 'forehead', 'right-temple', 'right-cheek', 'chin', 'left-cheek', 'left-temple', closed=True)
        self.add_arc('left-ear-lower', (8, 19), (2, 13), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('left-ear-top', (2, 13), (10, 5), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('left-ear-inner', (10, 5), (16, 11), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('left-ear', 'left-ear-lower', 'left-ear-top', 'left-ear-inner', closed=False)
        self.relate("connect", 'left-ear', 'face')
        self.add_arc('right-ear-inner', (32, 11), (38, 5), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('right-ear-top', (38, 5), (46, 13), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('right-ear-lower', (46, 13), (40, 19), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('right-ear', 'right-ear-inner', 'right-ear-top', 'right-ear-lower', closed=False)
        self.relate("connect", 'right-ear', 'face')
        self.add_line('left-eye', (17, 24), (17, 26))
        self.add_line('right-eye', (31, 24), (31, 26))
