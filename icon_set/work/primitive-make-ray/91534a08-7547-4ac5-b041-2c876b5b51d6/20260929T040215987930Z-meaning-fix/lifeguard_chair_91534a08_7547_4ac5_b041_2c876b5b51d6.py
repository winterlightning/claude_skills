from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '91534a08-7547-4ac5-b041-2c876b5b51d6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__lifeguard-chair/20260929T035453Z-thuan-mac/reference/swimming lifeguard_91534a08-7547-4ac5-b041-2c876b5b51d6.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore an elevated ladder chair, seated figure with bent leg and two rows of water waves.
# Construction references: human_ref/full_body_ref.png: outlined round head, coherent seated torso and bent leg; source owns the tall chair and two water rows.
class Drawing(Solo48):
    icon_id = 'lifeguard-chair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    aliases = ()
    keywords = ('swimming lifeguard',)

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
        # Stick figure: r4 at (14,8), torso starts (14,20), so head/body ink gap is exactly 4.
        self.circle('head',14,8,4)
        self.add_line('torso',(14,20),(14,26))
        self.add_polyline('seated-leg',(14,26),(22,26),(28,34))
        self.add_polyline('chair',(6,20),(8,28),(21,28))
        self.add_line('left-chair-leg',(8,28),(4,44))
        self.add_line('right-chair-leg',(21,28),(24,44))
        self.add_line('rung-upper',(7,34),(22,34))
        self.add_line('rung-lower',(5,40),(23,40))
        for y in (39,45):
         self.curve('water-'+str(y),(28,y),((31,y),(33,y-2),(34,y-3)),((37,y),(41,y),(44,y-3)))
        self.mark_human_figure('lifeguard',head='head',torso='torso',torso_junction='start')
        self.relate('connect','torso','seated-leg')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The seated person, elevated ladder chair and two water rows need compact scene spacing. The detached head-to-torso ink gap remains exactly 4px. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'e3b3c253c4a68ba0a43e71829477e4026fecf9c3d8ff282b720653d8c0785515'}
