from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4eff967d-5df4-43e4-98a7-d78f84b1fc39'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kermit-face/20260925T034349Z-thuan-mac/reference/kermit_4eff967d-5df4-43e4-98a7-d78f84b1fc39.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kermit-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # Frog face with two bulging eyes, wide mouth and a pointed collar.
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

        circle('eye-l',14,12,6);circle('eye-r',34,12,6)
        poly('left',(8,12),(6,28),(14,34));poly('right',(40,12),(42,28),(34,34))
        join('eye-l','left');join('eye-r','right')
        poly('collar',(14,34),(10,42),(21,38),(24,42),(27,38),(38,42),(34,34))
        join('left','collar');join('right','collar')
        arc('mouth',(17,26),(31,26),10,4,s=False)
