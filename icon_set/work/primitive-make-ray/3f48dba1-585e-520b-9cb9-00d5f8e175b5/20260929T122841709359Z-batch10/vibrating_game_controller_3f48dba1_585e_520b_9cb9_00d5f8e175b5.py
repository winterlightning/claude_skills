"""The rejected vibration controller lost its controls and moved the vibration arcs above and below. Restore the gamepad controls and side vibration marks.
Symbol plan: Lucide gamepad-2 original and atoms for paired controls and rounded grips; reference side vibration arcs.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3f48dba1-585e-520b-9cb9-00d5f8e175b5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vibrating-game-controller/20260929T122443Z-thuan-mac/reference/haptic sensor vibration controller_3f48dba1-585e-520b-9cb9-00d5f8e175b5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'vibrating-game-controller'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('vibrating', 'game', 'controller')

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

        path('body',(16,16),[('L',(32,16)),('A',(36,20),4,4,True),('L',(36,36)),('A',(32,40),4,4,True),('L',(28,32)),('L',(20,32)),('L',(16,40)),('A',(12,36),4,4,True),('L',(12,20)),('A',(16,16),4,4,True)],True)
        poly('pad-h',(19,24),(21,24),(23,24));poly('pad-v',(21,22),(21,24),(21,26));join('pad-h','pad-v')
        self.add_dot('button',(30,24))
        path('buzz-left',(6,8),[('C',(4,24),(4,12),(4,18)),('C',(6,38),(4,30),(4,34))])
        path('buzz-right',(42,8),[('C',(44,24),(44,12),(44,18)),('C',(42,38),(44,30),(44,34))])
