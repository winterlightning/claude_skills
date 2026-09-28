'An upright fire extinguisher has a rounded cylinder, a short neck and two diverging handles at the top. A hose loops down the left side to a tapered nozzle.\n\nConstruction: Rounded pressure cylinder, lever and external hose with nozzle; omitted small label. Bounds (8,4)-(40,44).\nLucide: fire-extinguisher: cylinder/neck/handle/hose hierarchy.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a202026-d63d-5133-9c74-4f21265cd353'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety fire extinguisher_2a202026-d63d-5133-9c74-4f21265cd353.svg'
AUTHOR = 'gpt-6'

class FireExtinguisher(Solo48):
    icon_id = 'fire-extinguisher'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('fire', 'extinguisher', 'safety', 'hose', 'cylinder', 'equipment')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('cylinder-0-joint-1', (26, 16), (28, 16))
        self.add_line('cylinder-0-joint-2', (28, 16), (34, 16))
        self.add_arc('cylinder-1', (34, 16), (40, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('cylinder-2', (40, 22), (40, 38))
        self.add_arc('cylinder-3', (40, 38), (34, 44), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('cylinder-4', (34, 44), (26, 44))
        self.add_arc('cylinder-5', (26, 44), (20, 38), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('cylinder-6', (20, 38), (20, 22))
        self.add_arc('cylinder-7', (20, 22), (26, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('neck-1', (28, 16), (28, 8))
        self.add_line('neck-2', (28, 8), (36, 8))
        self.add_line('neck-3', (36, 8), (36, 16))
        self.add_line('lever-1', (28, 8), (36, 4))
        self.add_line('lever-2', (36, 4), (40, 4))
        self.add_line('hose-top', (28, 8), (20, 8))
        self.add_arc('hose-bend', (20, 8), (8, 20), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_line('hose-drop', (8, 20), (8, 32))
        self.add_contour('cylinder', 'cylinder-0-joint-1', 'cylinder-0-joint-2', 'cylinder-1', 'cylinder-2', 'cylinder-3', 'cylinder-4', 'cylinder-5', 'cylinder-6', 'cylinder-7', closed=True)
        self.add_contour('neck', 'neck-1', 'neck-2', 'neck-3', closed=False)
        self.add_contour('lever', 'lever-1', 'lever-2', closed=False)
        self.add_contour('hose', 'hose-top', 'hose-bend', 'hose-drop', closed=False)
        self.relate('connect', 'neck', 'cylinder')
        self.relate('connect', 'lever', 'neck')
        self.relate('connect', 'hose', 'neck')
