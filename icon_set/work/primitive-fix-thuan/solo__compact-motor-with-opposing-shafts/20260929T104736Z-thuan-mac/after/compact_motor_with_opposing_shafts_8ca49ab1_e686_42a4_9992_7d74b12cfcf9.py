"""Restore taller rounded motor vents and rebalance casing.
Symbol plan: No exact local Lucide match. Shared casing radius and symmetric vents.
Keyshape VRECT_M; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8ca49ab1-e686-42a4-9992-7d74b12cfcf9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__compact-motor-with-opposing-shafts/20260929T104736Z-thuan-mac/reference/electronics motor_8ca49ab1-e686-42a4-9992-7d74b12cfcf9.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'compact-motor-with-opposing-shafts'
    keyshape = Keyshape.VRECT_M
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

        box('body',10,12,38,40,4)
        line('shaft-top',(24,4),(24,12));line('shaft-bottom',(24,40),(24,44))
        line('seam',(10,20),(38,20))
        for n in ('shaft-top','shaft-bottom','seam'):join(n,'body')
        for x in (20,28):line('vent-'+str(x),(x,29),(x,31))
