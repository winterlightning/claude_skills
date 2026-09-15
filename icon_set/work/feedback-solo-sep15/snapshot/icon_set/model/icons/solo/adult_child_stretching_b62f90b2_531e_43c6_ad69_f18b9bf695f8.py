'A tall figure raises both arms in a wide V beside a smaller crouched figure on the left. The smaller figure spreads its arms and bends both knees outward.\nConstruction: Bounds (6,6)-(42,42). Tall adult with raised arms beside smaller crouching child. Physical group, no modifier. Keep unequal head sizes; simplify fingers and paired limbs.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b62f90b2-531e-43c6-ad69-f18b9bf695f8'
SOURCE_PATH = 'pictographic-primitives/sports/yoga stretch_b62f90b2-531e-43c6-ad69-f18b9bf695f8.svg'
AUTHOR = 'gpt-6'

class AdultChildStretching(Solo48):
    icon_id = 'adult-child-stretching'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('adult', 'child', 'stretching', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (31, 9), (37, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (37, 9), (31, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('adult-arms', (24, 17), (34, 25), (42, 17), closed=False)
        self.add_line('adult-body', (34, 25), (34, 33))
        self.relate("connect", 'adult-arms', 'adult-body')
        self.add_polyline('adult-legs', (30, 42), (34, 33), (40, 42), closed=False)
        self.relate("connect", 'adult-body', 'adult-legs')
        self.add_arc('child-head-top', (10, 15), (14, 15), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('child-head-bottom', (14, 15), (10, 15), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('child-head', 'child-head-top', 'child-head-bottom', closed=True)
        self.add_polyline('child-arms', (6, 26), (12, 26), (20, 26), closed=False)
        self.add_line('child-body', (12, 26), (12, 34))
        self.relate("connect", 'child-arms', 'child-body')
        self.add_polyline('child-legs', (6, 42), (12, 34), (18, 42), closed=False)
        self.relate("connect", 'child-body', 'child-legs')
