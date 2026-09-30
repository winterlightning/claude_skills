"""Enlarge eye curves and frown; draw pointed tear.
Symbol plan: Lucide-like facial arcs, source-specific tear arrangement.
Keyshape CIRCLE; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cb57b7db-4e36-492c-979b-5c7f2457c852'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crying-face-with-single-tear/20260929T104736Z-thuan-mac/reference/face sad cry_cb57b7db-4e36-492c-979b-5c7f2457c852.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'crying-face-with-single-tear'
    keyshape = Keyshape.CIRCLE
    category = "objects"
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

        circle('face',24,24,20)
        arc('eye-left',(14,16),(20,16),3,2,s=False)
        arc('eye-right',(28,16),(34,16),3,2,s=False)
        arc('mouth',(24,34),(34,34),5,4)
        bez('tear',(16,26),((14,29),(12,30),(12,32)),((12,36),(20,36),(20,32)),((20,30),(18,29),(16,26)))
