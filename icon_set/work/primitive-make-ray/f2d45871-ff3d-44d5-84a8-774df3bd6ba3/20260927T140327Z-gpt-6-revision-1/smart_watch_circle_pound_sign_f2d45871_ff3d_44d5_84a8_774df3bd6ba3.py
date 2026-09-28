"""smart watch circle pound sign: standalone batch 17 repair.
Retained the circular watch case, paired straps and pound mark. Open strap ends, rebuilt sterling hook, shorter crossbar and eight-unit baseline spacing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f2d45871-ff3d-44d5-84a8-774df3bd6ba3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smartwatch-pound-symbol/20260927T140026Z-thuan-mac-1/reference/smart watch circle pound sign_f2d45871-ff3d-44d5-84a8-774df3bd6ba3.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCE = 'pound-sterling'

class Drawing(Solo48):
    icon_id = 'smartwatch-pound-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('combination', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('smartwatch', 'pound', 'symbol')



    def build(self):
        curves=[
            ((8,24),(8,17),(11,12),(16,10)),
            ((16,10),(20,7),(28,7),(32,10)),
            ((32,10),(37,12),(40,17),(40,24)),
            ((40,24),(40,31),(37,36),(32,38)),
            ((32,38),(28,41),(20,41),(16,38)),
            ((16,38),(11,36),(8,31),(8,24)),
        ]
        for j,(a,c1,c2,b) in enumerate(curves,1):
            self.add_bezier(f'face-{j}',a,(c1,c2,b))
        self.add_contour('face',*(f'face-{j}' for j in range(1,7)),closed=True)
        self.add_polyline('upper-band',(16,10),(18,4),(30,4),(32,10))
        self.add_polyline('lower-band',(16,38),(18,44),(30,44),(32,38))
        self.relate('connect','face','upper-band')
        self.relate('connect','face','lower-band')
        self.add_bezier('pound-hook',(29,20),((29,15),(21,15),(21,21)))
        self.add_line('pound-stem',(21,21),(21,31))
        self.add_line('pound-bar',(17,24),(26,24))
        self.add_line('pound-foot',(18,31),(30,31))
        for name in ('pound-hook','pound-bar','pound-foot'):
            self.relate('connect','pound-stem',name)

