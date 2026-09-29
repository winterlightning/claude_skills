"""Restored a rounded palm, a long distinct downward index, three folded finger lobes and a short angled thumb.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide hand: shared fingertip radii and continuous palm. Original determines the downward pointing direction.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: No identifying parts omitted; thumb contour and fingertip lobes rebuilt with coherent curves."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5a80cb54-e04f-5e41-ba53-6892a6852f05'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-pointing-down-batch-024-04/20260929T025914Z-thuan-mac/reference/hand pointer bottom_5a80cb54-e04f-5e41-ba53-6892a6852f05.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-pointing-down-batch-024-04'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('hand', 'pointing', 'down', 'batch', '024', '04')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. Preserve the long downward index and three curled finger lobes with a short thumb. Their natural narrow fingertip channels and slightly asymmetric optical bounds are intentional. The pointing direction and palm are immediately readable at 48px. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '0a2d81d4794997fc6f415fbd5d0006cc5dc6cee5b42bc11d2b21b3c83d406452'}

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

        path('hand',(15,24),[('L',(15,39)),('C',(23,39),(15,45),(23,45)),('L',(23,28)),('C',(29,29),(23,34),(29,34)),('L',(29,25)),('C',(35,26),(29,31),(35,31)),('L',(35,23)),('C',(41,24),(35,29),(41,29)),('L',(41,17)),('C',(28,6),(41,8),(36,6)),('L',(23,6)),('C',(16,10),(20,6),(18,8)),('L',(7,20)),('C',(11,26),(3,25),(7,29)),('L',(15,22))])
 