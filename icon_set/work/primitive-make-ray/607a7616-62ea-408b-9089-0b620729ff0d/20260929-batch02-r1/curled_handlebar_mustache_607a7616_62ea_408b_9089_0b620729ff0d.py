"""Restore wide low moustache with pointed curled ends.
Symbol plan: No exact Lucide match. Mirrored low lobes and pointed upward curled tips.
Keyshape HRECT_M; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '607a7616-62ea-408b-9089-0b620729ff0d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curled-handlebar-mustache/20260929T104736Z-thuan-mac/reference/mustache 1_607a7616-62ea-408b-9089-0b620729ff0d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'curled-handlebar-mustache'
    keyshape = Keyshape.HRECT_M
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

        bez('moustache',(24,16),((20,8),(12,8),(10,16)),((8,20),(6,22),(4,20)),((4,32),(12,38),(18,36)),((21,35),(23,32),(24,30)),((25,32),(27,35),(30,36)),((36,38),(44,32),(44,20)),((42,22),(40,20),(38,16)),((36,8),(28,8),(24,16)))
