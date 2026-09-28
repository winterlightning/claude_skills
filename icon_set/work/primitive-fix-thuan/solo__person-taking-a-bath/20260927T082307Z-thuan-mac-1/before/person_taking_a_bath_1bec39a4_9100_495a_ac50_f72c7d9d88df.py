"""Person Taking a Bath. Reclining bather above a deep rounded tub with two feet; reduce three steam trails to two.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide bath: tangent lower corner arcs and attached feet; the person is intrinsic to the bathing scene. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1bec39a4-9100-495a-ac50-f72c7d9d88df'
SOURCE_PATH = 'pictographic-primitives/recreation/take bath_1bec39a4-9100-495a-ac50-f72c7d9d88df.svg'
AUTHOR = 'gpt-6'


class PersonTakingABath(Solo48):
    icon_id = 'person-taking-a-bath'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('person', 'taking', 'a', 'bath')

    def build(self) -> None:
        self.add_arc('head-top', (32, 16), (38, 16), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (38, 16), (32, 16), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('arms-1', (21, 27), (28, 31))
        self.add_line('arms-2', (28, 31), (42, 27))
        self.add_contour('arms', 'arms-1', 'arms-2', closed=False)
        self.add_line('rim-left-1', (6, 27), (15, 27))
        self.add_contour('rim-left', 'rim-left-1', closed=False)
        self.add_line('tub-left', (6, 27), (8, 34))
        self.add_arc('corner-left', (8, 34), (14, 40), radius_x=6, radius_y=6, sweep=False)
        self.add_line('bottom', (14, 40), (34, 40))
        self.add_arc('corner-right', (34, 40), (40, 34), radius_x=6, radius_y=6, sweep=False)
        self.add_line('tub-right', (40, 34), (42, 27))
        self.add_contour('tub', 'tub-left', 'corner-left', 'bottom', 'corner-right', 'tub-right', closed=False)
        self.relate("connect", 'rim-left', 'tub')
        self.relate("connect", 'arms', 'tub')
        self.add_line('foot-left', (14, 40), (12, 42))
        self.add_line('foot-right', (34, 40), (36, 42))
        self.relate("connect", 'foot-left', 'tub')
        self.relate("connect", 'foot-right', 'tub')
        self.add_arc('steam-a0', (8, 6), (10, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('steam-b0', (10, 10), (8, 14), radius_x=4, radius_y=4, sweep=False)
        self.add_contour('steam0', 'steam-a0', 'steam-b0', closed=False)
        self.add_arc('steam-a1', (18, 6), (20, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('steam-b1', (20, 10), (18, 14), radius_x=4, radius_y=4, sweep=False)
        self.add_contour('steam1', 'steam-a1', 'steam-b1', closed=False)
