from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f8bb3c70-137a-40bf-96f2-7de841464ca6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ribbon-gymnast-circle/20260929T043927Z-thuan-mac/reference/ribbon person_f8bb3c70-137a-40bf-96f2-7de841464ca6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ribbon-gymnast-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('ribbon person',)

    # Revision plan: The gymnast lost the raised arm, long leg and flowing ribbon; it read like a seated person under a dome. Restore the dancing pose and near-circular ribbon sweep.
    def build(self):

        self.circle('head',24,15,4)
        self.add_line('torso',(24,27),(24,34))
        self.add_polyline('raised-arm',(24,27),(15,24),(11,16))
        self.add_line('other-arm',(24,27),(36,31))
        self.add_line('standing-leg',(24,34),(22,42))
        self.curve('raised-leg',(24,34),((29,40),(32,42),(38,42)))
        for n in ('raised-arm','other-arm','standing-leg','raised-leg'):self.relate('connect','torso',n)
        self.mark_human_figure('gymnast',head='head',torso='torso',torso_junction='start')
        self.curve('ribbon',(13,9),((25,1),(42,11),(42,28)))
        self.curve('ribbon-lower',(6,24),((7,31),(11,36),(16,38)))

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def rect(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for k in range(8):
            a,b=pts[k],pts[(k+1)%8]
            if k%2:self.add_arc(n+str(k),a,b,radius_x=r)
            else:self.add_line(n+str(k),a,b)
        self.add_contour(n,*[n+str(k) for k in range(8)],closed=True)

    def curve(self,n,start,*segs):
        self.add_bezier(n,start,*segs)

    def star(self,n,x,y,s):
        # Five-point silhouette, shared integer vertices for each star instance.
        p=[(0,-6),(2,-2),(6,-2),(3,1),(4,6),(0,3),(-4,6),(-3,1),(-6,-2),(-2,-2)]
        self.add_polyline(n,*[(x+round(a*s/6),y+round(b*s/6)) for a,b in p],closed=True)
