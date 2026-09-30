"""The rejected commuter carried a tiny square case and raised a rigid horizontal arm. Widen the case, bend the carrying arm and angle the forward arm down as in the reference.
Symbol plan: human_ref/full_body_ref.png; outlined head and round-ended moving limbs; exact4 ink gap at actual torso junction.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '22bd302b-7cdc-4d13-8f4e-efe2bab54d50'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walking-commuter-with-briefcase/20260929T122443Z-thuan-mac/reference/coffee delivery_22bd302b-7cdc-4d13-8f4e-efe2bab54d50.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'walking-commuter-with-briefcase'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('walking', 'commuter', 'with', 'briefcase')

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

        circle('head',29,11,5)
        line('torso',(29,24),(29,33))
        poly('legs',(23,42),(29,33),(39,42));join('legs','torso')
        path('front',(29,24),[('C',(42,28),(34,24),(36,28))]);join('front','torso')
        poly('back',(29,24),(16,24),(12,29));join('back','torso')
        poly('case',(6,29),(12,29),(16,29),(16,37),(6,37),closed=True);join('case','back')
        self.mark_human_figure('commuter',head='head',torso='torso',torso_junction='start')
