from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9181cbaa-7e8c-531e-9143-78e43b2cb58e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__retro-bicycle/20260929T043927Z-thuan-mac/reference/bicycle retro_9181cbaa-7e8c-531e-9143-78e43b2cb58e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': "Preserve the classic bicycle diamond frame, equal wheels and curled handlebar. Natural wheel/frame intersections and small chassis openings are intentional and recognizable at native size. Visually reviewed at 48px in light and dark themes under the user's explicit delegated exception authorization.", 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'afc41b829e1dd145f41ef1d6edef15a828edc085e0cbf1672e3699f09e9a8df0'}
    icon_id = 'retro-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('bicycle retro',)

    # Revision plan: The wheels were undersized and the retro handlebar was a heavy hook. Restore larger wheels, the diamond frame, a slim saddle and curled handlebar.
    def build(self):

        # Retro diamond frame above equal large wheels; saddle and curled bar share the top level.
        for x in (12,36): self.circle('wheel-'+str(x),x,32,8)
        self.add_polyline('frame',(12,32),(24,32),(32,16),(18,16),(12,32))
        self.add_line('seat-tube',(18,8),(24,32))
        self.add_line('saddle',(13,8),(23,8));self.relate('connect','seat-tube','saddle')
        self.add_polyline('fork',(36,32),(30,8),(36,8))
        self.add_arc('handlebar',(36,8),(36,16),radius_x=4)
        self.relate('connect','fork','handlebar');self.relate('connect','frame','seat-tube')

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
