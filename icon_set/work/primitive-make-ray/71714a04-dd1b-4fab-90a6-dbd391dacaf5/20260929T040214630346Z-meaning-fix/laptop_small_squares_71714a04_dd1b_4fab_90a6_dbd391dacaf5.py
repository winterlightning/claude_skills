from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '71714a04-dd1b-4fab-90a6-dbd391dacaf5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__laptop-small-squares/20260929T035453Z-thuan-mac/reference/laptop small squares_71714a04-dd1b-4fab-90a6-dbd391dacaf5.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore two small outlined squares in a vertical column inside a clear laptop screen.
# Construction references: Lucide laptop: screen with consistent rounded corners and a broad lower deck.
class Drawing(Solo48):
    icon_id = 'laptop-small-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'other'
    aliases = ()
    keywords = ('laptop small squares',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,x,y,w,h,r=0):
        if not r:
            self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for j in range(8):
            if j%2:self.add_arc(n+str(j),pts[j],pts[(j+1)%8],radius_x=r)
            else:self.add_line(n+str(j),pts[j],pts[(j+1)%8])
        self.add_contour(n,*(n+str(j) for j in range(8)),closed=True)
    def curve(self,n,start,*segments):
        self.add_bezier(n,start,*segments)

    def build(self):
        self.rect('screen',8,6,32,28,3)
        for y in (13,24):self.rect('tile-'+str(y),15,y,6,6)
        self.add_polyline('base',(8,34),(6,42),(42,42),(40,34))
        self.relate('connect','screen','base')
