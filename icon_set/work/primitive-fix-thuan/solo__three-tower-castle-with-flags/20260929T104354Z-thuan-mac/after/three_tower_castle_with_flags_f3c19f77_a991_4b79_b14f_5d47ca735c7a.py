'Raised a longer flagstaff with a turned pennant edge, staggered the three roofs and preserved the clear central doorway.\nOriginal/current comparison: The rejected central flag is just a short bar and the towers have cramped roof-to-wall proportions.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide castle original/atomic-debug for coherent wall and doorway construction; original supplies the three pointed towers.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f3c19f77-a991-4b79-b14f-5d47ca735c7a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-tower-castle-with-flags/20260929T104354Z-thuan-mac/reference/amusement park castle_f3c19f77-a991-4b79-b14f-5d47ca735c7a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-tower-castle-with-flags'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('three', 'tower', 'castle', 'with', 'flags')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
        def path(n,start,steps,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{i}';members.append(m)
                if kind=='L': line(m,here,end)
                elif kind=='A': arc(m,here,end,*args)
                elif kind=='C': bez(m,here,(args[0],args[1],end))
                here=end
            con(n,*members,closed=closed)
        def rect(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad),('L',(r,b-rad)),('A',(r-rad,b),rad),('L',(l+rad,b)),('A',(l,b-rad),rad),('L',(l,t+rad)),('A',(l+rad,t),rad)],True)

        poly('walls',(6,34),(6,42),(18,42),(18,34),(30,34),(30,42),(42,42),(42,34),(30,34),(30,26),(18,26),(18,34),closed=True)
        poly('roof-left',(6,34),(12,24),(18,34));join('roof-left','walls')
        poly('roof-right',(30,34),(36,24),(42,34));join('roof-right','walls')
        poly('roof-middle',(18,26),(24,16),(30,26));join('roof-middle','walls')
        poly('flag',(24,16),(24,6),(34,6),(34,10));join('flag','roof-middle')
