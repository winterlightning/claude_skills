from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4bd78193-76e7-4e65-b3e3-2a7e05a8553b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-chevron-left/20260925T034349Z-thuan-mac/reference/square chevron left_4bd78193-76e7-4e65-b3e3-2a7e05a8553b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-chevron-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # Square frame enclosing the conventional symbol named by the concept; misleading reference content replaced.
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*p,closed=False): self.add_contour(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,k=4):
            line(n+'t',(l+k,t),(r-k,t));arc(n+'tr',(r-k,t),(r,t+k),k)
            line(n+'r',(r,t+k),(r,b-k));arc(n+'br',(r,b-k),(r-k,b),k)
            line(n+'b',(r-k,b),(l+k,b));arc(n+'bl',(l+k,b),(l,b-k),k)
            line(n+'l',(l,b-k),(l,t+k));arc(n+'tl',(l,t+k),(l+k,t),k)
            contour(n,*[n+x for x in ['t','tr','r','br','b','bl','l','tl']],closed=True)
        box('frame',6,6,42,42)
        poly('chevron',(28,15),(19,24),(28,33))
