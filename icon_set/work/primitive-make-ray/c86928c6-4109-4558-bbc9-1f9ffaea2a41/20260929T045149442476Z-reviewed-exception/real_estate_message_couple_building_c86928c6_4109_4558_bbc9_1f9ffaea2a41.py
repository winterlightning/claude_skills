from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c86928c6-4109-4558-bbc9-1f9ffaea2a41'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__real-estate-message-couple-building/20260929T043927Z-thuan-mac/reference/real estate message couple building_c86928c6-4109-4558-bbc9-1f9ffaea2a41.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': "Preserve a complete house inside a speech bubble and two detached-head busts. This dense scene needs the wider envelope and smaller bubble-to-house and bubble-to-head clearances; each head retains 4 units of visible clearance to its shoulders. Visually reviewed at 48px in light and dark themes under the user's explicit delegated exception authorization.", 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '984e9b6d86316af77cfa874fa335eda588180118b195335b002ee86757db1ee6'}
    icon_id = 'real-estate-message-couple-building'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('real estate message couple building',)

    # Revision plan: The house inside the speech bubble became a chevron and the couple became tiny face dots. Restore a complete house and two broader busts.
    def build(self):

        # Keep a complete house within the bubble and independently readable paired busts.
        self.add_polyline('bubble',(5,2),(43,2),(43,25),(28,25),(24,29),(24,25),(5,25),closed=True)
        self.add_polyline('house',(16,15),(24,8),(32,15),(29,15),(29,19),(19,19),(19,15),closed=True)
        for x in (12,36):
            self.circle('head-'+str(x),x,33,3)
            self.curve('shoulders-'+str(x),(x-7,46),((x-7,45),(x-4,44),(x,44)),((x+4,44),(x+7,45),(x+7,46)))

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
