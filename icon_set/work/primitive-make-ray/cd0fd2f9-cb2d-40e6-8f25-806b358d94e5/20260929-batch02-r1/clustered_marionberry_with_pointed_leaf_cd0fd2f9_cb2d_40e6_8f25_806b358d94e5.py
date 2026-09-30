"""Restore a structured berry cluster and preserve the pointed upper-right leaf.
Symbol plan: Lucide grape and leaf: coherent lobes, internal berry cells and pointed leaf.
Keyshape VRECT_L; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cd0fd2f9-cb2d-40e6-8f25-806b358d94e5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__clustered-marionberry-with-pointed-leaf/20260929T104519Z-thuan-mac/reference/marionberry_cd0fd2f9-cb2d-40e6-8f25-806b358d94e5.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'clustered-marionberry-with-pointed-leaf'
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

        arc('top-left',(24,24),(8,24),8,s=False)
        arc('left-side',(8,24),(16,32),8,s=False)
        arc('base',(16,36),(32,36),8,s=False)
        line('lower-left',(16,32),(16,36))
        line('lower-right',(32,36),(32,32))
        arc('right-side',(32,32),(40,24),8,s=False)
        arc('top-right',(40,24),(24,24),8,s=False)
        contour('berry','top-left','left-side','lower-left','base','lower-right','right-side','top-right',closed=True)
        poly('cells',(16,32),(24,24),(32,32));join('cells','berry')
        bez('leaf',(24,16),((24,8),(32,4),(40,4)),((40,12),(36,16),(32,16)))
        join('leaf','berry')
