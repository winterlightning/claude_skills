'A flame sits beneath a short overhead sprinkler line. A single vertical droplet or spray mark descends from the centre of the horizontal line toward the pointed top of the flame.\n\nConstruction: Ceiling sprinkler line above one falling drop and a flame. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b7521df-9e30-4205-9f5c-c5cc20293e20'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety extinguish fire_4b7521df-9e30-4205-9f5c-c5cc20293e20.svg'
AUTHOR = 'gpt-6'

class FireSprinkler(Solo48):
    icon_id = 'fire-sprinkler'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('sprinkler', 'fire', 'water', 'safety', 'extinguish', 'flame')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('ceiling', (8, 4), (40, 4))
        self.add_line('spray', (24, 13), (24, 16))
        self.add_arc('flame-left', (24, 25), (14, 34), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_arc('flame-base-left', (14, 34), (24, 44), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('flame-base-right', (24, 44), (40, 32), radius_x=16, radius_y=12, large_arc=False, sweep=False)
        self.add_line('flame-tips-1', (40, 32), (36, 24))
        self.add_line('flame-tips-2', (36, 24), (30, 34))
        self.add_line('flame-tips-3', (30, 34), (24, 25))
        self.add_contour('flame', 'flame-left', 'flame-base-left', 'flame-base-right', 'flame-tips-1', 'flame-tips-2', 'flame-tips-3', closed=True)
