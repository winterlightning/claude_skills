from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cab69194-7d72-4ec5-92ef-c43974df941f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__four-piece-jigsaw-puzzle/20260925T034349Z-thuan-mac/reference/jigsaw_cab69194-7d72-4ec5-92ef-c43974df941f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-piece-jigsaw-puzzle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # Four pieces with two broad interlocking seams; shared center and square envelope.
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

        poly('frame',(6,6),(24,6),(42,6),(42,24),(42,42),(24,42),(6,42),(6,24),closed=True)
        line('v1',(24,6),(24,10));arc('tab1',(24,10),(24,20),5,s=False);line('v2',(24,20),(24,24))
        line('v3',(24,24),(24,28));arc('tab2',(24,28),(24,38),5);line('v4',(24,38),(24,42))
        contour('vertical','v1','tab1','v2','v3','tab2','v4')
        line('h1',(6,24),(24,24));line('h2',(24,24),(42,24));contour('horizontal','h1','h2')
        join('frame','vertical');join('frame','horizontal');join('vertical','horizontal')
