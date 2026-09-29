from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b4a39a92-59f3-4333-bba3-da6c75735b50'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__holly-leaves-and-berries/20260929T033507Z-thuan-mac/reference/mistletoe_b4a39a92-59f3-4333-bba3-da6c75735b50.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore pointed toothed holly leaves and a joined cluster of three outlined berries.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'holly-leaves-and-berries'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('mistletoe',)

    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,x,y,w,h,r=0):
        if not r:
            self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for j in range(8):
            a,b=pts[j],pts[(j+1)%8]
            if j%2:self.add_arc(n+str(j),a,b,radius_x=r)
            else:self.add_line(n+str(j),a,b)
        self.add_contour(n,*(n+str(j) for j in range(8)),closed=True)
    def curve(self,n,start,*segments):
        self.add_bezier(n,start,*segments)

    def build(self):
        # Two pointed serrated leaves, mirrored only in their shared overall structure.
        self.add_polyline('leaf-left',(20,29),(11,27),(10,22),(5,18),(5,6),(16,7),(20,12),(23,13),(24,24))
        self.add_polyline('leaf-right',(28,29),(37,27),(38,22),(43,18),(43,6),(32,7),(28,12),(25,13),(24,24))
        self.add_line('vein-left',(11,13),(19,23))
        self.add_line('vein-right',(37,13),(29,23))
        self.circle('berry-top',24,30,5)
        self.circle('berry-left',18,39,5)
        self.circle('berry-right',30,39,5)
