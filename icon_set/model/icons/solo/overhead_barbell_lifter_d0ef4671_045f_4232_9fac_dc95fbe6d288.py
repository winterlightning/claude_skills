'A person lifts a barbell overhead.\nConstruction: Square centerlines (6,6)-(42,42). Shared vertical axis, paired weights and bent arms; remove body outline and grip detail.\nLucide: dumbbell: paired weights; accessibility: simple circular head and bent limbs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0ef4671-045f-4232-9fac-dc95fbe6d288'
SOURCE_PATH = 'pictographic-primitives/sports/weightlift_d0ef4671-045f-4232-9fac-dc95fbe6d288.svg'
AUTHOR = 'gpt-6'

class OverheadBarbellLifter(Solo48):
    icon_id = 'overhead-barbell-lifter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('overhead', 'barbell', 'lifter', 'sport')

    def build(self):
        self.add_arc('head-top', (21, 18), (27, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 18), (21, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('bar', (6, 18), (6, 6), (12, 6), (36, 6), (42, 6), (42, 18), closed=False)
        self.add_polyline('arms', (12, 6), (12, 30), (24, 30), (36, 30), (36, 6), closed=False)
        self.relate("connect", 'arms', 'bar')
        self.add_line('torso', (24, 30), (24, 34))
        self.relate("connect", 'arms', 'torso')
        self.add_polyline('legs', (18, 42), (24, 34), (30, 42), closed=False)
        self.relate("connect", 'legs', 'torso')
