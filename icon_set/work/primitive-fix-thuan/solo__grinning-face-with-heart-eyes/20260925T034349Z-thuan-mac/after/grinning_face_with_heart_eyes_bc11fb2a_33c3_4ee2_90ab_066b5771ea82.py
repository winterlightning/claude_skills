from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bc11fb2a-33c3-4ee2-90ab-066b5771ea82'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__grinning-face-with-heart-eyes/20260925T034349Z-thuan-mac/reference/face grin hearts_bc11fb2a-33c3-4ee2-90ab-066b5771ea82.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'grinning-face-with-heart-eyes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # Two large outlined heart eyes and a grin; omit the enclosing face circle to preserve legal readable heart openings.
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

        for i,x in enumerate([12,36]):
            n='heart'+str(i)
            arc(n+'a',(x,12),(x-8,12),4,s=False)
            poly(n+'b',(x-8,12),(x,23),(x+8,12))
            arc(n+'c',(x+8,12),(x,12),4,s=False)
            join(n+'a',n+'b');join(n+'b',n+'c');join(n+'a',n+'c')
        line('mouth-top',(12,32),(36,32));arc('mouth-bottom',(36,32),(12,32),12,8)
        contour('mouth','mouth-top','mouth-bottom',closed=True)
