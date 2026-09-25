"""Kitesurfer. Rider balances below a crescent kite joined by a tether; omit canopy divisions and doubled line.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: a coherent fabric silhouette; person-standing: sparse limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '914bc957-ebe3-53b4-b39f-e54b2676e845'
SOURCE_PATH = 'pictographic-primitives/recreation/sport kitesurfing_914bc957-ebe3-53b4-b39f-e54b2676e845.svg'
AUTHOR = 'gpt-6'


class Kitesurfer(Solo48):
    icon_id = 'kitesurfer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    aliases = ()
    keywords = ('kitesurfer',)

    def build(self) -> None:
        self.add_arc('canopy-outer', (6, 24), (30, 24), radius_x=12, radius_y=18, sweep=True)
        self.add_arc('canopy-inner', (30, 24), (6, 24), radius_x=12, radius_y=5, sweep=False)
        self.add_contour('kite', 'canopy-outer', 'canopy-inner', closed=True)
        self.add_line('tether-1', (30, 24), (37, 29))
        self.add_contour('tether', 'tether-1', closed=False)
        self.relate("connect", 'kite', 'tether')
        self.add_arc('head-top', (38, 14), (42, 14), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('head-bottom', (42, 14), (38, 14), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('rider-1', (37, 29), (35, 35))
        self.add_line('rider-2', (35, 35), (30, 42))
        self.add_contour('rider', 'rider-1', 'rider-2', closed=False)
        self.relate("connect", 'rider', 'tether')
        self.add_line('board-1', (26, 42), (30, 42))
        self.add_line('board-2', (30, 42), (40, 42))
        self.add_line('board-3', (40, 42), (42, 42))
        self.add_contour('board', 'board-1', 'board-2', 'board-3', closed=False)
        self.relate("connect", 'board', 'rider')
