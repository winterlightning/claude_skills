from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5b3e332a-d46c-498c-b0ae-13caae896b54'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horned-demon-face/20260925T034349Z-thuan-mac/reference/smiley face horns demon_5b3e332a-d46c-498c-b0ae-13caae896b54.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horned-demon-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # A round devil face with two pointed horns, slanted eyes and a smirk.
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

        poly('crown',(6,24),(6,6),(16,16),(32,16),(42,6),(42,24))
        arc('jaw',(42,24),(6,24),18)
        join('crown','jaw')
        line('eye-left',(15,24),(18,25));line('eye-right',(33,24),(30,25))
        line('smirk',(20,33),(28,33))
