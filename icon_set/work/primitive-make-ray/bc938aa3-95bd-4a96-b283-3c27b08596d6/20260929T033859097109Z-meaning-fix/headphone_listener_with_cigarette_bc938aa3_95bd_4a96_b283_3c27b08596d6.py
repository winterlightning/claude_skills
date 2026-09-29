from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bc938aa3-95bd-4a96-b283-3c27b08596d6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__headphone-listener-with-cigarette/20260929T033507Z-thuan-mac/reference/music genre smoke_bc938aa3-95bd-4a96-b283-3c27b08596d6.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the circular face, separate overhead band, two earcups and a straight diagonal cigarette.
# Construction references: Lucide headphones: continuous overhead arch and rounded earcups; user.svg: circular head vocabulary.
class Drawing(Solo48):
    icon_id = 'headphone-listener-with-cigarette'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('music genre smoke',)

    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,x,y,w,h,r=0):
        if not r:
            self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for j in range(8):
            a,b=pts[j],pts[(j+1)%8]
            if j%2:self.add_arc(n+str(j),a,b,radius_x=r)
            else:self.add_line(n+str(j),a,b)
        self.add_contour(n,*(n+str(j) for j in range(8)),closed=True)
    def curve(self,n,start,*segments):
        self.add_bezier(n,start,*segments)

    def build(self):
        self.curve('headband',(5,23),((5,-2),(43,-2),(43,23)))
        self.curve('face',(12,18),((15,10),(33,10),(36,18)),((40,25),(38,32),(33,37)),((29,42),(19,42),(15,38)),((8,33),(8,24),(12,18)))
        self.rect('ear-left',4,20,7,12,3)
        self.rect('ear-right',37,20,7,12,3)
        self.curve('smile',(19,31),((22,34),(27,34),(30,31)))
        self.add_polyline('cigarette',(32,32),(42,41),(39,44),(29,35),closed=True)
