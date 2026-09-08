"""Right-facing beetle with a capsule shell and a broad hooked horn. Centerline extremes (2,8)-(46,40). Lucide bug informs attached legs; profile asymmetry preserves the source. No tiny eye or shell texture."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b5ef71c-5aa8-4146-809d-f56369f47fe4'
SOURCE_PATH = 'pictographic-primitives/animals/insect_3b5ef71c-5aa8-4146-809d-f56369f47fe4.svg'
AUTHOR = 'gpt-6'


class StagBeetle(Solo48):
    icon_id = 'stag-beetle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('stag beetle', 'beetle', 'insect', 'horn', 'bug', 'shell', 'profile', 'nature')

    def build(self) -> None:
        self.add_arc('shell-back', (12, 32), (12, 16), radius_x=10, radius_y=8, sweep=True)
        self.add_line('shell-top', (12, 16), (28, 16))
        self.add_line('shell-front', (28, 16), (28, 32))
        self.add_line('belly-front', (28, 32), (24, 32))
        self.add_line('belly-middle', (24, 32), (14, 32))
        self.add_line('belly-back', (14, 32), (12, 32))
        self.add_contour('shell', 'shell-back', 'shell-top', 'shell-front', 'belly-front', 'belly-middle', 'belly-back', closed=True)
        self.add_arc('head-rise', (28, 16), (38, 8), radius_x=10, radius_y=8, sweep=True)
        self.add_arc('horn-inner', (38, 8), (46, 20), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('head-front', (46, 20), (34, 32), radius_x=12, radius_y=12, sweep=True)
        self.add_line('head-base', (34, 32), (28, 32))
        self.add_contour('head', 'head-rise', 'horn-inner', 'head-front', 'head-base', closed=False)
        self.relate("connect", 'shell', 'head')
        self.add_arc('leg-0', (14, 32), (10, 40), radius_x=10, radius_y=10, sweep=True)
        self.relate("connect", 'shell', 'leg-0')
        self.add_arc('leg-1', (34, 32), (38, 40), radius_x=10, radius_y=10, sweep=False)
        self.relate("connect", 'head', 'leg-1')
