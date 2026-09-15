"""Wakeboarder. Wakeboarder leans back against a triangular tow handle above a rounded board; reduce the paired legs to one bent leg and omit doubled arms.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2baefd97-8c64-5fc2-8c4b-0c6018001d00'
SOURCE_PATH = 'pictographic-primitives/recreation/sport wakeboarding_2baefd97-8c64-5fc2-8c4b-0c6018001d00.svg'
AUTHOR = 'gpt-6'

class WakeboarderVariant2(Solo48):
    icon_id = 'wakeboarder-v2'
    variant_of = 'wakeboarder'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('wakeboarder',)

    def build(self) -> None:
        """Open the head circle; head bottom12 and shoulder20 preserve exactly4 visible ink clearance."""
        self.add_arc('head-top', (32, 9), (38, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (38, 9), (32, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('rider-1', (21, 20), (35, 20))
        self.add_line('rider-2', (35, 20), (33, 27))
        self.add_line('rider-3', (33, 27), (26, 29))
        self.add_line('rider-4', (26, 29), (23, 34))
        self.add_contour('rider', 'rider-1', 'rider-2', 'rider-3', 'rider-4', closed=False)
        self.add_line('handle-1', (9, 20), (21, 12))
        self.add_line('handle-2', (21, 12), (21, 20))
        self.add_line('handle-3', (21, 20), (21, 28))
        self.add_line('handle-4', (21, 28), (9, 20))
        self.add_contour('handle', 'handle-1', 'handle-2', 'handle-3', 'handle-4', closed=True)
        self.add_line('rope', (6, 20), (9, 20))
        self.relate('connect', 'rope', 'handle')
        self.relate('connect', 'handle', 'rider')
        self.add_line('board-top-1', (18, 34), (23, 34))
        self.add_line('board-top-2', (23, 34), (38, 34))
        self.add_arc('board-right', (38, 34), (38, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('board-bottom', (38, 42), (18, 42))
        self.add_arc('board-left', (18, 42), (18, 34), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('board', 'board-top-1', 'board-top-2', 'board-right', 'board-bottom', 'board-left', closed=True)
        self.relate('connect', 'board', 'rider')
