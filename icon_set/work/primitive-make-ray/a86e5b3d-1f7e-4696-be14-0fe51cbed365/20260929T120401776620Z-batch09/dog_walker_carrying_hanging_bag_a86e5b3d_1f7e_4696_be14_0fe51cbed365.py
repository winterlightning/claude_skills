"""Dog walker: rejected bag is a ring and dog is a bare angular stick. Restore hanging bag shape, dog head/back, and natural person proportions. Reshape bag as a hanging teardrop and restore a low dog back with upright ear and muzzle.
Symbol plan: human_ref/full_body_ref.png: radius5 head bottom18 to neck26 exact4 ink gap; original hanging bag and dog.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a86e5b3d-1f7e-4696-be14-0fe51cbed365'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dog-walker-carrying-hanging-bag/20260929T115456Z-thuan-mac/reference/dog poop clean_a86e5b3d-1f7e-4696-be14-0fe51cbed365.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'dog-walker-carrying-hanging-bag'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('dog', 'walker', 'carrying', 'hanging', 'bag')

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

        circle('head',19,13,5)
        line('torso',(19,26),(19,31));poly('legs',(19,40),(19,31),(27,40));join('legs','torso')
        poly('bag-arm',(19,26),(15,26),(8,22));join('bag-arm','torso')
        path('bag',(8,22),[('C',(4,35),(7,27),(4,32)),('A',(12,35),4,5,False),('C',(8,22),(12,31),(9,27))],True);join('bag','bag-arm')
        poly('leash',(19,26),(26,26),(34,32));join('leash','torso');join('leash','bag-arm')
        poly('dog',(34,40),(34,32),(44,32),(44,24),(40,20));join('dog','leash')
        line('foreleg',(44,32),(44,40));join('foreleg','dog')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
