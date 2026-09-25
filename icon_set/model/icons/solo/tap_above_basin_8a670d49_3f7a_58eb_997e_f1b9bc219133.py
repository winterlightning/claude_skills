"A tap rises at the right and bends left over a shallow basin with a flat rim. One large droplet falls from the spout above the basin's smoothly curved underside.\n\nConstruction: Wall-mounted faucet above a shallow basin, with a falling drop. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a670d49-3f7a-58eb-997e-f1b9bc219133'
SOURCE_PATH = 'pictographic-primitives/wayfinding/water fountain sink_8a670d49-3f7a-58eb-997e-f1b9bc219133.svg'
AUTHOR = 'gpt-6'

class TapAboveBasin(Solo48):
    icon_id = 'tap-above-basin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('tap', 'basin', 'sink', 'water', 'drop', 'plumbing')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('tap-1', (42, 6), (24, 6))
        self.add_line('tap-2', (24, 6), (20, 10))
        self.add_line('tap-3', (20, 10), (20, 16))
        self.add_line('tap-4', (20, 16), (28, 16))
        self.add_line('tap-5', (28, 16), (28, 14))
        self.add_line('tap-6', (28, 14), (42, 14))
        self.add_line('wall', (42, 14), (42, 34))
        self.add_line('drop', (20, 25), (20, 25))
        self.add_line('basin-1', (6, 34), (42, 34))
        self.add_line('basin-2', (42, 34), (42, 42))
        self.add_line('basin-3', (42, 42), (14, 42))
        self.add_line('basin-4', (14, 42), (6, 34))
        self.add_contour('tap', 'tap-1', 'tap-2', 'tap-3', 'tap-4', 'tap-5', 'tap-6', closed=False)
        self.add_contour('basin', 'basin-1', 'basin-2', 'basin-3', 'basin-4', closed=False)
        self.relate('connect', 'wall', 'tap')
        self.relate('connect', 'wall', 'basin')
