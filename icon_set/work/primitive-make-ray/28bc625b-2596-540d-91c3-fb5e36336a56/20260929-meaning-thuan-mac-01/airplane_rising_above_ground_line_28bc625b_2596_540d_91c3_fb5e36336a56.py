"""Restored the downward swept wing, small tail fin, rounded nose and rising fuselage above a ground line.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide plane-takeoff: rounded fuselage and ground line; original owns the downward main wing.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Small tail/body corner irregularities simplified; wing direction retained."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '28bc625b-2596-540d-91c3-fb5e36336a56'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__airplane-rising-above-ground-line/20260929T025914Z-thuan-mac/reference/plane land_28bc625b-2596-540d-91c3-fb5e36336a56.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'airplane-rising-above-ground-line'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('airplane', 'rising', 'above', 'ground', 'line')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. Preserve the source downward swept wing and shallow rising fuselage. The natural silhouette has narrow wing/tail channels and intentionally less height than the square envelope; the runway is detached and the wing direction is clear at 48px. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '3465fc37ab3865f3a1cd74db0abaaa90a343d49f4cfaa47c234a62d5c922542a'}

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

        path('plane',(6,17),[('L',(11,17)),('L',(16,22)),('L',(35,14)),('C',(42,17),(39,12),(42,13)),('C',(39,21),(42,19),(41,20)),('L',(29,25)),('L',(24,35)),('L',(19,37)),('L',(21,27)),('L',(14,30)),('C',(10,28),(12,31),(11,30)),('L',(6,17))],True)
        self.add_line('ground',(6,42),(42,42))
 