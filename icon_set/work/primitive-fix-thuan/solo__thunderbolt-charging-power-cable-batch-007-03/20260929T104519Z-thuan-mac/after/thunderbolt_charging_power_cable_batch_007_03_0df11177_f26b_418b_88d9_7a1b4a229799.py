"""Restore connector tips and preserve the alternating cable bends.
Symbol plan: Lucide cable: unequal connectors with protruding ends and coherent S-shaped cord.
Keyshape SQUARE; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0df11177-f26b-418b-88d9-7a1b4a229799'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thunderbolt-charging-power-cable-batch-007-03/20260929T104519Z-thuan-mac/reference/thunderbolt cable_0df11177-f26b-418b-88d9-7a1b4a229799.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'thunderbolt-charging-power-cable-batch-007-03'
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

        box('plug-left',6,10,14,22,2)
        line('tip-left',(10,6),(10,10));join('tip-left','plug-left')
        line('cord-a',(10,22),(10,35));arc('cord-b',(10,35),(24,35),7,s=False)
        line('cord-c',(24,35),(24,13));arc('cord-d',(24,13),(38,13),7)
        line('cord-e',(38,13),(38,28))
        contour('cord','cord-a','cord-b','cord-c','cord-d','cord-e')
        box('plug-right',34,28,42,38,2)
        line('tip-right',(38,38),(38,42))
        join('tip-right','plug-right');join('cord','plug-left');join('cord','plug-right')
