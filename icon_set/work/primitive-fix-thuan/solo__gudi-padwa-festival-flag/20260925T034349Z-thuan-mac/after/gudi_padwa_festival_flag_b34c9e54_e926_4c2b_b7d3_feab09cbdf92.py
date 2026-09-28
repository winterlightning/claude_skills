from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b34c9e54-e926-4c2b-b7d3-feab09cbdf92'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gudi-padwa-festival-flag/20260925T034349Z-thuan-mac/reference/gudi padwa_b34c9e54-e926-4c2b-b7d3-feab09cbdf92.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gudi-padwa-festival-flag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # Inverted ceremonial pot on a tall pole with a draped festival cloth.
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

        poly('pot',(8,16),(10,4),(24,4),(26,16),closed=True)
        line('pole',(17,16),(17,44));join('pot','pole')
        poly('cloth',(17,24),(40,24),(40,40),(29,36),(17,40))
        join('pole','cloth')
