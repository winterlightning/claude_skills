from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '32ab4ed8-b548-4a61-956b-a99332d1684d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__headphones-with-portable-player/20260929T033507Z-thuan-mac/reference/walkman headphones_32ab4ed8-b548-4a61-956b-a99332d1684d.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore two earcups, an overhead arch and a player with screen division and circular control.
# Construction references: Lucide headphones: arch tangent to earcups and matching earcup radii.
class Drawing(Solo48):
    icon_id = 'headphones-with-portable-player'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'music'
    aliases = ()
    keywords = ('walkman headphones',)

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
        self.curve('band',(5,27),((5,-3),(43,-3),(43,27)))
        self.rect('left-cup',4,24,6,10,3)
        self.rect('right-cup',38,24,6,10,3)
        self.rect('player',15,17,18,27,4)
        self.add_line('screen-rule',(15,25),(33,25))
        self.circle('control',24,34,3)

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The earcups, overhead band and detailed player need nested spacing and small control openings to remain recognizable. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'a63a8a468a6cbbd7d167cf40be547a1a56f5af77a48b2bd254d5b2668196eeb6'}
