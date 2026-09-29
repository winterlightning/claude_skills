from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6223f446-fea9-4888-9f8d-66b676fc6edf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__residential-car-house/20260929T043927Z-thuan-mac/reference/parking resident_6223f446-fea9-4888-9f8d-66b676fc6edf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'residential-car-house'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('parking resident',)

    # Revision plan: The foreground car looked like a bag and the house was only a roof arch. Restore a windshield, hood, wheels and a complete rear house.
    def build(self):

        self.add_polyline('house',(21,16),(31,6),(42,16),(42,33),(34,33),(34,23),(28,23))
        self.add_polyline('windshield',(6,30),(10,21),(22,21),(26,30))
        self.rect('car',4,30,24,10,3)
        self.add_line('left-wheel',(8,40),(8,43));self.relate('connect','car','left-wheel')
        self.add_line('right-wheel',(24,40),(24,43));self.relate('connect','car','right-wheel')
        self.relate('connect','windshield','car')
        for x in (10,22):self.add_dot('lamp-'+str(x),(x,35))

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
