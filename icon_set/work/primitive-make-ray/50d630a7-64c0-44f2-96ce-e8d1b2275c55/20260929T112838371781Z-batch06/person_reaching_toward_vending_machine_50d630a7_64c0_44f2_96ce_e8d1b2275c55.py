"""Rejected machine looked like a narrow cabinet with two dots. Widen the vending face, add a distinct product window and delivery compartment, and soften the reaching arm.
Symbol plan: human_ref/full_body_ref.png: head radius5 and torso26 give exact4 ink gap; rounded rectangular machine.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '50d630a7-64c0-44f2-96ce-e8d1b2275c55'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reaching-toward-vending-machine/20260929T112503Z-thuan-mac/reference/eat vending machine_50d630a7-64c0-44f2-96ce-e8d1b2275c55.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'person-reaching-toward-vending-machine'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'reaching', 'toward', 'vending', 'machine')

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

        circle('head',9,13,5)
        line('torso',(9,26),(9,32));poly('legs',(4,40),(9,32),(14,40))
        path('arm',(9,26),[('L',(17,30)),('L',(24,30))])
        path('machine',(24,30),[('L',(24,11)),('A',(27,8),3,3,True),('L',(41,8)),('A',(44,11),3,3,True),('L',(44,37)),('A',(41,40),3,3,True),('L',(27,40)),('A',(24,37),3,3,True),('L',(24,30))],True)
        line('shelf',(24,30),(44,30))
        circle('product',34,18,2)
        join('torso','legs');join('torso','arm');join('arm','machine');join('shelf','machine');join('shelf','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
