"""Rejected lifter held a horizontal weight with a rigid right-angle arm. Restore the diagonal dumbbell, bent elbow and lunging legs.
Symbol plan: human_ref/full_body_ref.png; reference diagonal dumbbell and lunge. Head radius5 at14,11 torso24 exact4 gap.
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

        circle('head',14,11,5)
        line('torso',(14,24),(14,32))
        poly('left-arm',(14,24),(6,28),(6,32));join('torso','left-arm')
        poly('right-arm',(14,24),(26,30),(36,20));join('torso','right-arm')
        poly('legs',(6,42),(14,32),(26,34),(26,42));join('torso','legs')
        line('bar',(30,14),(36,20));line('bar-b',(36,20),(42,26))
        line('weight-a',(26,18),(34,10));line('weight-b',(38,30),(46,22))
        join('bar','bar-b');join('right-arm','bar');join('right-arm','bar-b');join('bar','weight-a');join('bar-b','weight-b')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
