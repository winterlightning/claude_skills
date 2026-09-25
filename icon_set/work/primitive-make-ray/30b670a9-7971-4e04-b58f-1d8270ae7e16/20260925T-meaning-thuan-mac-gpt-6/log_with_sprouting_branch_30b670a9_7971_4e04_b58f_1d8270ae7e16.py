from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '30b670a9-7971-4e04-b58f-1d8270ae7e16'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__log-with-sprouting-branch/20260925T034349Z-thuan-mac/reference/tree log_30b670a9-7971-4e04-b58f-1d8270ae7e16.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'log-with-sprouting-branch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # Diagonal cylindrical tree log with a broad end-grain ring. Omit the small branch to emphasize the original tree-log concept.
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

        arc('cut-a',(12,15),(22,39),13);arc('cut-b',(22,39),(12,15),13)
        contour('cut','cut-a','cut-b',closed=True)
        line('top',(12,15),(31,8));arc('end',(31,8),(44,31),13,23);line('bottom',(44,31),(22,39))
        join('cut','top');join('cut','bottom');join('top','end');join('end','bottom')
        circle('grain',17,27,4)
