"""Rejected car was a pentagonal box and seated person rigid. Restore windshield above bumper, paired wheels and a curved seated torso with reaching arm.
Symbol plan: human_ref/full_body_ref.png; head lower16 to neck24 exact4 ink gap. Lucide car-front original and atoms: windshield, bumper, wheels.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd870fd26-4ba9-4393-b85f-95ba5e7e4786'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-person-beside-front-facing-car/20260929T112503Z-thuan-mac/reference/disability in car_d870fd26-4ba9-4393-b85f-95ba5e7e4786.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'seated-person-beside-front-facing-car'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('seated', 'person', 'beside', 'front', 'facing', 'car')

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

        circle('head',11,11,5)
        path('torso',(11,24),[('L',(11,30)),('A',(16,35),5,5,False)])
        poly('legs',(16,35),(22,35),(28,42));join('torso','legs')
        poly('arm',(11,24),(17,27),(19,27));join('arm','torso')
        poly('roof',(26,14),(29,6),(39,6),(42,14))
        box('car',26,14,42,24,2);join('roof','car')
        line('wheel-l',(28,24),(28,27));line('wheel-r',(40,24),(40,27));join('wheel-l','car');join('wheel-r','car')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
