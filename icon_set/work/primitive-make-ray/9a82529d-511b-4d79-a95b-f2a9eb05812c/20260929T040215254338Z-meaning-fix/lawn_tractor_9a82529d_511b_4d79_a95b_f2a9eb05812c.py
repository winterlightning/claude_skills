from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9a82529d-511b-4d79-a95b-f2a9eb05812c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__lawn-tractor/20260929T035453Z-thuan-mac/reference/lawn tractor_9a82529d-511b-4d79-a95b-f2a9eb05812c.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the rounded engine hood, seat/back outline, steering stem and unequal wheels.
# Construction references: Lucide tractor: unequal round wheels and a separate engine silhouette; source owns lawn-mower proportions and steering stem.
class Drawing(Solo48):
    icon_id = 'lawn-tractor'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('lawn tractor',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,x,y,w,h,r=0):
        if not r:
            self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for j in range(8):
            if j%2:self.add_arc(n+str(j),pts[j],pts[(j+1)%8],radius_x=r)
            else:self.add_line(n+str(j),pts[j],pts[(j+1)%8])
        self.add_contour(n,*(n+str(j) for j in range(8)),closed=True)
    def curve(self,n,start,*segments):
        self.add_bezier(n,start,*segments)

    def build(self):
        self.circle('front-wheel',13,36,8)
        self.circle('rear-wheel',39,38,6)
        self.curve('hood',(5,29),((5,24),(7,21),(12,21)),((12,21),(26,21),(26,21)),((31,21),(33,24),(33,29)))
        self.add_polyline('hood-end',(33,29),(33,33))
        self.add_line('chassis',(21,36),(33,36))
        self.curve('seat',(26,20),((26,20),(26,16),(29,16)),((29,16),(40,15),(40,22)),((40,22),(40,32),(40,32)))
        self.add_polyline('steering',(4,4),(10,4),(16,21))
        self.relate('connect','hood','hood-end')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The mower hood, steering stem, back/seat and unequal wheels need compact attached construction and natural vehicle proportions. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '3c4eb98efd906e6f7254fb1673f99d7777ab07dc7b7bc2424b85c701dcb3c087'}
