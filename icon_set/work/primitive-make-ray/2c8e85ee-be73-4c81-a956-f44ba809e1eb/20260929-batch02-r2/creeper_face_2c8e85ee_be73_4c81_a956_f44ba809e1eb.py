"""Restore square eyes and broader angular mouth.
Symbol plan: No useful Lucide match for pixel identity. Square eye frames and stepped mouth on shared x24 axis.
Keyshape SQUARE; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2c8e85ee-be73-4c81-a956-f44ba809e1eb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__creeper-face/20260929T104736Z-thuan-mac/reference/video game logo creeper_2c8e85ee-be73-4c81-a956-f44ba809e1eb.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'creeper-face'
    keyshape = Keyshape.SQUARE
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

        poly('frame',(6,6),(42,6),(42,42),(6,42),closed=True)
        line('eye-left',(15,16),(19,16));line('eye-right',(29,16),(33,16))
        poly('mouth',(16,34),(16,26),(24,26),(32,26),(32,34))
        line('nose',(24,21),(24,26));join('nose','mouth')
