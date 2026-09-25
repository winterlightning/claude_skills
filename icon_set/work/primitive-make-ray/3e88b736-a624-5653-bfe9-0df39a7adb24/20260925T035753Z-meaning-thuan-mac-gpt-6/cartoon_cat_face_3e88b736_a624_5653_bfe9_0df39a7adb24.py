from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3e88b736-a624-5653-bfe9-0df39a7adb24'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cartoon-cat-face/20260925T035753Z-thuan-mac/reference/cat 1_3e88b736-a624-5653-bfe9-0df39a7adb24.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'cartoon-cat-face'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # Cat face with mirrored pointed ears, a round jaw and whiskers on each cheek. Shared axis 24 controls ears, eyes, nose and whiskers.
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

        poly('ears',(10,26),(10,8),(20,16),(28,16),(38,8),(38,26))
        arc('jaw',(38,26),(10,26),14);join('ears','jaw')
        for i,side in enumerate([-1,1]):
            cheek=(24+side*14,26)
            for j,y in enumerate([22,34]):
                n=f'whisker-{i}-{j}'
                line(n,cheek,(24+side*20,y));join('ears',n);join('jaw',n)
            join(f'whisker-{i}-0',f'whisker-{i}-1')
            self.add_dot('eye-'+str(i),(24+side*6,24))
        poly('nose',(22,31),(24,33),(26,31))
