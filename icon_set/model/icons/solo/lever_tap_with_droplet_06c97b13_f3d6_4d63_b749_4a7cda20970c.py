'A tap has a tall upright body, a long lever sloping upward to the right and a horizontal spout. A single large droplet hangs directly beneath the spout outlet.\n\nConstruction: Upright mixer tap with an angled lever and one detached water drop. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '06c97b13-f3d6-4d63-b749-4a7cda20970c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/water fountain drop_06c97b13-f3d6-4d63-b749-4a7cda20970c.svg'
AUTHOR = 'gpt-6'

class LeverTapWithDroplet(Solo48):
    icon_id = 'lever-tap-with-droplet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('tap', 'faucet', 'water', 'drop', 'lever', 'plumbing')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('body-1', (8, 44), (8, 16))
        self.add_line('body-2', (8, 16), (18, 16))
        self.add_line('body-3', (18, 16), (18, 18))
        self.add_line('body-4', (18, 18), (36, 18))
        self.add_line('body-5', (36, 18), (36, 26))
        self.add_line('body-6', (36, 26), (18, 26))
        self.add_line('body-7', (18, 26), (18, 44))
        self.add_line('body-8', (18, 44), (8, 44))
        self.add_line('lever-1', (8, 16), (8, 12))
        self.add_line('lever-2', (8, 12), (36, 4))
        self.add_line('lever-3', (36, 4), (40, 8))
        self.add_line('lever-4', (40, 8), (18, 16))
        self.add_line('drop-sides-1', (30, 40), (34, 35))
        self.add_line('drop-sides-2', (34, 35), (38, 40))
        self.add_arc('drop-base', (38, 40), (30, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', closed=True)
        self.add_contour('lever', 'lever-1', 'lever-2', 'lever-3', 'lever-4', closed=False)
        self.add_contour('drop', 'drop-sides-1', 'drop-sides-2', 'drop-base', closed=True)
        self.relate('connect', 'lever', 'body')
