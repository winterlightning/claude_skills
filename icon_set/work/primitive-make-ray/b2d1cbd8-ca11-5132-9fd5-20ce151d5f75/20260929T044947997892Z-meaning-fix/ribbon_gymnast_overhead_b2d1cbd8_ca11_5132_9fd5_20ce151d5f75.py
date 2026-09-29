from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b2d1cbd8-ca11-5132-9fd5-20ce151d5f75'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ribbon-gymnast-overhead/20260929T043927Z-thuan-mac/reference/rhythmic ribbon_b2d1cbd8-ca11-5132-9fd5-20ce151d5f75.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ribbon-gymnast-overhead'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('rhythmic ribbon',)

    # Revision plan: The gymnast became a squat seated shape and the ribbon lost its loop. Restore a raised hand, standing leg, bent back leg and an overhead ribbon loop.
    def build(self):

        # Upright torso, longer support leg and extended rear leg beneath an overhead ribbon loop.
        self.circle('head',27,14,4)
        self.curve('torso',(27,26),((27,29),(27,31),(25,33)))
        self.add_polyline('raised-arm',(27,26),(35,23),(40,15))
        self.add_line('left-arm',(27,26),(18,30))
        self.add_polyline('back-leg',(25,33),(19,38),(10,37))
        self.add_polyline('standing-leg',(25,33),(29,38),(27,44))
        for n in ('raised-arm','left-arm','back-leg','standing-leg'):self.relate('connect','torso',n)
        self.mark_human_figure('gymnast',head='head',torso='torso',torso_junction='start')
        self.curve('ribbon',(40,15),((30,-2),(7,1),(6,10)),((5,19),(22,15),(16,11)),((12,8),(9,19),(8,22)))
        self.relate('connect','raised-arm','ribbon')

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
