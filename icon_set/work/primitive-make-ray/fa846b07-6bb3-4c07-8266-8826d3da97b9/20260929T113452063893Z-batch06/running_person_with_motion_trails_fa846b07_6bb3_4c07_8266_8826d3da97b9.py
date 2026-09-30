"""Rejected runner had comma-like motion dots. Restore long sweeping trails, a larger head and clear running limbs. Four source trails reduced to two.
Symbol plan: human_ref/full_body_ref.png; head lower16 and neck24 give exact4 ink gap.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fa846b07-6bb3-4c07-8266-8826d3da97b9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__running-person-with-motion-trails/20260929T112503Z-thuan-mac/reference/safety fire exit 1_fa846b07-6bb3-4c07-8266-8826d3da97b9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'running-person-with-motion-trails'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('running', 'person', 'with', 'motion', 'trails')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        circle('head',18,11,5)
        path('torso',(18,24),[('C',(15,33),(18,27),(17,30))])
        poly('arms',(6,28),(10,24),(18,24),(24,29),(28,26));join('arms','torso')
        poly('legs',(6,42),(15,33),(23,40),(27,40));join('legs','torso')
        path('trail-top',(34,8),[('A',(42,16),8,8,True)])
        path('trail-bottom',(34,30),[('A',(42,38),8,8,True)])
        self.mark_human_figure('runner',head='head',torso='torso-0',torso_junction='start')
