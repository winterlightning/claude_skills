from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0a473297-da88-4e1f-8691-703bcbdef5cb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__capped-carpenter-beside-a-hand-saw/20260925T035753Z-thuan-mac/reference/avatar carpenter_0a473297-da88-4e1f-8691-703bcbdef5cb.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'capped-carpenter-beside-a-hand-saw'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # Capped carpenter head beside an upright hand saw with three coarse teeth and a large rectangular handle opening; preserve the reference layout.
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*p,closed=False): self.add_contour(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,k=4):
            line(n+'t',(l+k,t),(r-k,t));arc(n+'tr',(r-k,t),(r,t+k),k)
            line(n+'r',(r,t+k),(r,b-k));arc(n+'br',(r,b-k),(r-k,b),k)
            line(n+'b',(r-k,b),(l+k,b));arc(n+'bl',(l+k,b),(l,b-k),k)
            line(n+'l',(l,b-k),(l,t+k));arc(n+'tl',(l,t+k),(l+k,t),k)
            contour(n,*[n+x for x in ['t','tr','r','br','b','bl','l','tl']],closed=True)

        poly('saw',(4,40),(4,8),(16,8),(12,14),(16,18),(12,22),(16,28),(16,40),closed=True)
        line('handle-top',(4,28),(16,28));join('saw','handle-top')
        arc('cap',(28,16),(44,16),8)
        line('brim',(24,16),(44,16));join('cap','brim')
        line('face-r',(44,16),(44,24));arc('jaw',(44,24),(28,24),8);line('face-l',(28,24),(28,16))
        contour('face','face-r','jaw','face-l')
        join('cap','face');join('brim','face')
