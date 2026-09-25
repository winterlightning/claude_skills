'Opposed diagonal hands with a rounded thumb and broad clean wrist contours.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: handshake: diagonal interlocking grip and rounded fingertips; human_ref/user.svg reviewed for human construction.\nOmissions: Individual finger creases reduced to one broad grip.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e18ed81a-df3e-442f-9876-54ac0d744866'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/clasp_e18ed81a-df3e-442f-9876-54ac0d744866.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='interlocking-handshake'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('interlocking', 'handshake')
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

        path('outer',(6,18),[('L',(18,6)),('L',(26,10)),('C',(34,8),(29,6),(32,6)),('L',(40,14)),('C',(42,20),(42,16),(42,18)),('C',(38,26),(42,22),(40,24)),('L',(42,30)),('L',(30,42)),('L',(26,42)),('L',(6,26)),('L',(6,18))],True)
        path('grip',(26,10),[('L',(18,18)),('C',(24,24),(16,20),(21,27)),('L',(30,18)),('L',(38,26))])
        join('grip','outer')
