"""Restored overlapping hands of different sizes, diagonal fingers, a raised rear thumb and a smaller foreground palm.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide hand: rounded fingers and a coherent palm outline. Original defines two overlapping hands and relative size.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Four-finger silhouettes reduced to three visible foreground fingers and two partial rear fingers to preserve separation."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b88757c2-b1ab-49df-9283-b755a2874066'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__adult-child-high-five-hands/20260929T025914Z-thuan-mac/reference/play together_b88757c2-b1ab-49df-9283-b755a2874066.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'adult-child-high-five-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('adult', 'child', 'high', 'five', 'hands')

    def build(self):

        def curve(name,start,c1,c2,end): self.add_bezier(name,start,(c1,c2,end))
        def path(name,start,steps,closed=False):
            point=start;ids=[]
            for j,(kind,end,*args) in enumerate(steps):
                part=f'{name}-{j}'
                if kind=='L':self.add_line(part,point,end)
                elif kind=='C':curve(part,point,args[0],args[1],end)
                elif kind=='A':self.add_arc(part,point,end,radius_x=args[0],sweep=args[1])
                ids.append(part);point=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):path(name,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,True)],True)

        path('rear-hand',(42,40),[('L',(38,35)),('C',(38,24),(39,31),(39,28)),('L',(36,12)),('C',(30,12),(35,7),(30,7)),('L',(29,23)),('L',(15,8)),('C',(10,12),(11,3),(6,8)),('L',(19,21))])
        path('rear-fingers',(10,12),[('C',(7,18),(5,10),(3,15)),('L',(13,24))])
        path('rear-little',(7,18),[('C',(8,28),(1,18),(4,24))])
        path('small-hand',(13,42),[('C',(6,34),(8,42),(6,39)),('C',(9,27),(6,31),(7,29)),('L',(21,15)),('C',(25,19),(25,12),(28,16)),('L',(18,26)),('L',(28,18)),('C',(32,22),(32,15),(35,19)),('L',(24,30)),('L',(32,24)),('C',(36,28),(36,21),(39,25)),('L',(26,36)),('L',(29,35)),('C',(31,40),(33,33),(35,38)),('L',(21,42)),('C',(13,42),(18,44),(15,43))],True)
 