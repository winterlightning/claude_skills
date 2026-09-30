"""Crowned visitor: rejected tent looks like a bottle and the shoulders are detached too far. Restore broad tent roof and body and closer natural bust. Broaden the tent roof and restore a longer tent body beside the crowned bust.
Symbol plan: human_ref/user.svg: circular jaw and close shoulders; crown and tent retain original layout.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd473ee00-6198-4285-ab1a-64b68f5f176e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crowned-visitor-beside-a-tent/20260929T115456Z-thuan-mac/reference/amusement park_d473ee00-6198-4285-ab1a-64b68f5f176e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'crowned-visitor-beside-a-tent'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('crowned', 'visitor', 'beside', 'a', 'tent')
    human_construction = "bust"
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

        poly('tent-roof',(4,20),(12,8),(20,20),closed=True)
        poly('tent-body',(8,20),(6,38),(18,38),(16,20));join('tent-body','tent-roof')
        poly('crown',(28,8),(32,12),(36,8),(40,12),(44,8),(42,20),(30,20),closed=True)
        path('jaw',(30,20),[('A',(42,20),6,6,False)]);join('jaw','crown')
        path('shoulders',(26,40),[('A',(36,30),10,10,True),('A',(44,34),10,10,True),('L',(44,40))]);join('jaw','shoulders')
