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

        self.circle('head',27,18,4)
        self.add_line('torso',(27,30),(25,35))
        self.add_polyline('raised-arm',(27,30),(35,26),(40,18))
        self.add_line('left-arm',(27,30),(18,33))
        self.add_polyline('back-leg',(25,35),(20,40),(12,39))
        self.add_polyline('standing-leg',(25,35),(29,39),(27,44))
        for n in ('raised-arm','left-arm','back-leg','standing-leg'):self.relate('connect','torso',n)
        self.mark_human_figure('gymnast',head='head',torso='torso',torso_junction='start')
        self.curve('ribbon',(40,18),((30,-1),(6,2),(7,12)),((8,21),(22,14),(16,11)),((12,8),(9,18),(8,22)))
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
