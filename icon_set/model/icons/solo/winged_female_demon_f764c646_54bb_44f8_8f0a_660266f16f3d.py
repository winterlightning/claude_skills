'Horned female demon with mirrored bat wings, a triangular dress and a curled pointed tail.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/full_body_ref.png: circular head and torso alignment; source defines horns, dress and tail.\nOmissions: Finger details and separate feet omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f764c646-54bb-44f8-8f0a-660266f16f3d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/04-f764c646-54bb-44f8-8f0a-660266f16f3d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='winged-female-demon'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "video-games"
    aliases=()
    keywords=('winged', 'female', 'demon')
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

        circle('head',24,11,4)
        for x in (20,28):line(f'horn-{x}',(x,11),(x,6));join(f'horn-{x}','head')
        poly('torso',(24,23),(24,27),(24,33))
        self.mark_human_figure('demon',head='head',torso='torso-1',torso_junction='start')
        poly('dress',(24,33),(16,42),(32,42),(24,33));join('dress','torso')
        for side in (-1,1):
         x=lambda d:24+side*d
         path(f'wing-{side}',(24,27),[('L',(x(18),20)),('C',(x(14),32),(x(18),25),(x(16),29))])
         join(f'wing-{side}','torso')
        join('wing--1','wing-1')
        path('tail',(32,42),[('A',(42,32),10,10,False)]);join('tail','dress')
        poly('tail-tip',(37,32),(42,32),(42,37));join('tail-tip','tail')
