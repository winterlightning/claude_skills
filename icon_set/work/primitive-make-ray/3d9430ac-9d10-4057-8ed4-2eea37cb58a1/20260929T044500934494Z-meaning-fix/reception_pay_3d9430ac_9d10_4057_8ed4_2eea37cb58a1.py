from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3d9430ac-9d10-4057-8ed4-2eea37cb58a1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__reception-pay/20260929T043927Z-thuan-mac/reference/reception pay_3d9430ac-9d10-4057-8ed4-2eea37cb58a1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'reception-pay'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('reception pay',)

    # Revision plan: The payment cue was reduced to an unexplained dot and the receptionist disappeared behind a T. Restore two people, a counter and a dollar payment mark.
    def build(self):

        # Receptionist behind left counter; customer reaches left; dollar below handoff.
        self.circle('staff-head',11,10,4)
        self.curve('staff-shoulders',(5,27),((5,24),(8,22),(11,22)),((14,22),(17,24),(17,27)))
        self.add_line('counter',(5,30),(19,30))
        self.add_line('counter-leg',(8,30),(8,42))
        self.relate('connect','counter','counter-leg')
        self.circle('head',36,10,4)
        self.add_line('torso',(36,22),(36,32))
        self.add_polyline('arm',(36,23),(28,28),(25,28))
        self.add_polyline('legs',(31,42),(36,32),(41,42))
        self.relate('connect','torso','legs')
        self.mark_human_figure('customer',head='head',torso='torso',torso_junction='start')
        self.curve('dollar',(25,33),((19,31),(17,35),(22,36)),((28,37),(24,41),(19,39)))
        self.add_line('currency-bar',(22,30),(22,42))

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
