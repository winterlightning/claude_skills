"""Raise the bent knee and lifted foot while preserving head gap.
Symbol plan: Shared full_body_ref.png circular head, exact 4px head/torso gap; intentional dance asymmetry.
Keyshape SQUARE; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '771cdf79-e59d-4541-bdff-a58073f629be'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dancer-with-raised-arm-and-bent-knee/20260929T104736Z-thuan-mac/reference/dancer_771cdf79-e59d-4541-bdff-a58073f629be.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'dancer-with-raised-arm-and-bent-knee'
    keyshape = Keyshape.SQUARE
    category = "objects"
    human_construction = "bust"
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ()
    keywords = ()
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def bez(n,a,*segs): self.add_bezier(n,a,*segs)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,k=2):
            pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k),(l+k,t)]
            names=[]
            for i,(a,z) in enumerate(zip(pts,pts[1:])):
                if a==z: continue
                m=n+str(i); names.append(m)
                if i%2: arc(m,a,z,k)
                else: line(m,a,z)
            contour(n,*names,closed=True)

        circle('head',24,11,5)
        line('torso',(24,24),(24,32))
        line('left-arm',(6,28),(24,24))
        line('arm-start',(24,24),(34,24));bez('raised-arm',(34,24),((41,24),(42,16),(42,6)))
        join('arm-start','raised-arm');join('torso','arm-start');join('torso','left-arm')
        line('standing-leg',(24,32),(17,42));poly('lifted-leg',(24,32),(36,34),(34,38))
        join('standing-leg','torso');join('lifted-leg','torso');join('standing-leg','lifted-leg')
        self.mark_human_figure('dancer',head='head',torso='torso',torso_junction='start')
