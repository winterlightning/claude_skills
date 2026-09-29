"""Restored a continuous diagonal spine, smooth handle and five evenly spaced comb teeth with a squared terminal tooth.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: No useful exact local Lucide comb match; source supplies a diagonal continuous spine and regular tooth series.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Five teeth retained as a regular series; tiny handle irregularities removed."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dafdca17-4d27-4cd9-935d-01a08f4e53e2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handled-comb-on-diagonal/20260929T025914Z-thuan-mac/reference/hair dress comb_dafdca17-4d27-4cd9-935d-01a08f4e53e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'handled-comb-on-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('handled', 'comb', 'on', 'diagonal')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. Five closely spaced teeth define a comb. Preserve their regular diagonal series and actual shared inner-spine attachment instead of reducing them to a three-tooth rake. Tooth channels and the natural diagonal footprint are optically approved at 48px. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '005058f055201470db8e06852ead24d6e37ce46eebd195f8c9494f02e1bddb60'}

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

        path('spine',(16,31),[('L',(10,37)),('C',(5,32),(6,42),(1,37)),('L',(29,8)),('C',(35,8),(31,6),(33,6)),('L',(42,15))])
        # Five identical tooth runs; common spacing along the diagonal spine.
        for j in range(5):
            x=16+4*j;y=31-4*j
            self.add_line(f'tooth-{j}',(x,y),(x+7,y+7))
 
        self.add_line('inner-spine',(16,31),(32,15))
        self.relate('connect','spine','inner-spine')
        for j in range(5):self.relate('connect','inner-spine',f'tooth-{j}')
