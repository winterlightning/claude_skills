"""Restored a hand reaching diagonally from the upper right to pinch the card edge, with a clear thumb and a separate identity portrait.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide id-card and hand-grab: card/portrait hierarchy and grip. human_ref/user.svg: head (17,25), r3 and shoulder apex (17,36) yield exactly 4px detached ink gap.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Card text omitted, preserving the portrait and the stealing/pinching gesture."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3ba267b5-9ca9-4999-a24d-b73d45e0c937'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-stealing-identity-card-solo-b005-06/20260929T025914Z-thuan-mac/reference/identity stolen id card_3ba267b5-9ca9-4999-a24d-b73d45e0c937.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-stealing-identity-card-solo-b005-06'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('hand', 'stealing', 'identity', 'card', 'solo', 'b005', '06')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. Preserve a diagonal hand pinching the identity card rather than three abstract prongs. Intentional overlap at the card edge and tight portrait/frame spacing retain both the grip and card identity. Head-to-shoulder ink gap is exactly 4px and the shoulder curve stays detached from the border. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '5ace621c62bb64dbe373da29cf95e452e9c649e10bf14f985646a4db536a755c'}

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

        path('card',(29,16),[('L',(9,16)),('A',(6,19),3,False),('L',(6,41)),('A',(9,44),3,False),('L',(33,44)),('A',(36,41),3,False),('L',(36,24))])
        circle('head',17,25,3)
        path('shoulders',(10,38),[('C',(17,36),(11,36),(14,36)),('C',(24,38),(20,36),(23,36))])
        path('hand-top',(42,6),[('L',(36,10)),('L',(28,10)),('C',(24,12),(26,10),(25,11)),('L',(20,16))])
        path('pinch',(31,16),[('L',(26,22)),('C',(30,27),(22,26),(27,30)),('L',(37,21)),('L',(42,19))])
