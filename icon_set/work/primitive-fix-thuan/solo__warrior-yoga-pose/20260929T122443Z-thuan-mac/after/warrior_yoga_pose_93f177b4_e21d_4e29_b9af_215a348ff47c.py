"""The rejected warrior pose had a very short torso and a nearly horizontal rear leg. Lengthen the torso and open a clear bent forward knee and diagonal straight rear leg.
Symbol plan: human_ref/full_body_ref.png: round-ended limbs and circle head; head bottom14 to torso22 gives4 ink gap.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '93f177b4-e21d-4e29-b9af-215a348ff47c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__warrior-yoga-pose/20260929T122443Z-thuan-mac/reference/yoga_93f177b4-e21d-4e29-b9af-215a348ff47c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'warrior-yoga-pose'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('warrior', 'yoga', 'pose')

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

        circle('head',24,10,4)
        line('torso',(24,22),(24,32))
        poly('arms',(6,22),(24,22),(42,22));join('arms','torso')
        poly('legs',(10,42),(10,34),(24,32),(38,42));join('legs','torso')
        self.mark_human_figure('warrior',head='head',torso='torso',torso_junction='start')
