"""Film Reel. Keeps four diamond-arranged dots and a tangent bottom tail; no extra hub detail.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85b4e864-aa1e-440d-9e8f-3d5759c16845'
SOURCE_PATH = 'pictographic-primitives/symbol/clipper board_85b4e864-aa1e-440d-9e8f-3d5759c16845.svg'
AUTHOR = 'gpt-6'


class FilmReel(Solo48):
    icon_id = 'film-reel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('film', 'reel', 'movie', 'cinema', 'video', 'tape', 'recording', 'spool')

    def build(self) -> None:
        self.add_arc('reel-right', (24, 6), (24, 42), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('reel-left', (24, 42), (24, 6), radius_x=18, radius_y=18, sweep=True)
        self.add_contour('reel', 'reel-right', 'reel-left', closed=True)
        self.add_line('film-tail', (24, 42), (42, 42))
        self.relate("connect", 'reel', 'film-tail')
        self.add_dot('top', (24, 15))
        self.add_dot('right', (33, 24))
        self.add_dot('bottom', (24, 33))
        self.add_dot('left', (15, 24))
