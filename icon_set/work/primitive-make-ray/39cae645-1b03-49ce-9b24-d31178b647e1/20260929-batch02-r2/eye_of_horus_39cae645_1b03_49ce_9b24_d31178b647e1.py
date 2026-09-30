"""Restore eyebrow and vertical cheek mark with curled flourish.
Symbol plan: Source Egyptian eye: brow, lens, descending cheek and curled flourish.
Keyshape HRECT_L; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '39cae645-1b03-49ce-9b24-d31178b647e1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__eye-of-horus/20260929T104736Z-thuan-mac/reference/eye of horus_39cae645-1b03-49ce-9b24-d31178b647e1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'eye-of-horus'
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

        bez('brow',(4,12),((12,10),(18,8),(24,8)),((30,8),(36,10),(44,12)))
        bez('eye-top',(4,24),((16,14),(32,14),(44,24)))
        bez('eye-bottom',(44,24),((32,34),(16,34),(4,24)))
        contour('eye','eye-top','eye-bottom',closed=True)
        line('iris',(24,17),(24,31));join('iris','eye')
        line('cheek',(36,29),(36,40));join('cheek','eye')
        bez('curl',(4,32),((4,40),(12,40),(16,40)),((22,40),(30,35),(36,29)))
        join('curl','eye');join('curl','cheek')
