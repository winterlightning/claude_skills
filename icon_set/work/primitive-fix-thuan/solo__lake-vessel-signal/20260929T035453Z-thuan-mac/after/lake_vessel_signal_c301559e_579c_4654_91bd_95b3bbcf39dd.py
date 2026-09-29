from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c301559e-579c-4654-91bd-95b3bbcf39dd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__lake-vessel-signal/20260929T035453Z-thuan-mac/reference/lake formation_c301559e-579c-4654-91bd-95b3bbcf39dd.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore a deep curved hull, rim, three signal arcs and water beneath.
# Construction references: Original reference; no useful exact Lucide match. Smooth curves and shared geometric proportions are authored on SOLO48.
class Drawing(Solo48):
    icon_id = 'lake-vessel-signal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'programing'
    aliases = ()
    keywords = ('lake formation',)

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
        # Three nested signal arcs, a bowl-shaped hull and one continuous water stroke.
        for n,y,w,h in [('outer',8,10,6),('middle',13,6,4),('inner',18,2,2)]:
         self.curve('signal-'+n,(24-w,y),((24-w//2,y-h),(24+w//2,y-h),(24+w,y)))
        self.curve('back-left',(4,23),((5,20),(9,20),(13,19)))
        self.curve('back-right',(35,19),((39,20),(43,20),(44,23)))
        self.curve('rim',(4,23),((12,28),(36,28),(44,23)))
        self.curve('hull',(44,23),((42,40),(6,40),(4,23)))
        self.add_contour('vessel','rim','hull',closed=True)
        self.curve('water',(4,43),((8,43),(10,42),(12,40)),((17,44),(21,44),(24,40)),((29,44),(33,44),(36,40)),((39,42),(41,43),(44,43)))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The deep vessel, rim, three signal arcs and water require compact stacked spacing; removing a level would lose the source meaning. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'b9df64ca744345ea214759fd0dc9b44a58774324df60e8bf41cf0aa9d532a575'}
