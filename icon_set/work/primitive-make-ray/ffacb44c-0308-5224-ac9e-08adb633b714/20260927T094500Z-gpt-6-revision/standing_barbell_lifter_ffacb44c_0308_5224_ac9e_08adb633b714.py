'A person holds a barbell at hip level.\nConstruction: Square centerlines (6,6)-(42,42). Shared vertical axis, paired weights and bent arms; remove body outline and grip detail.\nLucide: dumbbell: paired weights; accessibility: simple circular head and bent limbs.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ffacb44c-0308-5224-ac9e-08adb633b714'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-barbell-lifter/20260927T093533Z-thuan-mac-1/reference/weightlifting_ffacb44c-0308-5224-ac9e-08adb633b714.svg'
AUTHOR = "gpt-6"

class StandingBarbellLifter(Solo48):
    icon_id = 'standing-barbell-lifter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('standing', 'barbell', 'lifter', 'sport')

    def build(self):
        self.add_arc('head-top', (20, 9), (28, 9), radius_x=4, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (28, 9), (20, 9), radius_x=4, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('arms', (14, 29), (14, 21), (24, 21), (34, 21), (34, 29), closed=False)
        self.add_polyline('torso', (24, 21), (24, 29), (24, 33), closed=False)
        self.relate("connect", 'arms', 'torso')
        self.add_polyline('legs', (18, 42), (24, 33), (30, 42), closed=False)
        self.relate("connect", 'legs', 'torso')
        self.add_polyline('bar', (6, 29), (14, 29), (24, 29), (34, 29), (42, 29), closed=False)
        self.relate("connect", 'arms', 'bar')
        self.relate("connect", 'torso', 'bar')
        self.add_polyline('wl', (6, 20), (6, 29), (6, 38), closed=False)
        self.add_polyline('wr', (42, 20), (42, 29), (42, 38), closed=False)
        self.relate("connect", 'bar', 'wl')
        self.relate("connect", 'bar', 'wr')
