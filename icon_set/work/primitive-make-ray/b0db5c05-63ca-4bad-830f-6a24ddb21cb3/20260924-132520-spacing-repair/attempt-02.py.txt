"""emoji gaming lover hug 1. Plan: SQUARE extremes (6,6)-(42,42); mirrored smiling head behind a two-grip controller with exact shared side junctions. Lucide gamepad-2 informs broad top and paired grips. Eyes and tiny cross control omitted to retain the smile and open controller shape; no torso is depicted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b0db5c05-63ca-4bad-830f-6a24ddb21cb3'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/emoji gaming lover hug 1_b0db5c05-63ca-4bad-830f-6a24ddb21cb3.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'smiling-face-behind-game-controller'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('emoji', 'gaming', 'lover', 'hug', '1')
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
        self.path('face',(8,32),[((6,24),18,18,True),((24,6),18,18,True),((42,24),18,18,True),((40,32),18,18,True)])
        self.add_bezier('controller',(8,32),((9,29),(11,29),(14,29)),((20,29),(28,29),(34,29)),((37,29),(39,29),(40,32)),((41,34),(42,36),(42,38)),((42,41),(41,42),(38,42)),((35,42),(33,38),(30,38)),((26,38),(22,38),(18,38)),((15,38),(13,42),(10,42)),((7,42),(6,41),(6,38)),((6,36),(7,34),(8,32)))
        self.add_contour('gamepad','controller',closed=True)
        self.relate('connect','face','gamepad')
        self.add_arc('smile',(20,17),(28,17),radius_x=4,radius_y=3,sweep=False)
