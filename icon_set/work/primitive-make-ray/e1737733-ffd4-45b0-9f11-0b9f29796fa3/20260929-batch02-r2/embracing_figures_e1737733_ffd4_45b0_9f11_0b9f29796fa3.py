"""Wrap a curved embracing arm across foreground person.
Symbol plan: Shared human user.svg circular heads; hugging arm curves over foreground torso.
Keyshape VRECT_L; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e1737733-ffd4-45b0-9f11-0b9f29796fa3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__embracing-figures/20260929T104736Z-thuan-mac/reference/hug_e1737733-ffd4-45b0-9f11-0b9f29796fa3.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'embracing-figures'
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

        circle('rear-head',18,11,7);circle('front-head',34,24,5)
        arc('rear-shoulder',(8,32),(18,22),10)
        line('rear-side',(8,32),(8,44));contour('rear-body','rear-side')
        join('rear-side','rear-shoulder');join('rear-head','rear-shoulder')
        bez('arm',(8,32),((14,42),(25,44),(32,42)))
        join('arm','rear-side');join('arm','rear-shoulder')
        arc('front-shoulder',(28,39),(40,39),6,6)
        join('front-shoulder','front-head')
        line('front-side',(40,39),(40,44));join('front-side','front-shoulder')
