'An adult and a smaller child walk together with their hands meeting between them. A small tiered evergreen stands above the child, placing the pair within a park scene.\n\nConstruction: Adult and child walk beside a small tree; clothing details omitted. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a7cb03f-21bf-4ab8-a038-43f1f09b9abc'
SOURCE_PATH = 'pictographic-primitives/wayfinding/family walk park_1a7cb03f-21bf-4ab8-a038-43f1f09b9abc.svg'
AUTHOR = 'gpt-6'

class AdultAndChildWalkingInPark(Solo48):
    icon_id = 'adult-and-child-walking-in-park'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('adult', 'child', 'family', 'walking', 'park', 'tree')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('adult-head-top', (9, 11), (15, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('adult-head-bottom', (15, 11), (9, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('adult-body-1', (12, 23), (12, 30))
        self.add_line('adult-arms-1', (4, 28), (12, 23))
        self.add_line('adult-arms-2', (12, 23), (22, 28))
        self.add_line('adult-legs-1', (6, 40), (12, 30))
        self.add_line('adult-legs-2', (12, 30), (20, 40))
        self.add_line('child-head', (30, 26), (30, 26))
        self.add_line('child-body-1', (32, 35), (32, 37))
        self.add_line('child-body-2', (32, 37), (28, 40))
        self.add_line('child-leg-1', (32, 37), (38, 40))
        self.add_line('child-arms-1', (29, 35), (32, 35))
        self.add_line('child-arms-2', (32, 35), (38, 34))
        self.add_arc('tree-crown-top', (32, 14), (44, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('tree-crown-bottom-joint-1', (44, 14), (38, 20), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('tree-crown-bottom-joint-2', (38, 20), (32, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('tree-trunk', (38, 20), (38, 26))
        self.add_contour('adult-head', 'adult-head-top', 'adult-head-bottom', closed=True)
        self.add_contour('adult-body', 'adult-body-1', closed=False)
        self.add_contour('adult-arms', 'adult-arms-1', 'adult-arms-2', closed=False)
        self.add_contour('adult-legs', 'adult-legs-1', 'adult-legs-2', closed=False)
        self.add_contour('child-body', 'child-body-1', 'child-body-2', closed=False)
        self.add_contour('child-leg', 'child-leg-1', closed=False)
        self.add_contour('child-arms', 'child-arms-1', 'child-arms-2', closed=False)
        self.add_contour('tree-crown', 'tree-crown-top', 'tree-crown-bottom-joint-1', 'tree-crown-bottom-joint-2', closed=True)
        self.relate('connect', 'adult-body', 'adult-arms')
        self.relate('connect', 'adult-body', 'adult-legs')
        self.relate('connect', 'child-body', 'child-leg')
        self.relate('connect', 'child-body', 'child-arms')
        self.relate('connect', 'tree-crown', 'tree-trunk')
