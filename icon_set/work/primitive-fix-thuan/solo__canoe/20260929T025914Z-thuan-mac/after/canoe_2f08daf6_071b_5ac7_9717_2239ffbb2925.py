"""Restored a low, wide empty canoe with raised bow/stern and a smooth curved gunwale; removed braces and compressed the hull to its natural shallow proportions.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: No useful exact local Lucide canoe match; source supplies shallow hull, raised bow/stern and smooth gunwale.
Keyshape: HRECT_M; bounds checked and any deliberate optical deviation recorded.
Reduction: Removed all invented hull furniture; preserves the empty canoe shown in the original."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2f08daf6-071b-5ac7-9717-2239ffbb2925'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__canoe/20260929T025914Z-thuan-mac/reference/canoe_2f08daf6-071b-5ac7-9717-2239ffbb2925.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'canoe'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('canoe',)

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. The shallow source canoe should remain low and wide. Accept a smaller vertical footprint than HRECT_M rather than enlarging it into a basket. The empty hull and smoothly curved gunwale pass all non-envelope automatic checks and are clear at native size. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '47c5ef0dab7f6590ee1656c17318583566b9ef29fad87169286fe25054298b06'}

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

        path('hull',(4,18),[('C',(24,25),(10,23),(17,25)),('C',(44,18),(31,25),(38,23)),('L',(44,27)),('C',(24,34),(44,33),(33,34)),('C',(4,27),(15,34),(4,33)),('L',(4,18))],True)
