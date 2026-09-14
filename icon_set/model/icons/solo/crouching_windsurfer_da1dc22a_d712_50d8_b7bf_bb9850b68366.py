"""Windsurfer with Open Sail Outline. Crouching rider reaches toward a complete curved sail on a sloping board. Reconstruct the missing right edge instead of preserving the source defect; omit decorative sail details.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: a closed coherent sail and structural mast. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da1dc22a-d712-50d8-b7bf-bb9850b68366'
SOURCE_PATH = 'pictographic-primitives/recreation/sport windsurfing_da1dc22a-d712-50d8-b7bf-bb9850b68366.svg'
AUTHOR = 'gpt-6'


class CrouchingWindsurfer(Solo48):
    icon_id = 'crouching-windsurfer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('crouching', 'windsurfer')

    def build(self) -> None:
        self.add_arc('sail-edge', (25, 6), (8, 30), radius_x=36, radius_y=36, sweep=False)
        self.add_line('sail-base-1', (8, 30), (20, 30))
        self.add_line('sail-base-2', (20, 30), (21, 25))
        self.add_line('sail-base-3', (21, 25), (25, 6))
        self.add_contour('sail', 'sail-edge', 'sail-base-1', 'sail-base-2', 'sail-base-3', closed=True)
        self.add_line('mast', (20, 30), (18, 38))
        self.relate("connect", 'sail', 'mast')
        self.add_arc('head-top', (34, 17), (40, 17), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (40, 17), (34, 17), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('person-1', (23, 26), (35, 28))
        self.add_line('person-2', (35, 28), (32, 35))
        self.add_line('person-3', (32, 35), (35, 40))
        self.add_contour('person', 'person-1', 'person-2', 'person-3', closed=False)
        self.add_line('hand', (23, 26), (21, 25))
        self.relate("connect", 'person', 'hand')
        self.relate("connect", 'hand', 'sail')
        self.add_line('board-1', (6, 36), (18, 38))
        self.add_line('board-2', (18, 38), (35, 40))
        self.add_line('board-3', (35, 40), (42, 42))
        self.add_contour('board', 'board-1', 'board-2', 'board-3', closed=False)
        self.relate("connect", 'mast', 'board')
        self.relate("connect", 'person', 'board')
