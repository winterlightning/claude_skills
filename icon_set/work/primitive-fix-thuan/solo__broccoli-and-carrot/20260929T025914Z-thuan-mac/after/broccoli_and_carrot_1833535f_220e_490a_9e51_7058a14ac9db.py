"""Restored a tilted carrot with a leafy top and a distinct branching broccoli stalk beneath rounded florets; separated the two silhouettes.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide carrot: tapered diagonal root and top leaves; supplied reference defines broccoli lobes and arrangement.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Fine floret detail and carrot grooves omitted to separate the two vegetables clearly."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1833535f-220e-490a-9e51-7058a14ac9db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broccoli-and-carrot/20260929T025914Z-thuan-mac/reference/broccoli carrot_1833535f-220e-490a-9e51-7058a14ac9db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broccoli-and-carrot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('broccoli', 'and', 'carrot')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. Preserve two distinct vegetables with a tilted tapered root and leafy top beside the broccoli crown and stalk. Intentional crown/stalk connections, close floret lobes and natural envelope retain the source identities. The vegetables were separated after native review; tiny carrot grooves were removed. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'e5f58f7834d43f686d62acdd7e1b1d94ee00a85d1b50f74399c90ebdece4f5aa'}

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

        path('florets',(9,23),[('C',(4,18),(5,25),(2,22)),('C',(9,11),(4,13),(6,10)),('L',(12,11)),('C',(22,11),(14,3),(21,3)),('C',(26,16),(26,10),(28,13)),('C',(20,23),(28,21),(24,25)),('C',(14,24),(18,26),(16,26)),('L',(9,23))],True)
        path('stalk',(10,24),[('L',(14,34)),('L',(19,34)),('L',(21,24))])
        path('carrot',(36,22),[('C',(40,31),(41,22),(43,27)),('C',(27,42),(36,36),(30,40)),('C',(25,38),(24,44),(24,40)),('C',(30,25),(25,32),(28,26)),('C',(36,22),(32,23),(34,22))],True)
        self.add_polyline('greens',(36,22),(36,14),(42,12))
        self.add_line('leaf',(36,22),(44,19))
        self.relate('connect','carrot','greens');self.relate('connect','carrot','leaf');self.relate('connect','greens','leaf')
