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

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. The original is a close-up of overlapping adult and child hands. Preserve the occluded finger overlaps, rounded fingertip channels and larger rear thumb rather than replacing them with people. Tight finger spaces remain visually distinct at 48px after reducing and opening the foreground fingers. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6f06b94b172d3c624a5ee03d55cbbcfa8d7eab4bf608600aef5b6178c8b0137b'}

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

        path('rear-thumb',(42,40),[('L',(38,35)),('L',(38,24)),('L',(36,12)),('C',(30,12),(35,7),(30,7)),('L',(30,17))])
        path('rear-index',(28,18),[('L',(15,8)),('C',(10,12),(11,3),(6,8)),('L',(17,19))])
        path('rear-middle',(10,12),[('C',(7,18),(5,10),(3,15)),('L',(13,23))])
        path('rear-little',(7,18),[('C',(8,28),(1,18),(4,24))])
        path('small-hand',(13,42),[('C',(6,34),(8,42),(6,39)),('C',(9,27),(6,31),(7,29)),('L',(20,16)),('C',(25,20),(25,11),(30,16)),('L',(29,17)),('C',(32,22),(34,13),(37,18)),('C',(35,28),(37,20),(40,24)),('L',(26,36)),('L',(30,35)),('C',(32,40),(35,33),(36,38)),('L',(21,42)),('C',(13,42),(18,43),(15,43))],True)
        self.add_line('finger-a',(25,20),(17,28))
        self.add_line('finger-b',(32,22),(24,30))
        self.relate('connect','small-hand','finger-a');self.relate('connect','small-hand','finger-b')
