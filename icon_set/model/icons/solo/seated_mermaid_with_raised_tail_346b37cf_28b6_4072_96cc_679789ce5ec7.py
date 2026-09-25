'Seated mermaid with circular head, vertical torso, supporting arm and curved fishtail ending in a forked fluke.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/full_body_ref.png: circular head and coherent limbs; detached head lower 14 to torso 22 gives exact 4 ink gap.\nOmissions: Hair and internal tail scales omitted; forked tail restored.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '346b37cf-28b6-4072-96cc-679789ce5ec7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/05-346b37cf-28b6-4072-96cc-679789ce5ec7.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='seated-mermaid-with-raised-tail'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('seated', 'mermaid', 'with', 'raised', 'tail')
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

        circle('head',16,10,4)
        line('torso',(16,22),(16,32))
        self.mark_human_figure('mermaid',head='head',torso='torso',torso_junction='start')
        poly('support-arm',(16,22),(8,25),(6,42));join('support-arm','torso')
        path('tail',(16,32),[('C',(30,42),(18,39),(23,42)),('C',(40,31),(37,42),(40,38)),('L',(40,27)),('L',(34,27)),('C',(26,32),(32,30),(29,32)),('L',(16,32))],True);join('tail','torso')
        path('fluke',(34,27),[('C',(28,17),(30,26),(28,22)),('L',(36,21)),('L',(42,16)),('C',(40,27),(42,22),(42,25))]);join('fluke','tail')
