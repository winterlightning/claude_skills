"""Rooster profile with two-lobed comb and pointed wattle. Lucide bird informs simple head arc and eye. Centerline (2,2)-(46,46); the beak is integrated into the outline to preserve its opening."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '221f89e4-4362-5f43-aa0a-e270a4269e65'
SOURCE_PATH = 'pictographic-primitives/animals/rooster_221f89e4-4362-5f43-aa0a-e270a4269e65.svg'
AUTHOR = 'gpt-6'


class RoosterHead(Solo48):
    icon_id = 'rooster-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('rooster', 'cockerel', 'head', 'comb', 'wattle', 'beak', 'farm', 'poultry')

    def build(self) -> None:
        self.add_line('head-1', (2, 46), (2, 31))
        self.add_arc('head-2', (2, 31), (19, 14), radius_x=17, radius_y=17, sweep=True)
        self.add_arc('head-3', (19, 14), (33, 22), radius_x=17, radius_y=17, sweep=True)
        self.add_line('head-4', (33, 22), (46, 35))
        self.add_line('head-5', (46, 35), (36, 35))
        self.add_arc('head-6', (36, 35), (32, 46), radius_x=7, radius_y=9, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', 'head-5', 'head-6', closed=False)
        self.add_arc('comb-1', (14, 16), (12, 8), radius_x=9, radius_y=9, sweep=True)
        self.add_arc('comb-2', (12, 8), (18, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('comb-3', (18, 2), (24, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('comb-4', (24, 8), (36, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('comb-5', (36, 8), (32, 18), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('comb', 'comb-1', 'comb-2', 'comb-3', 'comb-4', 'comb-5', closed=False)
        self.relate("connect", 'head', 'comb')
        self.add_dot('eye', (25, 27))
