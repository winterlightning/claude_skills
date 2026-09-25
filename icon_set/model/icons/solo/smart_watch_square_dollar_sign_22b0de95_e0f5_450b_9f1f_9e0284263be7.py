"""smart watch square dollar sign: standalone batch 17 repair.
Retained the square watch case, paired straps and dollar mark. Square-cornered case, open strap ends and separated top/bottom dollar extensions remove small holes.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '22b0de95-e0f5-450b-9f1f-9e0284263be7'
SOURCE_PATH = 'pictographic-primitives/other/smart watch square dollar sign_22b0de95-e0f5-450b-9f1f-9e0284263be7.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'dollar-sign'

class Drawing(Solo48):
    icon_id='smart-watch-square-dollar-sign'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('smart', 'watch', 'square', 'dollar', 'sign')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.watch()
        self.dollar()




    def watch(self,circular=False):
        if circular:
            # Circular silhouette with integer attachment knots and continuous tangents.
            self.add_bezier('case-upper-left',(8,24),((8,18),(11,12),(16,10)),((21,8),(22,8),(24,8)))
            self.add_bezier('case-upper-right',(24,8),((26,8),(27,8),(32,10)),((37,12),(40,18),(40,24)))
            self.add_bezier('case-lower-right',(40,24),((40,30),(37,36),(32,38)),((27,40),(26,40),(24,40)))
            self.add_bezier('case-lower-left',(24,40),((22,40),(21,40),(16,38)),((11,36),(8,30),(8,24)))
            self.add_contour('case','case-upper-left','case-upper-right','case-lower-right','case-lower-left',closed=True)
            self.add_polyline('strap-top',(16,10),(18,4),(30,4),(32,10))
            self.add_polyline('strap-bottom',(16,38),(18,44),(30,44),(32,38))
        else:
            self.add_polyline('case',(8,8),(16,8),(32,8),(40,8),(40,40),(32,40),(16,40),(8,40),closed=True)
            self.add_line('strap-top-left',(16,8),(17,4))
            self.add_line('strap-top-right',(32,8),(31,4))
            self.add_line('strap-bottom-left',(16,40),(17,44))
            self.add_line('strap-bottom-right',(32,40),(31,44))
        for n in ['strap-top-left','strap-top-right','strap-bottom-left','strap-bottom-right']:self.relate('connect','case',n)

    def dollar(self):
        self.add_bezier('dollar-cap',(28,19),((27,18),(25,18),(24,18)))
        self.add_bezier('dollar-upper',(24,18),((20,18),(20,23),(24,24)))
        self.add_bezier('dollar-lower',(24,24),((28,25),(28,30),(24,30)))
        self.add_bezier('dollar-foot',(24,30),((23,30),(21,30),(21,29)))
        self.add_contour('dollar','dollar-cap','dollar-upper','dollar-lower','dollar-foot')
        self.add_line('stem-top',(24,16),(24,18))
        self.add_line('stem-bottom',(24,30),(24,32))
        self.relate('connect','dollar','stem-top');self.relate('connect','dollar','stem-bottom')

