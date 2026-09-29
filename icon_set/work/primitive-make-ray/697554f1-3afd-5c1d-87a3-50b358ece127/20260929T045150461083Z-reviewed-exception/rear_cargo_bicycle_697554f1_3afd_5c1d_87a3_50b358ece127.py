from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '697554f1-3afd-5c1d-87a3-50b358ece127'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rear-cargo-bicycle/20260929T043927Z-thuan-mac/reference/bike cargo back_697554f1-3afd-5c1d-87a3-50b358ece127.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': "Preserve cargo-box placement and bicycle frame crossing the wheels naturally. Wheel/frame intersections and small enclosed chassis spaces are intentional physical structure, not unrelated collisions. Visually reviewed at 48px in light and dark themes under the user's explicit delegated exception authorization.", 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '84c3ca98d540509959ce315d3c6d69e96f5c186cb807ccfbf594b7585fbfea79'}
    icon_id = 'rear-cargo-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('bike cargo back',)

    # Revision plan: The cargo bike lost its frame and broad rear box; the box looked like a sign on a pole. Restore a cargo box over the rear wheel and a connected bicycle frame.
    def build(self):

        # Equal wheels, a triangular chassis, rear cargo box and higher handlebar.
        for x in (12,36): self.circle('wheel-'+str(x),x,32,8)
        self.rect('cargo',4,8,16,12,2)
        self.add_polyline('frame',(12,32),(23,32),(32,20),(18,20),(23,32))
        self.add_polyline('fork',(36,32),(32,20),(29,8),(35,8))
        self.add_line('seat-post',(18,20),(18,24))
        self.relate('connect','cargo','frame')
        # Fork crosses the wheel as a physical spoke; no false connection waiver.
        self.relate('connect','frame','seat-post')

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
