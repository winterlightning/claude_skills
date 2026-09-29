from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '596e6132-95b1-5029-af21-f95f50a7587b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__restaurant-table-two-chairs-front/20260929T043927Z-thuan-mac/reference/table restaurant_596e6132-95b1-5029-af21-f95f50a7587b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'restaurant-table-two-chairs-front'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('table restaurant',)

    # Revision plan: The chairs were reduced to inward hooks and the table was undersized. Restore matching seats, backs and legs around a broader pedestal table.
    def build(self):

        # Mirrored chairs share seat height and leg lengths; central pedestal table.
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            n='chair-'+str(side)
            self.add_polyline(n,p(20,8),p(18,27),p(10,27),p(10,40))
            self.add_line(n+'-leg',p(18,27),p(18,40))
            self.relate('connect',n,n+'-leg')
        self.add_line('tabletop',(15,19),(33,19))
        self.add_line('pedestal',(24,19),(24,40))
        self.add_line('foot',(22,40),(26,40))
        self.relate('connect','tabletop','pedestal');self.relate('connect','pedestal','foot')

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
