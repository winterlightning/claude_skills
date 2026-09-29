"""Restored a gently curved horizontal hand and wrist above two tall flowing heat waves, preserving the sensing-heat gesture.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide hand: coherent palm/thumb contour; source owns side-on horizontal hand and heat waves.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Three short heat marks replaced with two longer recognizable rising waves."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e2391138-4aaf-4587-83d5-f636e7ba5379'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-over-heat/20260929T025914Z-thuan-mac/reference/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-over-heat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('hand', 'over', 'heat')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. Preserve the side-on palm and wrist with a narrow thumb/palm channel, separated above two tall rising heat waves. Its naturally horizontal envelope differs from square. Native review confirms the sensing-heat gesture remains clear in both themes. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '29d8853fdb5221aa8bae6105e7dc77633e82d8aa6e60f994462adc81646f52f4'}

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

        path('hand-top',(36,8),[('L',(26,8)),('C',(17,11),(23,8),(20,10)),('L',(7,17)),('C',(10,24),(1,20),(4,27)),('L',(22,18)),('L',(29,18))])
        path('palm',(19,20),[('C',(24,26),(20,25),(21,26)),('L',(33,26)),('C',(39,22),(36,26),(38,24)),('L',(44,14))])
        for name,x in [('left',14),('right',29)]:
            curve(name,(x,32),(x-4,37),(x+4,39),(x,44))
 