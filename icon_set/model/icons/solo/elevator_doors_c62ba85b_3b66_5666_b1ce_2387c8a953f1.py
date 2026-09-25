'A rounded rectangular elevator surround encloses two tall closed doors divided at the centre. Small up and down chevrons sit above the door opening as paired directional indicators.\n\nConstruction: Elevator frame enclosing paired doors; reduced directional chevrons to preserve the structural opening. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c62ba85b-3b66-5666-b1ce-2387c8a953f1'
SOURCE_PATH = 'pictographic-primitives/wayfinding/lift_c62ba85b-3b66-5666-b1ce-2387c8a953f1.svg'
AUTHOR = 'gpt-6'

class ElevatorDoors(Solo48):
    icon_id = 'elevator-doors'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('elevator', 'lift', 'doors', 'building', 'transport', 'entrance')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('frame-1', (16, 42), (6, 42))
        self.add_line('frame-2', (6, 42), (6, 6))
        self.add_line('frame-3', (6, 6), (42, 6))
        self.add_line('frame-4', (42, 6), (42, 42))
        self.add_line('frame-5', (42, 42), (32, 42))
        self.add_line('doors-1', (16, 42), (16, 18))
        self.add_line('doors-2', (16, 18), (24, 18))
        self.add_line('doors-3', (24, 18), (32, 18))
        self.add_line('doors-4', (32, 18), (32, 42))
        self.add_line('center-seam', (24, 18), (24, 42))
        self.add_contour('frame', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', closed=False)
        self.add_contour('doors', 'doors-1', 'doors-2', 'doors-3', 'doors-4', closed=False)
        self.relate('connect', 'doors', 'center-seam')
        self.relate('connect', 'frame', 'doors')
