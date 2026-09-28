from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0c533236-5c40-40d9-bfbe-74a4e6fe6dcd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bow-and-arrow-reference/20260925T034659Z-thuan-mac/reference/rama navami_0c533236-5c40-40d9-bfbe-74a4e6fe6dcd.svg'
AUTHOR = 'gpt-6'
# Plan: Conventional curved vertical bow, taut straight string and rightward nocked arrow; remove confusing diagonal double-arrow shape.
# Construction reference: No useful exact Lucide match; supplied reference subject and geometric arc construction.
# Envelope: VRECT_L; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'bow-and-arrow-reference'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('bow', 'and', 'arrow', 'reference')
    def build(self):
        self.add_arc('bow-top',(8,4),(24,24),radius_x=16,radius_y=20)
        self.add_arc('bow-bottom',(24,24),(8,44),radius_x=16,radius_y=20)
        self.add_contour('bow','bow-top','bow-bottom')
        self.add_polyline('string',(8,4),(8,24),(8,44))
        self.add_polyline('shaft',(8,24),(24,24),(40,24))
        self.add_polyline('arrowhead',(32,16),(40,24),(32,32))
        self.relate('connect','bow','string')
        self.relate('connect','bow','shaft')
        self.relate('connect','string','shaft')
        self.relate('connect','shaft','arrowhead')

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
