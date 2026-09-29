from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f2e9b73a-cb3b-4ba3-9a35-136a976c9aec'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__left-facing-person-sneezing/20260929T035453Z-thuan-mac/reference/sneeze_f2e9b73a-cb3b-4ba3-9a35-136a976c9aec.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore a smooth left-facing anatomical profile, closed eye, open lips, sloping neck and three outward sneeze rays.
# Construction references: Human reference: preserve coherent continuous head/neck anatomy rather than a detached stick-figure construction; original owns profile and sneeze rays.
class Drawing(Solo48):
    icon_id = 'left-facing-person-sneezing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sneeze',)

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
        self.curve('head-neck',(15,23),((11,23),(12,20),(14,17)),((15,14),(13,9),(20,5)),((31,0),(43,10),(39,22)),((37,27),(34,30),(35,34)),((36,39),(40,43),(43,46)))
        self.add_polyline('nose-upper-lip',(15,23),(11,25),(17,27))
        self.curve('lower-lip-chin',(17,33),((17,38),(22,36),(25,35)))
        self.add_polyline('neck-front',(25,35),(27,41),(24,45))
        self.add_line('closed-eye',(19,17),(22,18))
        for n,a,b in [('upper',(4,28),(10,30)),('middle',(3,35),(10,35)),('lower',(5,42),(11,39))]:self.add_line('sneeze-'+n,a,b)
        self.relate('connect','head-neck','nose-upper-lip');self.relate('connect','lower-lip-chin','neck-front')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The continuous head/neck, open mouth and three sneeze rays need compact face spacing and an asymmetric envelope. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '8a4eb29825ae37cd082932d0751387a502e9dc5235afeff9aa1dc5d2b2ad7e8c'}
