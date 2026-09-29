from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a7ad061e-a477-4a15-993d-a60fd5aa42f9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hiker-with-headlamp/20260929T033507Z-thuan-mac/reference/climbing head light_a7ad061e-a477-4a15-993d-a60fd5aa42f9.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore a leaning walking pose, slanted backpack, circular head and headlamp with two forward rays.
# Construction references: human_ref/full_body_ref.png: round head, single torso and bent limbs; intentional lean preserves hiking motion.
class Drawing(Solo48):
    icon_id = 'hiker-with-headlamp'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('climbing head light',)

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
        # Shared human full-body construction. r=4 head; neck (22,22) gives 5-12-13 distance from center (27,10), hence exact 4px ink gap.
        self.circle('head',27,10,5)
        self.add_line('headband',(22,9),(32,9))
        self.add_line('lamp-ray-upper',(37,7),(43,4))
        self.add_line('lamp-ray-lower',(37,13),(43,16))
        self.add_line('torso',(22,22),(17,32))
        self.add_polyline('arm',(22,22),(27,29),(34,31))
        self.add_polyline('front-leg',(17,32),(25,36),(25,44))
        self.add_polyline('rear-leg',(17,32),(14,39),(8,44))
        self.add_polyline('backpack',(16,18),(12,16),(7,26),(13,30))
        self.mark_human_figure('hiker',head='head',torso='torso',torso_junction='start')
