"""Rejected sling was a symmetric triangle detached from a natural arm. Restore a diagonal head bandage and an asymmetric sling across the torso with an elbow on the left.
Symbol plan: human_ref/user.svg circular jaw/shoulders, head bottom20 and shoulder top24 touching ink.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '483f0053-0d76-4f90-9c4a-d241bc144520'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-with-head-bandage-and-arm-sling/20260929T112503Z-thuan-mac/reference/bandage shoulder head_483f0053-0d76-4f90-9c4a-d241bc144520.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'person-with-head-bandage-and-arm-sling'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'with', 'head', 'bandage', 'and', 'arm', 'sling')
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

        circle('head',24,12,8)
        line('bandage',(17,16),(31,8));join('head','bandage')
        path('shoulders',(8,44),[('L',(8,40)),('A',(24,24),16,16,True),('A',(40,40),16,16,True),('L',(40,44))])
        join('head','shoulders')
        poly('sling',(24,24),(32,44),(16,44));join('sling','shoulders')
        path('arm',(8,36),[('L',(8,40)),('A',(12,44),4,4,False),('L',(16,44))]);join('arm','shoulders');join('arm','sling')
