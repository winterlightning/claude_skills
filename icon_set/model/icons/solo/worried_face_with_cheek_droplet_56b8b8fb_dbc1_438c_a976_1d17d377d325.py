'A round worried face with inward-raised brows, simple eyes, an arched frown and a cheek droplet.\nPlan: CIRCLE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: user-round: circular head; source-specific facial arrangement.\nOmissions: Tiny eye marks merged into worried eye/brow strokes; the round droplet retains a straight upper tip and open center.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '56b8b8fb-dbc1-438c-a976-1d17d377d325'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/face sad sweat_56b8b8fb-dbc1-438c-a976-1d17d377d325.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='worried-face-with-cheek-droplet'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('worried', 'face', 'with', 'cheek', 'droplet')
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

        circle('head',24,24,20)
        path('brow-left',(16,18),[('C',(20,16),(18,18),(20,17))])
        path('brow-right',(28,16),[('C',(32,18),(28,17),(30,18))])
        path('frown',(17,33),[('A',(23,33),3,3,True)])
        circle('droplet',32,25,3)
        line('drop-tip',(32,18),(32,22));join('drop-tip','droplet');join('drop-tip','brow-right')
