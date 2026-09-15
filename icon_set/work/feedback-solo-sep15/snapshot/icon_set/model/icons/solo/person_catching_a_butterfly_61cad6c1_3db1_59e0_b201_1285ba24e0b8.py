"""Person Catching a Butterfly. Torso figure raises a net toward a butterfly; omit mesh and reduce the insect to paired rounded wings. Pose and insect remain asymmetric.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61cad6c1-3db1-59e0-b201-1285ba24e0b8'
SOURCE_PATH = 'pictographic-primitives/recreation/catch bug_61cad6c1-3db1-59e0-b201-1285ba24e0b8.svg'
AUTHOR = 'gpt-6'


class PersonCatchingAButterfly(Solo48):
    icon_id = 'person-catching-a-butterfly'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('person', 'catching', 'a', 'butterfly')

    def build(self) -> None:
        self.add_arc('head-top', (36, 26), (40, 26), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('head-bottom', (40, 26), (36, 26), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('figure-1', (29, 42), (29, 37))
        self.add_line('figure-2', (29, 37), (20, 28))
        self.add_contour('figure', 'figure-1', 'figure-2', closed=False)
        self.add_line('back-1', (29, 37), (37, 37))
        self.add_line('back-2', (37, 37), (42, 42))
        self.add_contour('back', 'back-1', 'back-2', closed=False)
        self.relate("connect", 'figure', 'back')
        self.add_line('net-1', (27, 6), (42, 6))
        self.add_line('net-2', (42, 6), (35, 15))
        self.add_line('net-3', (35, 15), (27, 15))
        self.add_line('net-4', (27, 15), (27, 6))
        self.add_contour('net', 'net-1', 'net-2', 'net-3', 'net-4', closed=True)
        self.add_line('handle-1', (27, 15), (27, 23))
        self.add_line('handle-2', (27, 23), (20, 28))
        self.add_contour('handle', 'handle-1', 'handle-2', closed=False)
        self.relate("connect", 'net', 'handle')
        self.relate("connect", 'figure', 'handle')
        self.add_arc('wing-left-top', (6, 12), (12, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('wing-left-bottom', (12, 12), (6, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('wing-left', 'wing-left-top', 'wing-left-bottom', closed=True)
        self.add_arc('wing-right-top', (12, 12), (18, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('wing-right-bottom', (18, 12), (12, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('wing-right', 'wing-right-top', 'wing-right-bottom', closed=True)
        self.relate("connect", 'wing-left', 'wing-right')
        self.add_line('insect-body', (12, 12), (12, 20))
        self.relate("connect", 'insect-body', 'wing-left')
        self.relate("connect", 'insect-body', 'wing-right')
