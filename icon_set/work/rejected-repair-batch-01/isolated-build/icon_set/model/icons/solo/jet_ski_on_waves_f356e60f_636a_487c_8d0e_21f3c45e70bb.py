"""Jet Ski on Waves. Right-facing craft with tall cowling, low rear seat and raised handlebar; retain one water row instead of two.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide sailboat: unified hull contour above sparse waves. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f356e60f-636a-487c-8d0e-21f3c45e70bb'
SOURCE_PATH = 'pictographic-primitives/recreation/nautic sports scooter 1_f356e60f-636a-487c-8d0e-21f3c45e70bb.svg'
AUTHOR = 'gpt-6'


class JetSkiOnWaves(Solo48):
    icon_id = 'jet-ski-on-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('jet', 'ski', 'on', 'waves')

    def build(self) -> None:
        self.add_line('seat-1', (4, 27), (9, 20))
        self.add_line('seat-2', (9, 20), (21, 20))
        self.add_line('seat-3', (21, 20), (27, 15))
        self.add_line('seat-4', (27, 15), (31, 10))
        self.add_arc('nose', (31, 10), (44, 29), radius_x=25, radius_y=25, sweep=True)
        self.add_line('deck', (44, 29), (4, 29))
        self.add_line('rear', (4, 29), (4, 27))
        self.add_contour('craft', 'seat-1', 'seat-2', 'seat-3', 'seat-4', 'nose', 'deck', 'rear', closed=True)
        self.add_line('handle-1', (27, 15), (22, 8))
        self.add_line('handle-2', (22, 8), (16, 8))
        self.add_contour('handle', 'handle-1', 'handle-2', closed=False)
        self.relate("connect", 'craft', 'handle')
        self.add_arc('wave-left', (4, 38), (24, 38), radius_x=10, radius_y=2, sweep=False)
        self.add_arc('wave-right', (24, 38), (44, 38), radius_x=10, radius_y=2, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-right', closed=False)
