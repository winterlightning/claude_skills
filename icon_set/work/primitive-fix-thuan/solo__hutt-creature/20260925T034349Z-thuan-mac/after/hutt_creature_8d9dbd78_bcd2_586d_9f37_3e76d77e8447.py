from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8d9dbd78-bcd2-586d-9f37-3e76d77e8447'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hutt-creature/20260925T034349Z-thuan-mac/reference/hutt_8d9dbd78-bcd2-586d-9f37-3e76d77e8447.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hutt-creature'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # Broad slug-like alien with a heavy face, arms and a curling tail.
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

        arc('head',(14,24),(44,24),15,16)
        line('side',(44,24),(44,31));arc('lower',(44,31),(35,40),9)
        line('base',(35,40),(13,40));arc('tail',(13,40),(4,31),9)
        poly('tail-tip',(4,31),(4,24),(10,30),(14,30),(14,24))
        for a,b in [('head','side'),('side','lower'),('lower','base'),('base','tail'),('tail','tail-tip'),('tail-tip','head')]:join(a,b)
        self.add_dot('eye-l',(24,20));self.add_dot('eye-r',(34,20))
        line('mouth',(24,30),(35,30))
