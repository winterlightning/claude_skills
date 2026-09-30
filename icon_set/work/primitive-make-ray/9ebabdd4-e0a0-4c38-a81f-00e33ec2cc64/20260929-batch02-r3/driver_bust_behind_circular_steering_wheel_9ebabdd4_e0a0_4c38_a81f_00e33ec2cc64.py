"""Enlarge head and wheel; use steering spoke.
Symbol plan: Shared user.svg circular head and broad bust. Steering wheel with vertical spoke.
Keyshape VRECT_L; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9ebabdd4-e0a0-4c38-a81f-00e33ec2cc64'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__driver-bust-behind-circular-steering-wheel/20260929T104736Z-thuan-mac/reference/driver_9ebabdd4-e0a0-4c38-a81f-00e33ec2cc64.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'driver-bust-behind-circular-steering-wheel'
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

        circle('head',24,9,5)
        arc('shoulder-left',(8,30),(20,18),12);line('shoulder-top',(20,18),(28,18));arc('shoulder-right',(28,18),(40,30),12)
        contour('body','shoulder-left','shoulder-top','shoulder-right');join('head','body')
        line('left-arm',(8,30),(16,36));line('right-arm',(40,30),(32,36))
        join('left-arm','body');join('right-arm','body')
        circle('wheel',24,36,8);join('wheel','left-arm');join('wheel','right-arm')
