"""Lengthen the cob and lower the husks, retaining kernel divisions.
Symbol plan: Pointed husk contours mirrored around x24; lower leaves expose elongated cob.
Keyshape VRECT_L; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '509d8c81-aff0-4d15-9237-c757ac95069a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__corn-cob-in-open-husk/20260929T104519Z-thuan-mac/reference/cob_509d8c81-aff0-4d15-9237-c757ac95069a.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'corn-cob-in-open-husk'
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

        arc('top',(16,12),(32,12),8)
        line('right',(32,12),(32,27));line('left',(16,27),(16,12))
        contour('cob','left','top','right')
        line('kernels',(16,15),(32,15));join('kernels','cob')
        bez('husk-left',(24,44),((10,44),(8,37),(8,27)),((18,29),(24,35),(24,44)))
        bez('husk-right',(24,44),((24,35),(30,29),(40,27)),((40,37),(38,44),(24,44)))
        join('husk-left','husk-right');join('cob','husk-left');join('cob','husk-right')
