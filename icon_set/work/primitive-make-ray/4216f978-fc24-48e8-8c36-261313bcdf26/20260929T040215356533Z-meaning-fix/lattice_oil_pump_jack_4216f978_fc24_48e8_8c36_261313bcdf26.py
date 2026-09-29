from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4216f978-fc24-48e8-8c36-261313bcdf26'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__lattice-oil-pump-jack/20260929T035453Z-thuan-mac/reference/oil well_4216f978-fc24-48e8-8c36-261313bcdf26.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the slanted beam, curved horsehead, triangular lattice support, hanging rod and counterweight.
# Construction references: Original reference; no useful exact Lucide match. Smooth curves and shared geometric proportions are authored on SOLO48.
class Drawing(Solo48):
    icon_id = 'lattice-oil-pump-jack'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('oil well',)

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
        self.curve('horsehead',(15,4),((8,3),(3,20),(6,23)),((10,25),(19,7),(15,4)))
        self.add_polyline('beam',(14,12),(43,23),(41,28),(12,17))
        self.add_polyline('tower',(17,44),(26,18),(35,44))
        self.add_line('brace-a',(21,29),(32,39))
        self.add_line('brace-b',(31,29),(20,39))
        self.add_line('pump-rod',(7,23),(7,44))
        self.add_line('counterweight-rod',(40,28),(40,35))
        self.rect('counterweight',37,35,6,9)
        self.add_line('ground',(4,44),(44,44))
