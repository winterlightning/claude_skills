from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b1e5658b-c303-4f04-bd4a-6e87cd1ca809'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rectangular-currency-banknote/20260929T043927Z-thuan-mac/reference/money bill_b1e5658b-c303-4f04-bd4a-6e87cd1ca809.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rectangular-currency-banknote'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('money bill',)

    # Revision plan: The banknote became a scalloped ticket. Restore a rectangular note with rounded corners, a central denomination medallion and balanced side marks.
    def build(self):

        # Lucide banknote construction: rounded bill, round denomination, two side marks.
        self.rect('bill',4,10,40,28,3)
        self.circle('denomination',24,24,4)
        for x in (12,36): self.add_dot('mark-'+str(x),(x,24))

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
