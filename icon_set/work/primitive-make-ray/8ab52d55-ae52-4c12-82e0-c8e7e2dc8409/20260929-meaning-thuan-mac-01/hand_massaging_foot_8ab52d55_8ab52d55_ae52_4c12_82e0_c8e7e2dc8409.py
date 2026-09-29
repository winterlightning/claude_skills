"""Restored a sole with unequal rounded toes, heel and arch, plus a thumb pressing the sole and fingers wrapping around the foot.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide hand and hand-grab: rounded fingertip sequence and continuous grip; original supplies foot anatomy and massage contact.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Four toe bumps retained rather than five cramped marks; one arch crease and one finger crease."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8ab52d55-ae52-4c12-82e0-c8e7e2dc8409'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-massaging-foot-8ab52d55/20260929T025914Z-thuan-mac/reference/massage foot_8ab52d55-ae52-4c12-82e0-c8e7e2dc8409.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-massaging-foot-8ab52d55'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('hand', 'massaging', 'foot', '8ab52d55')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. Preserve the rounded heel, unequal toes, arch and wrapping massage thumb. Narrow toe gaps and the hand/foot contact are intentional anatomical details. Four toe bumps and one arch crease keep the sole identifiable without crowding it with all source lines. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '156fe29cf3c2b5bdd4bb8470e77a8f5216c1241396fcd54e7cfc016cf23c0fc6'}

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

        path('foot',(20,38),[('C',(7,35),(13,44),(7,41)),('C',(6,18),(5,30),(6,23)),('L',(6,10)),('C',(15,10),(3,1),(17,1)),('L',(15,13))])
        path('toes',(15,8),[('C',(21,11),(17,4),(22,6)),('C',(27,14),(23,7),(28,9)),('C',(31,18),(29,11),(33,13))])
        curve('arch',(11,28),(11,23),(14,20),(18,19))
        path('massage-hand',(30,44),[('L',(29,39)),('L',(19,28)),('C',(23,24),(16,24),(20,21)),('L',(29,31)),('L',(33,22)),('L',(30,20)),('C',(33,16),(26,17),(29,14)),('L',(39,19)),('C',(44,28),(43,20),(45,24)),('L',(40,38)),('L',(40,44))])
        self.add_line('finger-crease',(38,20),(37,27))
 