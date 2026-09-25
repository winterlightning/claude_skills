'Circular spiral candy and a straight upright stick, with tangent-connected outer turns.\nPlan: VRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: lollipop: concentric circular silhouette and inward semicircle progression.\nOmissions: Tight innermost turn simplified.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a6f3f418-9129-4fb0-abbb-79cc66b9dabb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/lollipop_a6f3f418-9129-4fb0-abbb-79cc66b9dabb.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='spiral-lollipop-on-upright-stick'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('spiral', 'lollipop', 'on', 'upright', 'stick')
    def build(self):

        def path(name,start,commands,closed=False):
            point=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,point,end)
                elif kind=='A': self.add_arc(member,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,point,(args[0],args[1],end))
                point=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        # Outer circle remains truly circular; the curling stripe meets it at the right extreme.
        path('candy',(24,36),[('A',(8,20),16,16,True),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('A',(24,36),16,16,True)])
        path('swirl',(40,20),[('A',(16,20),12,8,True),('A',(24,12),8,8,True)])
        join('swirl','candy')
        line('stick',(24,36),(24,44));join('stick','candy')
