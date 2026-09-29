from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a3acc8b0-54db-4bd5-a00e-eb2c72c03c16'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__remaining-range-indicator/20260929T043927Z-thuan-mac/reference/e car battery driving length 1_a3acc8b0-54db-4bd5-a00e-eb2c72c03c16.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'remaining-range-indicator'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('e car battery driving length 1',)

    # Revision plan: The number 10 became a bar and dot, and the battery became an angular bracket. Restore the range number, leftward distance arrow and battery silhouette.
    def build(self):

        # Preserve 10 at upper left, battery lower right, arrow to left boundary.
        self.add_polyline('one',(7,6),(10,6),(10,18))
        self.add_line('one-foot',(6,18),(14,18));self.relate('connect','one','one-foot')
        self.rect('zero',20,6,8,12,4)
        self.add_polyline('battery',(31,28),(31,24),(35,24),(35,20),(41,20),(41,24),(44,24),(44,42),(31,42),(31,36))
        self.add_line('distance',(10,32),(36,32))
        self.add_polyline('arrow',(16,26),(10,32),(16,38))
        self.relate('connect','distance','arrow')
        self.add_line('limit',(4,26),(4,38))

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
