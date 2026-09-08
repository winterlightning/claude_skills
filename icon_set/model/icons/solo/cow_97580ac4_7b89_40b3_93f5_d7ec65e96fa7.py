"""Symmetric cow head with broad muzzle and sweeping open ears. Paired arcs use shared mirrored dimensions; eyes omitted as in the source. No useful local Lucide cow match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97580ac4-7b89-40b3-93f5-d7ec65e96fa7'
SOURCE_PATH = 'pictographic-primitives/animals/cow_97580ac4-7b89-40b3-93f5-d7ec65e96fa7.svg'
AUTHOR = 'gpt-6'


class CowHeadWithHorns(Solo48):
    icon_id = 'cow-head-with-horns'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('cow', 'cattle', 'head', 'horns', 'muzzle', 'farm', 'bovine', 'dairy')

    def build(self) -> None:
        # Visible bounds: (0, 0, 48, 48); centerline inset 2.
        self.add_arc('crown', (14, 16), (34, 16), radius_x=10, radius_y=8, sweep=True)
        self.add_line('cheek-left', (14, 16), (16, 37))
        self.add_line('cheek-right', (34, 16), (32, 37))
        self.add_arc('muzzle-bottom', (32, 37), (16, 37), radius_x=8, radius_y=9, sweep=True)
        self.add_contour('head', 'cheek-left', closed=False)
        self.add_contour('right', 'cheek-right', 'muzzle-bottom', closed=False)
        self.relate("connect", 'crown', 'head')
        self.relate("connect", 'crown', 'right')
        self.relate("connect", 'head', 'right')
        self.add_arc('muzzle-top', (16, 37), (32, 37), radius_x=8, radius_y=5, sweep=True)
        self.relate("connect", 'muzzle-top', 'head')
        self.relate("connect", 'muzzle-top', 'right')
        self.add_arc('horn-left', (24, 8), (5, 2), radius_x=19, radius_y=6, sweep=True)
        self.relate("connect", 'horn-left', 'crown')
        self.add_arc('ear-left', (14, 16), (2, 26), radius_x=12, radius_y=10, sweep=True)
        self.relate("connect", 'ear-left', 'crown')
        self.relate("connect", 'ear-left', 'head')
        self.add_arc('horn-right', (24, 8), (43, 2), radius_x=19, radius_y=6, sweep=False)
        self.relate("connect", 'horn-right', 'crown')
        self.add_arc('ear-right', (34, 16), (46, 26), radius_x=12, radius_y=10, sweep=False)
        self.relate("connect", 'ear-right', 'crown')
        self.relate("connect", 'ear-right', 'right')
