from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b100eb65-29b9-42da-a61f-4629d1676fd9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gaming-console-and-controller/20260925T034349Z-thuan-mac/reference/xbox series x joy_b100eb65-29b9-42da-a61f-4629d1676fd9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gaming-console-and-controller'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # Upright console behind a gamepad with a directional cross and action button.
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

        poly('console',(6,18),(6,6),(24,6),(24,18))
        arc('pad-tl',(6,26),(14,18),8);line('pad-top',(14,18),(34,18));arc('pad-tr',(34,18),(42,26),8)
        poly('grips',(42,26),(42,42),(32,36),(16,36),(6,42),(6,26))
        join('pad-tl','pad-top');join('pad-top','pad-tr');join('pad-tr','grips');join('grips','pad-tl');join('console','pad-top')
        line('dpad-v',(17,26),(17,28));line('dpad-h',(15,27),(19,27));join('dpad-v','dpad-h')
        self.add_dot('button',(32,27))
