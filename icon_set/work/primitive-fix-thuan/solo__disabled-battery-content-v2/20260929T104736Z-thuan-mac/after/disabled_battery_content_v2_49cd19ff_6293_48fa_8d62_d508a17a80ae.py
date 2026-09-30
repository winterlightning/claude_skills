"""Attach outlined terminal and preserve disabling slash.
Symbol plan: Lucide battery: rounded casing and attached terminal; source disabling diagonal.
Keyshape HRECT_M; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '49cd19ff-6293-48fa-8d62-d508a17a80ae'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__disabled-battery-content-v2/20260929T104736Z-thuan-mac/reference/slash battery_49cd19ff-6293-48fa-8d62-d508a17a80ae.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'disabled-battery-content-v2'
    keyshape = Keyshape.HRECT_M
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

        poly('body',(4,38),(4,10),(34,10),(34,18),(34,30),(34,38),closed=True)
        poly('terminal',(34,18),(44,18),(44,30),(34,30));join('terminal','body')
        line('slash',(4,38),(34,10));join('slash','body')
