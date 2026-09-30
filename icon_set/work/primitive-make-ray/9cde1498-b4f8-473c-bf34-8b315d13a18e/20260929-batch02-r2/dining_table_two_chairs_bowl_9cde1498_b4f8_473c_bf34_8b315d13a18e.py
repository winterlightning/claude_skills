"""Flatten bowl and restore two table legs.
Symbol plan: Source table uses two legs and shallow bowl; mirror chairs around x24.
Keyshape HRECT_L; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9cde1498-b4f8-473c-bf34-8b315d13a18e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dining-table-two-chairs-bowl/20260929T104736Z-thuan-mac/reference/lunchroom_9cde1498-b4f8-473c-bf34-8b315d13a18e.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'dining-table-two-chairs-bowl'
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

        for n,x,s in [('left',4,1),('right',44,-1)]:
            poly(n+'-back',(x,8),(x,32),(x,40))
            poly(n+'-seat',(x,32),(x+s*8,32),(x+s*8,40));join(n+'-back',n+'-seat')
        poly('top',(12,20),(20,20),(24,20),(28,20),(36,20))
        for x in (20,28):line('leg-'+str(x),(x,20),(x,40));join('leg-'+str(x),'top')
        bez('bowl',(16,10),((16,17),(20,20),(24,20)),((28,20),(32,17),(32,10)))
        line('rim',(16,10),(32,10));contour('dish','bowl','rim',closed=True);join('dish','top')
