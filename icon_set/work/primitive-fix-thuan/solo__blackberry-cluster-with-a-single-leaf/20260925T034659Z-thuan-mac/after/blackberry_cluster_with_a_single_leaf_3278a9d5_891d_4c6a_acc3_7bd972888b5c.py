from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3278a9d5-891d-4c6a-acc3-7bd972888b5c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__blackberry-cluster-with-a-single-leaf/20260925T034659Z-thuan-mac/reference/blackberry_3278a9d5-891d-4c6a-acc3-7bd972888b5c.svg'
AUTHOR = 'gpt-6'
# Plan: Lobed blackberry cluster with curved drupelet divisions and one upright attached leaf; remove strawberry-like dots.
# Construction reference: No useful exact Lucide match; supplied reference subject and geometric arc construction.
# Envelope: VRECT_L; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'blackberry-cluster-with-a-single-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('blackberry', 'cluster', 'with', 'a', 'single', 'leaf')
    def build(self):
        self.add_arc('crown',(14,26),(34,26),radius_x=10,radius_y=6)
        self.add_arc('right-top',(34,26),(40,32),radius_x=6)
        self.add_arc('right-bottom',(40,32),(34,38),radius_x=6)
        self.add_arc('bottom-right',(34,38),(24,44),radius_x=10,radius_y=6)
        self.add_arc('bottom-left',(24,44),(14,38),radius_x=10,radius_y=6)
        self.add_arc('left-bottom',(14,38),(8,32),radius_x=6)
        self.add_arc('left-top',(8,32),(14,26),radius_x=6)
        self.add_contour('fruit','crown','right-top','right-bottom','bottom-right','bottom-left','left-bottom','left-top',closed=True)
        self.add_arc('divider',(14,26),(34,26),radius_x=10,radius_y=6,sweep=False)
        self.add_line('lower-seam',(24,32),(24,44))
        self.relate('connect','divider','fruit')
        self.relate('connect','divider','lower-seam')
        self.relate('connect','lower-seam','fruit')
        self.add_arc('leaf-left',(24,12),(24,4),radius_x=5,radius_y=4)
        self.add_arc('leaf-right',(24,4),(24,12),radius_x=5,radius_y=4)
        self.add_contour('leaf','leaf-left','leaf-right',closed=True)
        self.add_line('stem',(24,12),(24,20))
        self.relate('connect','stem','leaf')
        self.relate('connect','stem','fruit')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
