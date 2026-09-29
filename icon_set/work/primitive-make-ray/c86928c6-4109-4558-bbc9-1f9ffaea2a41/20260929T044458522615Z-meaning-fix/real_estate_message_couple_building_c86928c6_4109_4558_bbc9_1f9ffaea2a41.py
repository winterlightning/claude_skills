from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c86928c6-4109-4558-bbc9-1f9ffaea2a41'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__real-estate-message-couple-building/20260929T043927Z-thuan-mac/reference/real estate message couple building_c86928c6-4109-4558-bbc9-1f9ffaea2a41.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'real-estate-message-couple-building'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('real estate message couple building',)

    # Revision plan: The house inside the speech bubble became a chevron and the couple became tiny face dots. Restore a complete house and two broader busts.
    def build(self):

        # Speech bubble above two equal busts; intentionally compact complete house inside.
        self.add_polyline('bubble',(9,4),(39,4),(39,23),(27,23),(22,28),(22,23),(9,23),closed=True)
        self.add_polyline('house',(17,14),(24,8),(31,14),(29,14),(29,20),(19,20),(19,14),closed=True)
        for x in (12,36):
            self.circle('head-'+str(x),x,32,3)
            self.curve('shoulders-'+str(x),(x-7,44),((x-7,42),(x-4,43),(x,43)),((x+4,43),(x+7,42),(x+7,44)))

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
