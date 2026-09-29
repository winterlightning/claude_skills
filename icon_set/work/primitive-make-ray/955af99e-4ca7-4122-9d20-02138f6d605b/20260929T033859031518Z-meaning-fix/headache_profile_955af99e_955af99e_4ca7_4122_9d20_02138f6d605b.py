from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '955af99e-4ca7-4122-9d20-02138f6d605b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__headache-profile-955af99e/20260929T033507Z-thuan-mac/reference/head pain_955af99e-4ca7-4122-9d20-02138f6d605b.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore a tall left-facing head, continuous nose/chin/neck, and two slender coherent wavy pain strokes.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'headache-profile-955af99e'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('head pain',)

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
        self.curve('head',(17,13),((9,16),(9,22),(6,28)))
        self.add_polyline('face',(6,28),(12,28),(12,33))
        self.curve('chin',(12,33),((12,37),(16,37),(20,37)))
        self.add_line('front-neck',(20,37),(20,44))
        self.curve('back',(36,44),((36,39),(35,37),(38,34)),((44,29),(43,20),(37,15)))
        for x in (22,30):
         self.curve('pain-'+str(x),(x,4),((x-4,7),(x+4,9),(x,12)))
