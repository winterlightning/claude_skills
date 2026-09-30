"""The rejected gamepad had no controls and vibration bars above and below. Restore a central direction pad, rounded paired grips and vibration marks beside the controller.
Symbol plan: Lucide gamepad-2 rounded grips and crossed pad; source side vibration marks. One central pad preserves space at native size.
Keyshape HRECT_M: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3f48dba1-585e-520b-9cb9-00d5f8e175b5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vibrating-game-controller/20260929T122443Z-thuan-mac/reference/haptic sensor vibration controller_3f48dba1-585e-520b-9cb9-00d5f8e175b5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'vibrating-game-controller'
    keyshape = Keyshape.HRECT_M
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

        path('body',(17,13),[('L',(31,13)),('C',(36,18),(35,13),(36,15)),('L',(36,31)),('A',(30,37),6,6,True),('C',(24,33),(27,37),(28,33)),('C',(18,37),(20,33),(21,37)),('A',(12,31),6,6,True),('L',(12,18)),('C',(17,13),(12,15),(13,13))],True)
        poly('pad-h',(21,23),(24,23),(27,23));poly('pad-v',(24,22),(24,23),(24,24));join('pad-h','pad-v')
        line('buzz-left',(4,10),(4,38));line('buzz-right',(44,10),(44,38))
