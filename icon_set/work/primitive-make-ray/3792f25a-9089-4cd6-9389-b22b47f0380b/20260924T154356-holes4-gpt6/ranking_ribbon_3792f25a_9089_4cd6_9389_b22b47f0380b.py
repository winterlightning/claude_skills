from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3792f25a-9089-4cd6-9389-b22b47f0380b'
SOURCE_PATH = 'pictographic-primitives/rewards/ranking ribbon_3792f25a-9089-4cd6-9389-b22b47f0380b.svg'
AUTHOR = 'gpt-6'
PLAN = 'A five-point star with paired ribbon tails.'
CONSTRUCTION_REFERENCES = 'Local Lucide award: coherent contours and shared attachments; original and atomic-debug inspected.'
OMISSIONS = 'Removed the hidden banner segment beneath the star and the small fold-divider strokes; ribbon attachments moved to star tips.'

class Drawing(Solo48):
    icon_id = 'ranking-ribbon'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('ranking', 'ribbon')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)
    def monitor(self):
        self.box('screen',6,6,36,28,3)
        self.add_line('stand',(24,34),(24,42))
        self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','screen','stand');self.relate('connect','stand','foot')
    def person(self,x,y,r):
        # human_ref/user.svg: head and broad shoulders. Exact 8 centerline / 4 ink gap.
        self.circle('head',x,y,r)
        top=y+r+8
        self.add_arc('shoulders',(x-5,top+5),(x+5,top+5),radius_x=5)
    def play(self,x,y,w,h):
        self.add_polyline('play',(x,y),(x+w,y+h//2),(x,y+h),closed=True)

    def build(self):
        # Star fronts the upper banner edge. Bottom and open tails are separated.
        self.add_polyline('star',(24,8),(27,16),(35,16),(29,22),(32,30),(24,25),(16,30),(19,22),(13,16),(21,16),closed=True)
        # Side ribbons merge into the star silhouette; no hidden crossbar beneath it.
        for n,pts in [('left',((13,16),(4,24),(4,33),(8,36),(6,40),(15,36),(16,30))),('right',((35,16),(44,24),(44,33),(40,36),(42,40),(33,36),(32,30)))]:
            self.add_polyline(n+'-ribbon',*pts)
            self.relate('connect',n+'-ribbon','star')

# Final repair review: A five-point star with paired ribbon tails.
# HRECT_L preserves the wide award silhouette.
# Changes: Removed the hidden banner segment beneath the star and the small fold-divider strokes; ribbon attachments moved to star tips.
# validate_icon: valid; build gate: pass with zero errors and zero warnings.
