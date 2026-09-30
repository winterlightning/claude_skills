"""Give the register a deeper body, drawer and clearer display.
Symbol plan: Lucide calculator: evenly spaced keypad marks and rounded display.
Keyshape SQUARE; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0c49b262-1334-4719-a58f-965ec30f28ad'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tilted-keypad-cash-register/20260929T104519Z-thuan-mac/reference/cash register_0c49b262-1334-4719-a58f-965ec30f28ad.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'tilted-keypad-cash-register'
    keyshape = Keyshape.SQUARE
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

        box('display',26,6,42,14,2)
        line('stem',(34,14),(34,22));join('stem','display')
        poly('body',(6,34),(12,22),(34,22),(36,22),(42,34),(42,42),(6,42),closed=True)
        join('stem','body')
        line('drawer',(6,34),(42,34));join('drawer','body')
        for x in (18,28): self.add_dot('key-'+str(x),(x,26))
