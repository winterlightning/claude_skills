"""The rejected conveyor had rectangular divisions and a T-shaped worker. Restore a curved upper torso beside the box and dot rollers inside a deeper conveyor bed.
Symbol plan: human_ref/user.svg circular head and curved shoulders; exact4 ink gap from head14 to shoulder22. Rollers simplified to dots.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a73f189d-afeb-4835-99c1-01f3a49dee0f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__worker-beside-box-on-conveyor/20260929T124732Z-thuan-mac/reference/factory manufacturing line worker_a73f189d-afeb-4835-99c1-01f3a49dee0f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'worker-beside-box-on-conveyor'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('worker', 'beside', 'box', 'on', 'conveyor')

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

        circle('head',15,10,4)
        path('torso',(6,26),[('A',(15,22),9,4,True),('A',(24,26),9,4,True)])
        box('belt',6,26,42,42,8);join('torso','belt')
        poly('package',(32,26),(32,14),(42,14),(42,26));join('package','belt')
        for i,x in enumerate((16,32)):self.add_dot(f'roller-{i}',(x,34))
