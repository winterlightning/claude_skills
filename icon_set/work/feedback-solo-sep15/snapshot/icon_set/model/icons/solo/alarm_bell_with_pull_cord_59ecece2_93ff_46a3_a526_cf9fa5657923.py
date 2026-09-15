'A domed bell has a flared rim, a small top loop and a rounded clapper below. A cord curves from underneath to a round pull at the right, with two arcs above it.\n\nConstruction: Bell dome and flared rim beside a long pull cord with a circular grip. Sound waves omitted. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59ecece2-93ff-46a3-a526-cf9fa5657923'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety bell_59ecece2-93ff-46a3-a526-cf9fa5657923.svg'
AUTHOR = 'gpt-6'

class AlarmBellWithPullCord(Solo48):
    icon_id = 'alarm-bell-with-pull-cord'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('bell', 'alarm', 'cord', 'ring', 'safety', 'signal')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('dome-joint-1', (10, 18), (20, 8), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('dome-joint-2', (20, 8), (30, 18), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('bell-sides-1', (30, 18), (30, 30))
        self.add_line('bell-sides-2', (30, 30), (34, 34))
        self.add_line('bell-sides-3-joint-1', (34, 34), (20, 34))
        self.add_line('bell-sides-3-joint-2', (20, 34), (6, 34))
        self.add_line('bell-sides-4', (6, 34), (10, 30))
        self.add_line('bell-sides-5', (10, 30), (10, 18))
        self.add_line('hanger', (20, 6), (20, 8))
        self.add_line('cord-1', (20, 34), (20, 42))
        self.add_line('cord-2', (20, 42), (42, 42))
        self.add_line('cord-3', (42, 42), (42, 24))
        self.add_line('cord-4', (42, 24), (39, 18))
        self.add_arc('pull-top', (36, 15), (42, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('pull-bottom-joint-1', (42, 15), (39, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('pull-bottom-joint-2', (39, 18), (36, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('bell', 'dome-joint-1', 'dome-joint-2', 'bell-sides-1', 'bell-sides-2', 'bell-sides-3-joint-1', 'bell-sides-3-joint-2', 'bell-sides-4', 'bell-sides-5', closed=True)
        self.add_contour('cord', 'cord-1', 'cord-2', 'cord-3', 'cord-4', closed=False)
        self.add_contour('pull', 'pull-top', 'pull-bottom-joint-1', 'pull-bottom-joint-2', closed=True)
        self.relate('connect', 'hanger', 'bell')
        self.relate('connect', 'cord', 'bell')
        self.relate('connect', 'cord', 'pull')
