from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'eb47004b-f404-423b-86db-835fad7f0bcb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__redux-three-lobed-emblem/20260929T043927Z-thuan-mac/reference/redux logo_eb47004b-f404-423b-86db-835fad7f0bcb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'redux-three-lobed-emblem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('redux logo',)

    # Revision plan: The Redux paths were disconnected and flattened into a generic S. Restore the three orbiting lobes and three hollow endpoint nodes.
    def build(self):

        # Three smooth lobes arranged asymmetrically around three endpoint circles.
        self.circle('upper-node',22,19,3)
        self.circle('left-node',16,33,3)
        self.circle('right-node',33,29,3)
        self.curve('upper-lobe',(16,30),((7,17),(13,6),(23,6)),((31,6),(35,11),(36,15)))
        self.curve('right-lobe',(25,19),((42,19),(47,36),(36,41)),((32,43),(28,42),(26,41)))
        self.curve('lower-lobe',(33,32),((23,46),(3,43),(6,29)),((6,26),(8,24),(9,23)))

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
