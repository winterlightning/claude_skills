"""Separate dome and circular jaw with full brim and restore closed panel.
Symbol plan: Shared human user.svg: circular jaw and broad shoulders. Hard hat dome and full brim.
Keyshape VRECT_L; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cc025368-b3c0-4db5-9628-aeeb0bb29471'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__construction-worker-with-safety-helmet/20260929T104736Z-thuan-mac/reference/engineer project superviser 2_cc025368-b3c0-4db5-9628-aeeb0bb29471.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'construction-worker-with-safety-helmet'
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

        arc('dome',(14,14),(34,14),10)
        poly('brim',(8,14),(14,14),(34,14),(40,14));join('dome','brim')
        arc('jaw',(14,14),(34,14),10,s=False);join('jaw','brim');join('jaw','dome')
        arc('shoulders',(8,40),(40,40),16,12);join('shoulders','jaw')
        poly('body',(8,40),(8,44),(40,44),(40,40));join('body','shoulders')
