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
        self.add_line('beam',(12,14),(43,25))
        self.add_polyline('tower',(16,44),(26,21),(36,44))
        self.add_line('brace-a',(21,32),(32,43))
        self.add_line('brace-b',(31,32),(20,43))
        self.add_line('pump-rod',(7,23),(7,44))
        self.add_line('counterweight-rod',(40,24),(40,34))
        self.rect('counterweight',36,34,8,10)
        self.add_line('ground',(4,44),(44,44))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The pump jack needs a narrow lattice tower, cross braces, horsehead and counterweight; their small structural openings preserve the subject. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '29caa471a6d0f76889f006c99d0a42c9dcdd639af4f9020bc959160412c06f2e'}
