"""Restored a separate tall cargo box, sloped cab with a windshield division, and two equal round wheels with clear hubs.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide truck: cargo/cab hierarchy and wheel-aligned baseline. Source defines windshield separator.
Keyshape: HRECT_L; bounds checked and any deliberate optical deviation recorded.
Reduction: Minor source contour irregularities simplified."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0070eae2-79f7-4131-b3be-164ea822745d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__box-delivery-truck/20260929T025914Z-thuan-mac/reference/carrier_0070eae2-79f7-4131-b3be-164ea822745d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'box-delivery-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('box', 'delivery', 'truck')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. The defining sloped windshield produces a small triangular opening above the front wheel. Preserve that cab division, cargo box and two equal open wheels rather than reverting to an undivided block. Native inspection confirms all three features remain legible. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '951e64809d1ccdbcf19ed1169bd85103d7c4dee8577f58a13d2ff2d20cab6620'}

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

        path('cargo',(6,34),[('L',(4,34)),('L',(4,10)),('A',(6,8),2,True),('L',(26,8)),('A',(28,10),2,True),('L',(28,34)),('L',(18,34))])
        path('cab',(28,13),[('L',(35,13)),('L',(44,24)),('L',(44,34)),('L',(42,34))])
        self.add_line('windshield',(28,24),(44,24))
        self.add_line('underbody',(28,34),(30,34))
        circle('rear-wheel',12,34,6);circle('front-wheel',36,34,6)
        for a,b in [('cargo','cab'),('cab','windshield'),('cargo','windshield'),('cargo','underbody'),('underbody','front-wheel'),('cargo','rear-wheel'),('cab','front-wheel')]:self.relate('connect',a,b)
 