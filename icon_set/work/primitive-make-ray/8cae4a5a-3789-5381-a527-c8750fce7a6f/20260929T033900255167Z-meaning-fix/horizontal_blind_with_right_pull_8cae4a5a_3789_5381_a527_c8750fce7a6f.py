from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8cae4a5a-3789-5381-a527-c8750fce7a6f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-blind-with-right-pull/20260929T033507Z-thuan-mac/reference/blinds horizontal closed_8cae4a5a-3789-5381-a527-c8750fce7a6f.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore a shallow header, three evenly spaced horizontal slats, light guide structure and right cord with circular pull.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'horizontal-blind-with-right-pull'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('blinds horizontal closed',)

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
        self.rect('header',6,5,36,7,1)
        for y in (20,28,36):self.add_line('slat-'+str(y),(7,y),(41,y))
        self.add_line('guide',(37 if False else 11,12),(37 if False else 11,36))
        self.add_line('cord',(10 if False else 38,12),(10 if False else 38,40))
        self.circle('pull',10 if False else 38,43,3)

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The shallow header, horizontal slats and right cord pull need compact structure and a small circular pull opening. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'd52d86e592478aa9b4ddcdae6c8441445ae1d25b30dc302cf7fffd8510cb0c07'}
