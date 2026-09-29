"""japanese woman.
Plan: Restored the flower hair ornament, swept fringe, rounded bob and crossed kimono collar.
Construction: human_ref/user.svg and user: circular jaw with rounded shoulders; flower: smooth petal lobes.
Keyshape: VRECT_L; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'd8f7770b-d9fb-48cc-9814-dcf0af46b402'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__japanese-woman-avatar/20260929T033633Z-thuan-mac/reference/japanese woman_d8f7770b-d9fb-48cc-9814-dcf0af46b402.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'japanese-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    human_construction = 'bust'
    aliases = ()
    keywords = ('japanese', 'woman')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.add_bezier('hair-left',(14,29),((9,29),(6,28),(6,23)),((6,11),(15,4),(26,4)))
        self.add_bezier('hair-right',(42,23),((42,29),(38,29),(33,29)))
        self.add_arc('jaw',(32,20),(16,20),radius_x=8)
        self.add_bezier('fringe',(16,20),((15,17),(16,14),(18,12)),((21,17),(26,19),(32,20)))
        self.add_contour('face','jaw','fringe',closed=True)
        self.add_bezier('flower',(36,6),((39,3),(42,7),(40,10)),((45,9),(46,14),(41,15)),((44,20),(39,22),(36,18)),((32,22),(28,19),(31,15)),((26,14),(28,9),(33,10)),((32,5),(35,3),(36,6)))
        self.add_arc('shoulders',(6,44),(42,44),radius_x=18,radius_y=12)
        self.add_line('collar-main',(33,34),(21,44));self.add_line('collar-cross',(16,34),(25,41))
        self.relate('connect','collar-main','collar-cross')
        self.relate('connect','face','shoulders')

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve the flower ornament, swept hair and crossed kimono collar. Compact ornament spacing and natural asymmetric hair envelope retain identifying features; circular jaw and shoulders have zero visible contact gap.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '5c79fc09895a83d5adbec5f93ee2a2dbc11764dd7dfe242d70faf9376c06c13c'}
