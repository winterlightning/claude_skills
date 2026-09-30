"""Tilt pinky outward and clarify palm.
Symbol plan: Source three extended digits: upright index, splayed pinky and thumb; coherent rounded contour.
Keyshape VRECT_L; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '407c218e-c29c-4f30-b87f-c44424fce8df'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__extended-thumb-two-fingers/20260929T104736Z-thuan-mac/reference/pinkie_407c218e-c29c-4f30-b87f-c44424fce8df.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'extended-thumb-two-fingers'
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

        bez('thumb',(16,44),((16,37),(8,32),(8,25)),((8,21),(11,20),(14,23)))
        line('thumb-inner',(14,23),(18,27))
        line('index-left',(18,27),(18,8));arc('index-tip',(18,8),(26,8),4)
        line('index-right',(26,8),(26,25))
        arc('folded',(26,25),(34,25),4,s=False)
        line('pinky-left',(34,25),(32,16));arc('pinky-tip',(32,16),(40,16),4)
        line('pinky-right',(40,16),(40,30))
        bez('palm',(40,30),((40,36),(35,39),(34,44)))
        contour('hand','thumb','thumb-inner','index-left','index-tip','index-right','folded','pinky-left','pinky-tip','pinky-right','palm')
