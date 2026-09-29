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
        self.add_polyline('nose',(15,23),(11,25),(16,26),(16,29))
        self.curve('lips-chin',(16,29),((22,28),(23,31),(18,32)),((18,37),(22,35),(25,35)))
        self.add_polyline('neck-front',(25,35),(27,41),(24,45))
        self.add_line('closed-eye',(19,17),(22,18))
        for n,a,b in [('upper',(4,29),(10,31)),('middle',(3,36),(10,35)),('lower',(5,43),(11,39))]:self.add_line('sneeze-'+n,a,b)
        self.relate('connect','head-neck','nose');self.relate('connect','nose','lips-chin');self.relate('connect','lips-chin','neck-front')
