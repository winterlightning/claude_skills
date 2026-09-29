"""Windsurfer on Waves. Right-side rider holds the tall left sail; reduce waves to one waterline and omit small sail seam.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: curved sail and shared mast-board attachment. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c92ebca1-ceb1-5013-af58-e27dd7afe2b6'
SOURCE_PATH = 'pictographic-primitives/recreation/sport windsurfing_c92ebca1-ceb1-5013-af58-e27dd7afe2b6.svg'
AUTHOR = 'gpt-6'


class WindsurferOnWaves(Solo48):
    icon_id = 'windsurfer-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('windsurfer', 'on', 'waves')

    def build(self) -> None:
        self.add_arc('sail-edge', (25, 6), (6, 25), radius_x=36, radius_y=36, sweep=False)
        self.add_line('sail-base-1', (6, 25), (22, 25))
        self.add_line('sail-base-2', (22, 25), (25, 6))
        self.add_contour('sail', 'sail-edge', 'sail-base-1', 'sail-base-2', closed=True)
        self.add_line('mast', (22, 25), (20, 34))
        self.relate("connect", 'sail', 'mast')
        self.add_arc('head-top', (35, 12), (39, 12), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('head-bottom', (39, 12), (35, 12), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('person-1', (22, 25), (34, 24))
        self.add_line('person-2', (34, 24), (37, 30))
        self.add_line('person-3', (37, 30), (34, 33))
        self.add_contour('person', 'person-1', 'person-2', 'person-3', closed=False)
        self.relate("connect", 'sail', 'person')
        self.add_line('board-1', (6, 34), (20, 34))
        self.add_line('board-2', (20, 34), (34, 33))
        self.add_line('board-3', (34, 33), (42, 33))
        self.add_contour('board', 'board-1', 'board-2', 'board-3', closed=False)
        self.relate("connect", 'mast', 'board')
        self.relate("connect", 'person', 'board')
        self.add_line('water', (6, 42), (42, 42))
