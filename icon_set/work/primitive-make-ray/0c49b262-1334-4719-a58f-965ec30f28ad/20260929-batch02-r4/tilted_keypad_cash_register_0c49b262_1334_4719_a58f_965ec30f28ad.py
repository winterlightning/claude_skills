"""Give the register a deeper body, drawer and clearer display.
Symbol plan: Lucide calculator: spaced keypad marks; raised display and drawer.
Keyshape VRECT_L; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0c49b262-1334-4719-a58f-965ec30f28ad'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tilted-keypad-cash-register/20260929T104519Z-thuan-mac/reference/cash register_0c49b262-1334-4719-a58f-965ec30f28ad.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'tilted-keypad-cash-register'
    keyshape = Keyshape.VRECT_L
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

        box('display',24,4,40,12,2)
        line('stem',(32,12),(32,20));join('stem','display')
        poly('body',(8,36),(14,20),(32,20),(34,20),(40,36),(40,44),(8,44),closed=True)
        join('stem','body');line('drawer',(8,36),(40,36));join('drawer','body')
        for x in (20,28):self.add_dot('key-'+str(x),(x,28))
