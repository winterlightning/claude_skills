"""amazon web service codepipeline 1. Plan: equal side brackets and rotationally paired chevrons around the slanted slash; central slanted slash. HRECT_L extremes (4,8)-(44,40). Lucide code informs coherent chevron strokes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '12be411f-98cd-4c43-b650-b16b090dc516'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon web service codepipeline 1_12be411f-98cd-4c43-b650-b16b090dc516.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'amazon-web-service-codepipeline-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('amazon', 'web', 'service', 'codepipeline', '1')
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
        self.add_polyline('left-rail',(8,8),(4,8),(4,40),(8,40))
        self.add_polyline('right-rail',(40,8),(44,8),(44,40),(40,40))
        self.add_polyline('left-chevron',(16,19),(12,24),(14,29))
        self.add_polyline('right-chevron',(34,19),(36,24),(32,29))
        self.add_line('slash',(25,14),(23,34))
