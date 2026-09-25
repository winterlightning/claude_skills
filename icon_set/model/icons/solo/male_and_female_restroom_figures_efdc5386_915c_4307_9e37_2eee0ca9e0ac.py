'Two front-facing figures stand side by side with circular heads. The left wears a straight-sided outfit with a short chest mark, while the right wears a flared dress with a V neckline.\n\nConstruction: Two front-facing restroom figures distinguished by straight and skirt-shaped bodies. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'efdc5386-915c-4307-9e37-2eee0ca9e0ac'
SOURCE_PATH = 'pictographic-primitives/wayfinding/toilet sign 1_efdc5386-915c-4307-9e37-2eee0ca9e0ac.svg'
AUTHOR = 'gpt-6'

class MaleAndFemaleRestroomFigures(Solo48):
    icon_id = 'male-and-female-restroom-figures'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('restroom', 'toilet', 'male', 'female', 'people', 'wayfinding')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('male-head-top', (9, 9), (15, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('male-head-bottom', (15, 9), (9, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('female-head-top', (31, 9), (37, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('female-head-bottom', (37, 9), (31, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('male-arms-1', (6, 27), (12, 21))
        self.add_line('male-arms-2', (12, 21), (18, 27))
        self.add_line('male-body-1', (12, 21), (12, 32))
        self.add_line('male-body-2', (12, 32), (8, 42))
        self.add_line('male-leg-1', (12, 32), (16, 42))
        self.add_line('female-1', (34, 21), (26, 34))
        self.add_line('female-2', (26, 34), (30, 34))
        self.add_line('female-3', (30, 34), (30, 42))
        self.add_line('female-4', (30, 42), (38, 42))
        self.add_line('female-5', (38, 42), (38, 34))
        self.add_line('female-6', (38, 34), (42, 34))
        self.add_line('female-7', (42, 34), (34, 21))
        self.add_contour('male-head', 'male-head-top', 'male-head-bottom', closed=True)
        self.add_contour('female-head', 'female-head-top', 'female-head-bottom', closed=True)
        self.add_contour('male-arms', 'male-arms-1', 'male-arms-2', closed=False)
        self.add_contour('male-body', 'male-body-1', 'male-body-2', closed=False)
        self.add_contour('male-leg', 'male-leg-1', closed=False)
        self.add_contour('female', 'female-1', 'female-2', 'female-3', 'female-4', 'female-5', 'female-6', 'female-7', closed=False)
        self.relate('connect', 'male-arms', 'male-body')
        self.relate('connect', 'male-body', 'male-leg')
