"""Restore prominent eye rings, distinct ears and muzzle.
Symbol plan: No useful Lucide species match; source eye rings and ears with shared mirrored geometry.
Keyshape HRECT_L; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6b0fa457-2293-4b0b-b837-f3484ee72ffc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cute-lemur-animal-face/20260929T104736Z-thuan-mac/reference/lemur_6b0fa457-2293-4b0b-b837-f3484ee72ffc.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'cute-lemur-animal-face'
    keyshape = Keyshape.HRECT_L
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

        bez('upper',(4,24),((4,20),(4,16),(4,14)),((4,6),(12,8),(16,12)),((20,10),(28,10),(32,12)),((36,8),(44,6),(44,14)),((44,16),(44,20),(44,24)))
        arc('lower-right',(44,24),(28,40),16);line('chin',(28,40),(20,40));arc('lower-left',(20,40),(4,24),16)
        contour('face','upper','lower-right','chin','lower-left',closed=True)
        circle('eye-left',16,22,4);circle('eye-right',32,22,4)
        self.add_dot('nose',(24,31))
