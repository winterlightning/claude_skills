'Harpy with a human head, feather-shaped outstretched wings, a torso and splayed birdlike legs.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/full_body_ref.png: circular detached head and coherent torso; bird: tapered wings.\nOmissions: Hair, face detail and individual feathers reduced; asymmetric legs preserve the profile pose.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b87b798c-92b9-4644-b23b-705c2c8cf361'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_22/harpy_b87b798c-92b9-4644-b23b-705c2c8cf361.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='winged-harpy-profile'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('winged', 'harpy', 'profile')
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

        circle('head',24,10,4)
        poly('torso',(24,22),(24,24),(24,34),(24,36))
        self.mark_human_figure('harpy',head='head',torso='torso-1',torso_junction='start')
        for side in (-1,1):
         x=lambda d:24+side*d
         path(f'wing-{side}',(24,24),[('C',(x(18),17),(x(7),23),(x(14),20)),('C',(x(12),34),(x(18),28),(x(18),34)),('C',(24,34),(x(8),34),(x(4),34))])
         join(f'wing-{side}','torso')
        poly('leg-left',(24,36),(18,42),(14,42));join('leg-left','torso')
        poly('leg-right',(24,36),(32,42),(36,42));join('leg-right','torso');join('leg-left','leg-right')
