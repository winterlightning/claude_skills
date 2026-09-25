'A symmetric pointed sponge, two circular pores, and a tangent continuous rounded lower body.\nPlan: VRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: droplet: single smooth silhouette and circular base.\nOmissions: Two radius-3 circular pores preserve small open centers.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4527205d-f4e9-4989-85e1-f0ba94c4cdd5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/vegetable konjac_4527205d-f4e9-4989-85e1-f0ba94c4cdd5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='konjac-sponge'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('konjac', 'sponge')
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

        # Shared axis and mirrored control points preserve the sponge symmetry.
        axis=24
        path('sponge',(axis,4),[('C',(40,28),(38,13),(40,20)),('A',(8,28),16,16,True),('C',(axis,4),(8,20),(10,13))],True)
        for i,y in enumerate((18,32)): circle(f'pore-{i}',axis,y,3)
