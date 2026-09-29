from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bc2a6778-ef25-47fb-9edd-73d0b5963727'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__right-from-bracket/20260929T043927Z-thuan-mac/reference/right from bracket_bc2a6778-ef25-47fb-9edd-73d0b5963727.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'right-from-bracket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('right from bracket',)

    # Revision plan: The rightward exit arrow was trapped inside a closed box. Open the bracket on the right and extend the arrow out through it.
    def build(self):

        # Lucide log-out: open door bracket and arrow crossing its opening.
        self.add_polyline('bracket',(24,6),(6,6),(6,42),(24,42))
        self.add_line('shaft',(16,24),(42,24))
        self.add_polyline('arrow',(32,14),(42,24),(32,34))
        self.relate('connect','shaft','arrow')

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
