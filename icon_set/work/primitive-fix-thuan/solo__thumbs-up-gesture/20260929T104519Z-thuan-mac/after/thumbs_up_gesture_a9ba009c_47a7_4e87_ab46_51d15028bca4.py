"""Round the thumb and palm and articulate the finger edge.
Symbol plan: Lucide thumbs-up: smooth thumb transition and continuous palm contour.
Keyshape SQUARE; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a9ba009c-47a7-4e87-ab46-51d15028bca4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thumbs-up-gesture/20260929T104519Z-thuan-mac/reference/thumb up like sparkle_a9ba009c-47a7-4e87-ab46-51d15028bca4.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'thumbs-up-gesture'
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

        poly('wrist',(14,24),(6,24),(6,40),(14,40))
        bez('thumb-rise',(14,24),((20,20),(22,13),(22,6)))
        arc('thumb-tip',(22,6),(30,14),8)
        line('thumb-inner',(30,14),(28,22))
        line('fingers-top',(28,22),(36,22))
        arc('fingers-round',(36,22),(42,28),6)
        line('fingers-side',(42,28),(42,34))
        arc('palm-corner',(42,34),(34,42),8)
        bez('palm',(34,42),((24,42),(18,40),(14,40)))
        contour('hand','thumb-rise','thumb-tip','thumb-inner','fingers-top','fingers-round','fingers-side','palm-corner','palm')
        join('wrist','hand')
        line('crease',(33,32),(42,32));join('crease','hand')
