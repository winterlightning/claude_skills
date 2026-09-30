"""The rejected vibrating controller lost its controls and placed vibration strokes above and below. Restore side vibration arcs and a central direction pad within rounded gamepad grips.
Symbol plan: Lucide gamepad-2: rounded hanging grips and crossed pad; original side vibration marks. One control retained to give the side arcs room.
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

        path('body',(17,8),[('L',(31,8)),('C',(36,16),(35,8),(36,12)),('L',(36,34)),('A',(30,40),6,6,True),('C',(24,32),(27,40),(28,32)),('C',(18,40),(20,32),(21,40)),('A',(12,34),6,6,True),('L',(12,16)),('C',(17,8),(12,12),(13,8))],True)
        poly('pad-h',(21,20),(24,20),(27,20));poly('pad-v',(24,17),(24,20),(24,23));join('pad-h','pad-v')
        path('buzz-left',(4,10),[('L',(4,24)),('L',(4,38))])
        path('buzz-right',(44,10),[('L',(44,24)),('L',(44,38))])
