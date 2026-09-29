"""Restored the shallow wide canoe hull and one smooth curved gunwale, removing the unrelated braces.
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

        path('hull',(4,10),[('C',(24,17),(10,16),(17,17)),('C',(44,10),(31,17),(38,16)),('L',(44,29)),('C',(35,38),(44,36),(41,38)),('L',(13,38)),('C',(4,29),(7,38),(4,36)),('L',(4,10))],True)
 