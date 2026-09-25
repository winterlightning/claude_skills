from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '946bcf00-d07c-50b9-a9c6-2ef6fc891352'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__howling-wolf-with-sound/20260925T034349Z-thuan-mac/reference/wolf howl_946bcf00-d07c-50b9-a9c6-2ef6fc891352.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'howling-wolf-with-sound'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # A long raised muzzle, pointed ear and curved neck, with a separate howl wave.
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

        poly('profile',(6,42),(10,28),(6,23),(17,22),(27,8),(31,20),(27,30))
        arc('neck',(27,30),(32,42),18,s=False)
        join('profile','neck')
        arc('howl',(36,6),(42,24),6,18)
