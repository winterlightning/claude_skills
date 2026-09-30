"""Restore distinct earcups, circular face and shoulders.
Symbol plan: Shared user.svg circular jaw and shoulder proportions; explicit headset earcups.
Keyshape VRECT_L; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'be70bb88-f464-4645-872e-be780f9679ac'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__customer-support-agent/20260929T104736Z-thuan-mac/reference/headphones woman_be70bb88-f464-4645-872e-be780f9679ac.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'customer-support-agent'
    keyshape = Keyshape.VRECT_L
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

        arc('band',(8,20),(40,20),16)
        arc('head-top',(16,20),(32,20),8)
        arc('jaw',(32,20),(16,20),8)
        contour('head','head-top','jaw',closed=True)
        line('ear-left',(8,20),(8,28));line('ear-right',(40,20),(40,28))
        join('band','ear-left');join('band','ear-right')
        line('left',(8,44),(8,40));arc('shoulder-left',(8,40),(20,32),12,8)
        line('shoulder-top',(20,32),(28,32));arc('shoulder-right',(28,32),(40,40),12,8);line('right',(40,40),(40,44))
        contour('body','left','shoulder-left','shoulder-top','shoulder-right','right');join('head','body')
