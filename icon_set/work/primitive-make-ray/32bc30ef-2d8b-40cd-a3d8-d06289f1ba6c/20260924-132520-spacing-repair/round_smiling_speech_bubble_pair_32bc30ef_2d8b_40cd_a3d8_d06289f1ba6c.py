"""conversation smile type 1. Plan: SQUARE extremes (6,6)-(42,42); smaller foreground reply shares two exact occlusion nodes with large smiling bubble. Lucide messages-square informs coherent overlap. Eye dots omitted to retain the defining smile and both tails."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '32bc30ef-2d8b-40cd-a3d8-d06289f1ba6c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_12/conversation smile type 1_32bc30ef-2d8b-40cd-a3d8-d06289f1ba6c.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'round-smiling-speech-bubble-pair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('conversation', 'smile', 'type', '1')
    def path(self,n,start,steps,closed=False):
        here=start;members=[]
        for k,step in enumerate(steps):
            ident=f'{n}-{k}';members.append(ident)
            if len(step)==2:
                self.add_line(ident,here,step);here=step
            else:
                end,rx,ry,sweep=step
                self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep);here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,q=0):
        if q==0:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True)
        else:self.path(n,(l+q,t),[(r-q,t),((r,t+q),q,q,True),(r,b-q),((r-q,b),q,q,True),(l+q,b),((l,b-q),q,q,True),(l,t+q),((l+q,t),q,q,True)],True)
    def build(self):
        self.path('back',(34,26),[(34,20),((20,6),14,14,False),((6,20),14,14,False),((10,29),14,14,False),(6,38),(16,33),(20,34),(26,34)])
        self.path('front',(34,26),[((42,34),8,8,True),(39,37),(42,42),(34,40),((26,34),8,6,True),((34,26),8,8,True)],True)
        self.relate('connect','back','front')
        self.add_arc('smile',(15,18),(25,18),radius_x=5,radius_y=4,sweep=False)
