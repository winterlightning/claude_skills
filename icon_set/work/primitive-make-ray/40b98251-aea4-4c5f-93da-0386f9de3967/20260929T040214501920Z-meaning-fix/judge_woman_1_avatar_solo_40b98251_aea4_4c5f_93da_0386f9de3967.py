from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '40b98251-aea4-4c5f-93da-0386f9de3967'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__judge-woman-1-avatar-solo/20260929T035453Z-thuan-mac/reference/judge woman_40b98251-aea4-4c5f-93da-0386f9de3967.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore long outward-turning hair, a parted hairline, circular jaw and judicial robe collar.
# Construction references: human_ref/user.svg and human-reference.md: circular jaw, broad shoulders and touching-ink portrait construction; source owns long parted hair and collar.
class Drawing(Solo48):
    icon_id = 'judge-woman-1-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('judge woman',)
    human_construction = "bust"

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
        # Portrait: circular r9 jaw, shoulders at y30 touch the jaw ink at y28.
        self.add_arc('jaw',(15,17),(33,17),radius_x=9,sweep=False)
        self.curve('parted-hairline',(33,17),((29,17),(26,13),(24,11)),((22,14),(18,17),(15,17)))
        self.add_contour('face','jaw','parted-hairline',closed=True)
        self.curve('hair',(12,33),((10,32),(8,31),(6,30)),((10,24),(9,21),(9,16)),((9,0),(39,0),(39,16)),((39,21),(38,24),(42,30)),((40,31),(38,32),(36,33)))
        self.curve('shoulders',(6,44),((8,33),(14,30),(24,30)),((34,30),(40,33),(42,44)))
        self.add_polyline('collar',(18,31),(24,38),(30,31))
        self.add_line('robe-front',(24,38),(24,44))
        self.relate('connect','face','shoulders')
        self.relate('connect','collar','robe-front')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The long parted hair, circular jaw and robe collar need compact portrait spacing. The jaw and shoulders retain exactly zero visible ink gap. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '74bdc891cf8789b92a961ac2a1aca0960e542e293e90d017b55c2ce03d4d7660'}
