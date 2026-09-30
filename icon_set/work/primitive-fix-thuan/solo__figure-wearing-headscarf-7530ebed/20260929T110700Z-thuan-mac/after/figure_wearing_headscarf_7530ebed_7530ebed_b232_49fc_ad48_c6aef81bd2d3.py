'Closed the headscarf around the circular face and attached distinct broad shoulders at shared cloth endpoints.\nOriginal/current comparison: The rejected scarf is an open arch that runs into the shoulders, losing the wrapped lower edge around the face.\nPlan: VRECT_L, bounds (6, 2, 42, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/user.svg for a circular blank face and broad shoulders; source headscarf is one continuous clothing outline. No detached head/body pair.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7530ebed-b232-49fc-ad48-c6aef81bd2d3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__figure-wearing-headscarf-7530ebed/20260929T110700Z-thuan-mac/reference/muslim man outfit 1_7530ebed-b232-49fc-ad48-c6aef81bd2d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'figure-wearing-headscarf-7530ebed'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('figure', 'wearing', 'headscarf', '7530ebed')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):arc(n+str(j),a,b,r)
            con(n,*(n+str(j) for j in range(4)),closed=True)
        def path(n,start,steps,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{i}';members.append(m)
                if kind=='L': line(m,here,end)
                elif kind=='A': arc(m,here,end,*args)
                elif kind=='C': bez(m,here,(args[0],args[1],end))
                here=end
            con(n,*members,closed=closed)
        def rect(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad),('L',(r,b-rad)),('A',(r-rad,b),rad),('L',(l+rad,b)),('A',(l,b-rad),rad),('L',(l,t+rad)),('A',(l+rad,t),rad)],True)

        circle('face',24,18,5)
        path('scarf',(24,4),[('A',(38,18),14),('L',(38,22)),('C',(32,32),(38,27),(36,30)),('C',(24,34),(30,34),(26,34)),('C',(16,32),(22,34),(18,34)),('C',(10,22),(12,30),(10,27)),('L',(10,18)),('A',(24,4),14)],True)
        bez('shoulder-left',(8,44),((8,38),(12,34),(16,32)))
        bez('shoulder-right',(32,32),((36,34),(40,38),(40,44)))
        join('shoulder-left','scarf');join('shoulder-right','scarf')
