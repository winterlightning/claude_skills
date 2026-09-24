from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c966f3f-127d-48b1-9cb4-530f9109feb3'
SOURCE_PATH = 'icon_set/work/todo-references/specialty hearing_4c966f3f-127d-48b1-9cb4-530f9109feb3.svg'
AUTHOR = 'gpt-6'
# Plan: Outer ear and inner fold beside a short sound waveform.
# References: ear: continuous outer helix and rounded lower lobe.
# Reduction: Reduced inner fold to one hooked curve; retained waveform.

class AuthoredIcon(Solo48):
    icon_id = 'specialty-hearing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('specialty', 'hearing')

    def build(self):
        self.add_arc('outer-top',(18,16),(42,16),radius_x=12,radius_y=10)
        self.add_bezier('outer-side',(42,16),((42,29),(34,27),(34,34)))
        self.add_arc('lobe',(34,34),(18,34),radius_x=8)
        self.add_contour('outer','outer-top','outer-side','lobe')
        self.add_bezier('inner',(23,18),((26,10),(35,13),(36,19)))
        self.add_bezier('fold',(23,18),((33,16),(34,27),(28,28)),((26,29),(29,33),(23,33)))
        self.relate('connect','inner','fold')
        self.add_polyline('sound',(6,24),(9,24),(12,28),(16,20),(19,25),(22,25))

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
