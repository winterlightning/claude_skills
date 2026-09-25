"""A horizontal lens barrel widens from its rear mount toward an oval front. Wide envelope follows the barrel axis. Lucide telescope informs the stepped optical tube; a full oval front preserves the side view. Fine focus-ring ribs are omitted and the ring is expressed by a barrel seam."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6cf2782-fc66-4fca-b290-0ffad68032d9'
SOURCE_PATH = 'pictographic-primitives/photography/lens horizontal_d6cf2782-fc66-4fca-b290-0ffad68032d9.svg'
AUTHOR = 'gpt-6'

class TelephotoLensSideView(Solo48):
    icon_id = 'telephoto-lens-side-view'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('lens', 'telephoto', 'zoom', 'camera lens', 'optics', 'photography', 'barrel', 'side view')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def segments(n,*p):
            for j,(a,b) in enumerate(zip(p,p[1:]),1):line(n+'-'+str(j),a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'-top',(x-r,y),(x+r,y),r)
            arc(n+'-bottom',(x+r,y),(x-r,y),r)
            contour(n,n+'-top',n+'-bottom',closed=True)

        segments('barrel-top',(4,18),(12,8),(18,8),(36,8))
        arc('front-right',(36,8),(36,40),8,16)
        segments('barrel-bottom',(36,40),(18,40),(12,40),(4,30))
        line('rear',(4,30),(4,18))
        contour('outline','barrel-top-1','barrel-top-2','barrel-top-3','front-right','barrel-bottom-1','barrel-bottom-2','barrel-bottom-3','rear',closed=True)
        arc('front-left',(36,40),(36,8),8,16);connect('front-left','outline')
        line('focus-ring',(18,8),(18,40));connect('focus-ring','outline')
