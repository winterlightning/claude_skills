"""Windsurfer Holding Sail. A left-leaning windsurfer grips the sail; retain bent knees and sailboard, omit second arm and sail seam.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: coherent sail outline and a structurally attached mast. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3541bc83-1790-4f3d-b629-f2530a4a05c6'
SOURCE_PATH = 'pictographic-primitives/recreation/nautic sports sailing person_3541bc83-1790-4f3d-b629-f2530a4a05c6.svg'
AUTHOR = 'gpt-6'

class WindsurferHoldingSailVariant2(Solo48):
    icon_id = 'windsurfer-holding-sail-v2'
    variant_of = 'windsurfer-holding-sail'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('windsurfer', 'holding', 'sail')

    def build(self) -> None:
        """Open and align the head over the nearest shoulder at (12,24), retaining exactly4 ink clearance."""
        self.add_line('sail-mast-1', (26, 6), (28, 16))
        self.add_line('sail-mast-2', (28, 16), (32, 36))
        self.add_contour('sail-mast', 'sail-mast-1', 'sail-mast-2', closed=False)
        self.add_arc('sail-edge', (26, 6), (42, 27), radius_x=30, radius_y=28, sweep=True)
        self.add_line('sail-foot', (42, 27), (32, 36))
        self.add_contour('sail', 'sail-edge', 'sail-foot', closed=False)
        self.relate('connect', 'sail', 'sail-mast')
        self.add_arc('head-top', (9, 13), (15, 13), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (15, 13), (9, 13), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('rider-1', (12, 42), (17, 33))
        self.add_line('rider-2', (17, 33), (8, 28))
        self.add_line('rider-3', (8, 28), (12, 24))
        self.add_line('rider-4', (12, 24), (21, 24))
        self.add_line('rider-5', (21, 24), (28, 16))
        self.add_contour('rider','rider-1','rider-2','rider-3','rider-4')
        self.relate('connect','rider','rider-5')
        self.relate('connect','rider-5','sail-mast')
        self.add_line('board-1', (6, 42), (12, 42))
        self.add_line('board-2', (12, 42), (32, 42))
        self.add_line('board-3', (32, 42), (42, 37))
        self.add_contour('board', 'board-1', 'board-2', 'board-3', closed=False)
        self.add_line('mast-base', (32, 36), (32, 42))
        self.relate('connect', 'mast-base', 'sail')
        self.relate('connect', 'mast-base', 'sail-mast')
        self.relate('connect', 'mast-base', 'board')
        self.relate('connect', 'rider', 'board')
