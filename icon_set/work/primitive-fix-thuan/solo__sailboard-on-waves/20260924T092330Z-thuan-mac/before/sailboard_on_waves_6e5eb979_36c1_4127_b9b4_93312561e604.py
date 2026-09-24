"""Sailboard on Waves. Leaning mast and curved sail above a raised board nose; omit paired sail stripes and reduce water to one wave row.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: a sparse sail and board hierarchy. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e5eb979-36c1-4127-b9b4-93312561e604'
SOURCE_PATH = 'pictographic-primitives/recreation/nautic sports sailing_6e5eb979-36c1-4127-b9b4-93312561e604.svg'
AUTHOR = 'gpt-6'


class SailboardOnWaves(Solo48):
    icon_id = 'sailboard-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('sailboard', 'on', 'waves')

    def build(self) -> None:
        self.add_arc('sail-curve', (19, 6), (9, 22), radius_x=28, radius_y=28, sweep=False)
        self.add_line('sail-base-1', (9, 22), (27, 22))
        self.add_line('sail-base-2', (27, 22), (19, 6))
        self.add_contour('sail', 'sail-curve', 'sail-base-1', 'sail-base-2', closed=True)
        self.add_line('mast', (27, 22), (31, 31))
        self.relate("connect", 'sail', 'mast')
        self.add_line('board-1', (6, 31), (31, 31))
        self.add_line('board-2', (31, 31), (42, 27))
        self.add_contour('board', 'board-1', 'board-2', closed=False)
        self.relate("connect", 'mast', 'board')
        self.add_arc('wave-left', (6, 40), (24, 40), radius_x=9, radius_y=2, sweep=False)
        self.add_arc('wave-right', (24, 40), (42, 40), radius_x=9, radius_y=2, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-right', closed=False)
