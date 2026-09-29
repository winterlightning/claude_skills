from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f53e79c7-b34f-44d2-9af3-49b5684cc631'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__real-estate-favorite-house-rating/20260929T043927Z-thuan-mac/reference/real estate favorite house rating_f53e79c7-b34f-44d2-9af3-49b5684cc631.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': "Preserve three recognizable five-point rating stars and the complete house. The small stars use compact solid silhouettes; their openings and rating-to-roof spacing need a visual exception. Visually reviewed at 48px in light and dark themes under the user's explicit delegated exception authorization.", 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '8eedb83aba0bef2e1d6d1c219eb1cd3dc8abb1dc6bdb8518e55eb42746649a4d'}
    icon_id = 'real-estate-favorite-house-rating'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('real estate favorite house rating',)

    # Revision plan: The two small rating stars became dots and the house was flattened. Restore three recognizable stars above an upright house.
    def build(self):

        # Rating owns one large star and a mirrored smaller pair; house retains door and pitched roof.
        self.star('rating',24,12,6)
        for x in (8,40): self.star('side-rating-'+str(x),x,16,4)
        self.add_polyline('roof',(8,31),(24,23),(40,31))
        self.add_polyline('house',(12,32),(12,42),(20,42),(20,34),(28,34),(28,42),(36,42),(36,32))

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
