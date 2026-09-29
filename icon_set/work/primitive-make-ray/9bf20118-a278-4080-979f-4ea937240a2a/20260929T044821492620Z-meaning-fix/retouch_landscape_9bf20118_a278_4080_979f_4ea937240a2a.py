from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9bf20118-a278-4080-979f-4ea937240a2a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__retouch-landscape/20260929T043927Z-thuan-mac/reference/retouch landscape_9bf20118-a278-4080-979f-4ea937240a2a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'retouch-landscape'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('retouch landscape',)

    # Revision plan: The retouch cue became disconnected dots and a slash over a generic mountain. Restore a landscape frame with sun, mountain range and a clear sparkle at the editing corner.
    def build(self):

        # A detached retouch wand and four-point glint above the landscape's open corner.
        self.add_polyline('frame',(24,12),(6,12),(6,42),(42,42),(42,32))
        self.circle('sun',15,22,3)
        self.add_polyline('mountains',(12,36),(20,29),(25,35),(31,28),(37,36))
        self.add_line('wand',(29,17),(39,27))
        self.add_polyline('glint',(38,3),(40,8),(45,10),(40,12),(38,17),(36,12),(31,10),(36,8),closed=True)

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
