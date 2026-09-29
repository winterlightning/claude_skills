from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '947547ca-2668-5370-8ab0-93b823725d21'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heart-eyes-face/20260929T033507Z-thuan-mac/reference/in love_947547ca-2668-5370-8ab0-93b823725d21.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore a complete round face with two recognizable heart eyes and a broad smile.
# Construction references: Lucide heart: paired rounded lobes and tapered point; complete circular face from source.
class Drawing(Solo48):
    icon_id = 'heart-eyes-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('in love',)

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
        self.circle('face',24,24,20)
        for n,x in [('left',15),('right',33)]:
         self.curve(n+'-heart',(x,16),((x-4,11),(x-9,17),(x-4,21)),((x-2,23),(x,25),(x,25)),((x,25),(x+2,23),(x+4,21)),((x+9,17),(x+4,11),(x,16)))
        self.curve('smile',(14,31),((17,40),(31,40),(34,31)))
