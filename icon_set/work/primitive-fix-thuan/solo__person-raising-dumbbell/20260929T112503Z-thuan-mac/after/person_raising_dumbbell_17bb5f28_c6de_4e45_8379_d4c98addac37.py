"""Rejected lifter had a rigid elbow and horizontal dumbbell. Restore a diagonal weight with wider plate spacing, a bent lifting arm and stable lunge.
Symbol plan: human_ref/full_body_ref.png: radius5 head lower16 neck24 exact4 ink gap; original diagonal dumbbell.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '17bb5f28-c6de-4e45-8379-d4c98addac37'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-raising-dumbbell/20260929T112503Z-thuan-mac/reference/exercise_17bb5f28-c6de-4e45-8379-d4c98addac37.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'person-raising-dumbbell'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'raising', 'dumbbell')

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
        line('torso',(11,24),(11,34))
        poly('left-arm',(11,24),(6,27));join('torso','left-arm')
        poly('right-arm',(11,24),(24,28),(33,17));join('torso','right-arm')
        poly('legs',(6,42),(11,34),(25,38),(25,42));join('torso','legs')
        poly('bar',(26,10),(33,17),(40,24))
        poly('weight-a',(24,12),(26,10),(28,8));poly('weight-b',(38,26),(40,24),(42,22))
        join('bar','weight-a');join('bar','weight-b');join('right-arm','bar')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
